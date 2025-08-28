/**
 * Extend the base Actor document by defining a custom roll data structure which is ideal for the Simple system.
 * @extends {Actor}
 */
export class Anima extends Actor {
  /** @override */
  prepareData() {
    // Prepare data for the actor. Calling the super version of this executes
    // the following, in order: data reset (to clear active effects),
    // prepareBaseData(), prepareEmbeddedDocuments() (including active effects),
    // prepareDerivedData().
    super.prepareData();
  }

  /** @override */
  prepareBaseData() {
    // Data modifications in this step occur before processing embedded
    // documents or derived data.
  }

  /**
   * @override
   * Augment the actor source data with additional dynamic data. Typically,
   * you'll want to handle most of your calculated/derived data in this step.
   * Data calculated in this step should generally not exist in template.json
   * (such as ability modifiers rather than ability scores) and should be
   * available both inside and outside of character sheets (such as if an actor
   * is queried and has a roll executed directly from it).
   */
  prepareDerivedData() {
    const actorData = this;
    const systemData = actorData.system;
    const flags = actorData.flags.anima || {};

    // Calculate characteristic modifiers first
    this._calculateCharacteristicModifiers(systemData);

    // Calculate derived combat values
    this._calculateCombatValues(systemData);

    // Calculate magic values
    this._calculateMagicValues(systemData);

    // Calculate health and fatigue based on characteristics
    this._calculateVitalStatistics(systemData);

    // Initialize secondary abilities if they don't exist
    this._initializeSecondaryAbilities(systemData);

    // Make separate methods for each Actor type (character, npc, etc.) to keep
    // things organized.
    this._prepareCharacterData(actorData);
    this._prepareNpcData(actorData);
  }

  /**
   * Calculate characteristic modifiers for Anima Beyond Fantasy
   */
  _calculateCharacteristicModifiers(systemData) {
    // Calculate modifiers for each characteristic
    // In Anima, the modifier is the characteristic value divided by 5 (rounded down)
    for (let [key, characteristic] of Object.entries(systemData.characteristics || {})) {
      characteristic.mod = Math.floor(characteristic.value / 5);
      characteristic.modBonus = characteristic.value % 5;
    }
  }

  /**
   * Calculate derived combat values
   */
  _calculateCombatValues(systemData) {
    if (!systemData.characteristics) return;

    const char = systemData.characteristics;
    const combat = systemData.combat;

    // Attack = (Dexterity + Strength) / 2 + 20
    if (char.dexterity && char.strength) {
      combat.attack.value = Math.floor((char.dexterity.value + char.strength.value) / 2) + 20;
    }

    // Defense = (Dexterity + Agility) / 2 + 20
    if (char.dexterity && char.agility) {
      combat.defense.value = Math.floor((char.dexterity.value + char.agility.value) / 2) + 20;
    }

    // Wear Armor = (Strength + Constitution) / 2
    if (char.strength && char.constitution) {
      combat.wearArmor.value = Math.floor((char.strength.value + char.constitution.value) / 2);
    }

    // Initiative = Dexterity + Agility
    if (char.dexterity && char.agility) {
      combat.initiative.value = char.dexterity.value + char.agility.value;
    }
  }

  /**
   * Calculate magic-related values
   */
  _calculateMagicValues(systemData) {
    if (!systemData.characteristics || !systemData.magic) return;

    const char = systemData.characteristics;
    const magic = systemData.magic;

    // Magic Projection = (Power + Willpower) / 2 + 20
    if (char.power && char.willpower) {
      magic.magicProjection.value = Math.floor((char.power.value + char.willpower.value) / 2) + 20;
    }

    // Zeon maximum = Magic Accumulation * Power * 5
    if (magic.magicAccumulation && char.power) {
      magic.zeon.max = magic.magicAccumulation.value * char.power.value * 5;
    }
  }

