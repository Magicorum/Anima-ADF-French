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

    // Calculate final values for secondary abilities
    this._calculateSecondaryAbilities(systemData);

    // Make separate methods for each Actor type (character, npc, etc.) to keep
    // things organized.
    this._prepareCharacterData(actorData);
    this._prepareNpcData(actorData);
  }

  /**
   * Calculate characteristic modifiers for Anima Beyond Fantasy
   * Using the official Anima modifier table
   */
  _calculateCharacteristicModifiers(systemData) {
    // Calculate modifiers using the official Anima table
    for (let [key, characteristic] of Object.entries(systemData.characteristics || {})) {
      // Calculate the final value from base + special + temp
      const value = (characteristic.base || 1) + (characteristic.special || 0) + (characteristic.temp || 0);

      // Official Anima modifier table - corrected
      if (value <= 1) {
        characteristic.mod = -30;
      } else if (value === 2) {
        characteristic.mod = -20;
      } else if (value === 3) {
        characteristic.mod = -10;
      } else if (value === 4) {
        characteristic.mod = -5;
      } else if (value === 5) {
        characteristic.mod = 0;
      } else if (value >= 6 && value <= 7) {
        characteristic.mod = 5;
      } else if (value >= 8 && value <= 9) {
        characteristic.mod = 10;
      } else if (value === 10) {
        characteristic.mod = 15;
      } else if (value >= 11 && value <= 12) {
        characteristic.mod = 20;
      } else if (value >= 13 && value <= 14) {
        characteristic.mod = 25;
      } else if (value === 15) {
        characteristic.mod = 30;
      } else if (value >= 16 && value <= 17) {
        characteristic.mod = 35;
      } else if (value >= 18 && value <= 19) {
        characteristic.mod = 40;
      } else if (value >= 20 && value <= 21) {
        characteristic.mod = 45;
      } else if (value >= 22 && value <= 23) {
        characteristic.mod = 50;
      } else {
        // For values above 23, continue the pattern
        characteristic.mod = 50 + Math.floor((value - 24) / 2) * 5 + (value % 2 === 0 ? 0 : 5);
      }

      // Keep the modBonus for backward compatibility (though not used in Anima)
      characteristic.modBonus = value % 5;

      // Update the final value
      characteristic.final = value;
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

    // Initialize global bonuses if they don't exist
    if (!systemData.globalBonuses) {
      systemData.globalBonuses = {
        physical: { value: 0 },
        mental: { value: 0 }
      };
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
            base: 0,
            natural: 0,
            naturalbi: 0,
            class: 0,
            special: 0,
            temp: 0,
            value: 0,
            baseChar: abilityData.baseChar
          };
        } else {
          // Ensure name and baseChar are set
          systemData.secondaryAbilities[category][key].name = abilityData.name;
          systemData.secondaryAbilities[category][key].baseChar = abilityData.baseChar;

          // Ensure all numeric fields exist
          if (systemData.secondaryAbilities[category][key].base === undefined) {
            systemData.secondaryAbilities[category][key].base = 0;
          }
          if (systemData.secondaryAbilities[category][key].natural === undefined) {
            systemData.secondaryAbilities[category][key].natural = 0;
          }
          if (systemData.secondaryAbilities[category][key].naturalbi === undefined) {
            systemData.secondaryAbilities[category][key].naturalbi = 0;
          }
          if (systemData.secondaryAbilities[category][key].class === undefined) {
            systemData.secondaryAbilities[category][key].class = 0;
          }
          if (systemData.secondaryAbilities[category][key].special === undefined) {
            systemData.secondaryAbilities[category][key].special = 0;
          }
          if (systemData.secondaryAbilities[category][key].temp === undefined) {
            systemData.secondaryAbilities[category][key].temp = 0;
          }
          if (systemData.secondaryAbilities[category][key].value === undefined) {
            systemData.secondaryAbilities[category][key].value = 0;
          }
        }
      }
    }
  }

  /**
   * Calculate final values for secondary abilities using Roll20 formula with physical/mental bonuses
   */
  _calculateSecondaryAbilities(systemData) {
    if (!systemData.secondaryAbilities || !systemData.characteristics) return;

    const char = systemData.characteristics;
    const globalBonuses = systemData.globalBonuses || {};

    // Define physical and mental characteristics
    const physicalCharacteristics = ['agility', 'constitution', 'dexterity', 'strength'];
    const mentalCharacteristics = ['intelligence', 'perception', 'power', 'willpower'];

    // Calculate each category of secondary abilities
    for (const [category, abilities] of Object.entries(systemData.secondaryAbilities)) {
      for (const [key, ability] of Object.entries(abilities)) {
        if (ability && ability.baseChar && char[ability.baseChar]) {
          // Get all the components
          const baseValue = ability.base || 0;
          const naturalValue = ability.natural || 0;
          const naturalBiValue = ability.naturalbi || 0;
          const classValue = ability.class || 0;
          const specialValue = ability.special || 0;
          const tempValue = ability.temp || 0;

          // Get characteristic modifier
          const charMod = char[ability.baseChar].mod || 0;

          // Add global bonus based on characteristic type
          let globalBonus = 0;
          if (physicalCharacteristics.includes(ability.baseChar)) {
            globalBonus = globalBonuses.physical?.value || 0;
          } else if (mentalCharacteristics.includes(ability.baseChar)) {
            globalBonus = globalBonuses.mental?.value || 0;
          }

          // Calculate final value using Anima formula:
          // Final = Base + Class + Special + Temp + Natural + NaturalBi + Char Modifier + Global Bonus
          ability.value = baseValue + classValue + specialValue + tempValue + naturalValue + naturalBiValue + charMod + globalBonus;

          // Ensure minimum value of 0
          if (ability.value < 0) {
            ability.value = 0;
          }
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

    // Copy secondary abilities for easier access in rolls
    if (data.secondaryAbilities) {
      for (let [category, abilities] of Object.entries(data.secondaryAbilities)) {
        for (let [key, ability] of Object.entries(abilities)) {
          if (ability) {
            // Copy the final calculated value
            if (ability.value !== undefined) {
              data[key] = ability.value;
            }

            // Copy individual components for roll calculations
            if (ability.base !== undefined) data[`${key}_base`] = ability.base;
            if (ability.class !== undefined) data[`${key}_class`] = ability.class;
            if (ability.special !== undefined) data[`${key}_special`] = ability.special;
            if (ability.temp !== undefined) data[`${key}_temp`] = ability.temp;
            if (ability.natural !== undefined) data[`${key}_natural`] = ability.natural;
            if (ability.naturalbi !== undefined) data[`${key}_naturalbi`] = ability.naturalbi;

            // Copy characteristic modifier and global bonus
            if (ability.baseChar && data.characteristics && data.characteristics[ability.baseChar]) {
              data[`${key}_charmod`] = data.characteristics[ability.baseChar].mod || 0;
            }

            // Calculate global bonus based on characteristic type
            let globalBonus = 0;
            const physicalCharacteristics = ['agility', 'constitution', 'dexterity', 'strength'];
            const mentalCharacteristics = ['intelligence', 'perception', 'power', 'willpower'];

            if (ability.baseChar) {
              if (physicalCharacteristics.includes(ability.baseChar)) {
                globalBonus = (data.globalBonuses?.physical?.value) || 0;
              } else if (mentalCharacteristics.includes(ability.baseChar)) {
                globalBonus = (data.globalBonuses?.mental?.value) || 0;
              }
            }
            data[`${key}_globalbonus`] = globalBonus;

            console.log(`DEBUG: Copié compétence ${key} = ${ability.value} (Base: ${ability.base}, Classe: ${ability.class}, Spécial: ${ability.special}, Temp: ${ability.temp}, Natural: ${ability.natural}, NaturalBi: ${ability.naturalbi}, CharMod: ${data[`${key}_charmod`]}, Global: ${globalBonus})`);
          }
        }
      }
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

    // Copy secondary abilities for easier access in rolls (for NPCs too)
    if (data.secondaryAbilities) {
      for (let [category, abilities] of Object.entries(data.secondaryAbilities)) {
        for (let [key, ability] of Object.entries(abilities)) {
          if (ability) {
            // Copy the final calculated value
            if (ability.value !== undefined) {
              data[key] = ability.value;
            }

            // Copy individual components for roll calculations
            if (ability.base !== undefined) data[`${key}_base`] = ability.base;
            if (ability.class !== undefined) data[`${key}_class`] = ability.class;
            if (ability.special !== undefined) data[`${key}_special`] = ability.special;
            if (ability.temp !== undefined) data[`${key}_temp`] = ability.temp;
            if (ability.natural !== undefined) data[`${key}_natural`] = ability.natural;
            if (ability.naturalbi !== undefined) data[`${key}_naturalbi`] = ability.naturalbi;

            // Copy characteristic modifier and global bonus
            if (ability.baseChar && data.characteristics && data.characteristics[ability.baseChar]) {
              data[`${key}_charmod`] = data.characteristics[ability.baseChar].mod || 0;
            }

            // Calculate global bonus based on characteristic type
            let globalBonus = 0;
            const physicalCharacteristics = ['agility', 'constitution', 'dexterity', 'strength'];
            const mentalCharacteristics = ['intelligence', 'perception', 'power', 'willpower'];

            if (ability.baseChar) {
              if (physicalCharacteristics.includes(ability.baseChar)) {
                globalBonus = (data.globalBonuses?.physical?.value) || 0;
              } else if (mentalCharacteristics.includes(ability.baseChar)) {
                globalBonus = (data.globalBonuses?.mental?.value) || 0;
              }
            }
            data[`${key}_globalbonus`] = globalBonus;

            console.log(`DEBUG NPC: Copié compétence ${key} = ${ability.value} (Base: ${ability.base}, Classe: ${ability.class}, Spécial: ${ability.special}, Temp: ${ability.temp}, Natural: ${ability.natural}, NaturalBi: ${ability.naturalbi}, CharMod: ${data[`${key}_charmod`]}, Global: ${globalBonus})`);
          }
        }
      }
    }

    // Legacy support for NPCs
    if (data.characteristics) {
      data.abilities = data.characteristics;
    }
  }
}