  /**
   * Calculate vital statistics (health, fatigue)
   */
  _calculateVitalStatistics(systemData) {
    if (!systemData.characteristics) return;

    const char = systemData.characteristics;

    // Health = Constitution * 10
    if (char.constitution) {
      systemData.health.max = char.constitution.value * 10;
      // Ensure current health doesn't exceed maximum
      if (systemData.health.value > systemData.health.max) {
        systemData.health.value = systemData.health.max;
      }
    }

    // Fatigue = Willpower * 10
    if (char.willpower) {
      systemData.fatigue.max = char.willpower.value * 10;
      // Ensure current fatigue doesn't exceed maximum
      if (systemData.fatigue.value > systemData.fatigue.max) {
        systemData.fatigue.value = systemData.fatigue.max;
      }
    }
  }

  /**
   * Initialize secondary abilities with default values
   */
  _initializeSecondaryAbilities(systemData) {
    if (!systemData.secondaryAbilities) {
      systemData.secondaryAbilities = {};
    }

    const { secondaryAbilities } = CONFIG.ANIMA;

    // Initialize each category of secondary abilities
    for (const [category, abilities] of Object.entries(secondaryAbilities)) {
      if (!systemData.secondaryAbilities[category]) {
        systemData.secondaryAbilities[category] = {};
      }

      // Initialize each ability in the category
      for (const [key, abilityData] of Object.entries(abilities)) {
        if (!systemData.secondaryAbilities[category][key]) {
          systemData.secondaryAbilities[category][key] = {
            name: abilityData.name,
            value: 0,
            baseChar: abilityData.baseChar
          };
        } else {
          // Ensure name and baseChar are set
          systemData.secondaryAbilities[category][key].name = abilityData.name;
          systemData.secondaryAbilities[category][key].baseChar = abilityData.baseChar;
        }
      }
    }
  }

  /**
   * Prepare Character type specific data
   */
  _prepareCharacterData(actorData) {
    if (actorData.type !== 'character') return;

    // Additional character-specific calculations can be added here
    const systemData = actorData.system;

    // Calculate experience needed for next level (simplified)
    if (systemData.attributes?.level) {
      const level = systemData.attributes.level.value;
      systemData.experiencePointsNeeded = level * 1000; // Simplified formula
    }
  }

  /**
   * Prepare NPC type specific data.
   */
  _prepareNpcData(actorData) {
    if (actorData.type !== 'npc') return;

    // Make modifications to data here. For example:
    const systemData = actorData.system;
    systemData.xp = systemData.cr * systemData.cr * 100;
  }

  /**
   * Override getRollData() that's supplied to rolls.
   */
  getRollData() {
    // Starts off by populating the roll data with a shallow copy of `this.system`
    const data = { ...this.system };

    // Prepare character roll data.
    this._getCharacterRollData(data);
    this._getNpcRollData(data);

    return data;
  }

  /**
   * Prepare character roll data.
   */
  _getCharacterRollData(data) {
    if (this.type !== 'character') return;

    // Copy the characteristics to the top level, so that rolls can use
    // formulas like `@dexterity.mod + 4`.
    if (data.characteristics) {
      for (let [k, v] of Object.entries(data.characteristics)) {
        data[k] = foundry.utils.deepClone(v);
      }
    }

    // Copy combat values for easier access
    if (data.combat) {
      for (let [k, v] of Object.entries(data.combat)) {
        data[k] = foundry.utils.deepClone(v);
      }
    }

    // Copy magic values for easier access
    if (data.magic) {
      for (let [k, v] of Object.entries(data.magic)) {
        data[k] = foundry.utils.deepClone(v);
      }
    }

    // Add level for easier access, or fall back to 0.
    if (data.attributes?.level) {
      data.lvl = data.attributes.level.value ?? 0;
    }

    // Legacy support - copy characteristics to abilities for backward compatibility
    if (data.characteristics) {
      data.abilities = data.characteristics;
    }
  }

  /**
   * Prepare NPC roll data.
   */
  _getNpcRollData(data) {
    if (this.type !== 'npc') return;

    // Copy the characteristics to the top level for NPCs too
    if (data.characteristics) {
      for (let [k, v] of Object.entries(data.characteristics)) {
        data[k] = foundry.utils.deepClone(v);
      }
    }

    // Copy combat values for NPCs
    if (data.combat) {
      for (let [k, v] of Object.entries(data.combat)) {
        data[k] = foundry.utils.deepClone(v);
      }
    }

    // Legacy support for NPCs
    if (data.characteristics) {
      data.abilities = data.characteristics;
    }
  }
}
