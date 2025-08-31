export const ANIMA = {};

/**
 * Special abilities and powers categories
 * @type {Object}
 */
ANIMA.specialAbilities = {
  magic: {
    innate: 'ANIMA.Special.Magic.Innate',
    projection: 'ANIMA.Special.Magic.Projection',
    accumulation: 'ANIMA.Special.Magic.Accumulation'
  },
  psychic: {
    disciplines: 'ANIMA.Special.Psychic.Disciplines',
    potential: 'ANIMA.Special.Psychic.Potential',
    projection: 'ANIMA.Special.Psychic.Projection',
    points: 'ANIMA.Special.Psychic.Points'
  },
  ki: {
    points: 'ANIMA.Special.Ki.Points',
    techniques: 'ANIMA.Special.Ki.Techniques',
    accumulation: 'ANIMA.Special.Ki.Accumulation'
  },
  summoning: {
    control: 'ANIMA.Special.Summoning.Control',
    bind: 'ANIMA.Special.Summoning.Bind',
    banish: 'ANIMA.Special.Summoning.Banish'
  }
};

/**
 * Advanced features and calculations
 * @type {Object}
 */
ANIMA.advancedFeatures = {
  metamagic: 'ANIMA.Advanced.Metamagic',
  mentalPatterns: 'ANIMA.Advanced.MentalPatterns',
  spellTheorems: 'ANIMA.Advanced.SpellTheorems',
  auraExtension: 'ANIMA.Advanced.Aura.Extension',
  auraIntensity: 'ANIMA.Advanced.Aura.Intensity'
};

/**
 * Game modifiers and special rules
 * @type {Object}
 */
ANIMA.gameModifiers = {
  circumstantial: {
    fatigue: 'ANIMA.Modifiers.Fatigue',
    environmental: 'ANIMA.Modifiers.Environmental',
    positional: 'ANIMA.Modifiers.Positional',
    weather: 'ANIMA.Modifiers.Weather',
    lighting: 'ANIMA.Modifiers.Lighting'
  },
  combat: {
    flanking: 'ANIMA.Modifiers.Combat.Flanking',
    surprise: 'ANIMA.Modifiers.Combat.Surprise',
    range: 'ANIMA.Modifiers.Combat.Range',
    cover: 'ANIMA.Modifiers.Combat.Cover',
    prone: 'ANIMA.Modifiers.Combat.Prone'
  },
  skill: {
    toolBonus: 'ANIMA.Modifiers.Skill.ToolBonus',
    timePressure: 'ANIMA.Modifiers.Skill.TimePressure'
  }
};

/**
 * Status conditions and effects
 * @type {Object}
 */
ANIMA.statusEffects = {
  combat: {
    blinded: 'ANIMA.Status.Blinded',
    deafened: 'ANIMA.Status.Deafened',
    stunned: 'ANIMA.Status.Stunned',
    unconscious: 'ANIMA.Status.Unconscious',
    prone: 'ANIMA.Status.Prone',
    grappled: 'ANIMA.Status.Grappled'
  },
  magic: {
    silenced: 'ANIMA.Status.Silenced',
    antimagic: 'ANIMA.Status.Antimagic',
    confusion: 'ANIMA.Status.Confusion',
    charm: 'ANIMA.Status.Charm',
    fear: 'ANIMA.Status.Fear'
  },
  physical: {
    poisoned: 'ANIMA.Status.Poisoned',
    diseased: 'ANIMA.Status.Diseased',
    bleeding: 'ANIMA.Status.Bleeding',
    fatigued: 'ANIMA.Status.Fatigued',
    exhausted: 'ANIMA.Status.Exhausted'
  }
};

/**
 * Time and action calculations
 * @type {Object}
 */
ANIMA.timeActions = {
  combatRound: 'COMBAT_ROUND_TIME',
  actionTypes: {
    free: 'ACTION_FREE',
    swift: 'ACTION_SWIFT',
    standard: 'ACTION_STANDARD',
    fullRound: 'ACTION_FULL_ROUND',
    reaction: 'ACTION_REACTION'
  },
  movement: {
    baseSpeed: 'BASE_MOVEMENT_SPEED',
    runMultiplier: 'RUN_MOVEMENT_MULTIPLIER',
    chargeMultiplier: 'CHARGE_MOVEMENT_MULTIPLIER',
    withdrawPenalty: 'WITHDRAW_MOVEMENT_PENALTY'
  },
  timeUnits: {
    round: 6, // seconds
    minute: 60,
    hour: 3600,
    day: 86400
  }
};

/**
 * The set of Characteristics used within the Anima Beyond Fantasy system.
 * @type {Object}
 */
ANIMA.characteristics = {
  agility: 'ANIMA.Characteristic.Agility.long',
  constitution: 'ANIMA.Characteristic.Constitution.long',
  dexterity: 'ANIMA.Characteristic.Dexterity.long',
  strength: 'ANIMA.Characteristic.Strength.long',
  intelligence: 'ANIMA.Characteristic.Intelligence.long',
  perception: 'ANIMA.Characteristic.Perception.long',
  power: 'ANIMA.Characteristic.Power.long',
  willpower: 'ANIMA.Characteristic.Willpower.long',
};

ANIMA.characteristicAbbreviations = {
  agility: 'ANIMA.Characteristic.Agility.abbr',
  constitution: 'ANIMA.Characteristic.Constitution.abbr',
  dexterity: 'ANIMA.Characteristic.Dexterity.abbr',
  strength: 'ANIMA.Characteristic.Strength.abbr',
  intelligence: 'ANIMA.Characteristic.Intelligence.abbr',
  perception: 'ANIMA.Characteristic.Perception.abbr',
  power: 'ANIMA.Characteristic.Power.abbr',
  willpower: 'ANIMA.Characteristic.Willpower.abbr',
};

/**
 * Primary Characteristics (used for combat calculations)
 * @type {Object}
 */
ANIMA.primaryCharacteristics = {
  attack: 'ANIMA.Primary.Attack',
  defense: 'ANIMA.Primary.Defense',
  magicProjection: 'ANIMA.Primary.MagicProjection',
  magicLevel: 'ANIMA.Primary.MagicLevel',
  psychicPotential: 'ANIMA.Primary.PsychicPotential'
};

/**
 * Combat Abilities
 * @type {Object}
 */
ANIMA.combatAbilities = {
  attack: 'ANIMA.Combat.Attack',
  defense: 'ANIMA.Combat.Defense',
  wearArmor: 'ANIMA.Combat.WearArmor'
};

/**
 * Magic Abilities
 * @type {Object}
 */
ANIMA.magicAbilities = {
  zeon: 'ANIMA.Magic.Zeon',
  magicAccumulation: 'ANIMA.Magic.MagicAccumulation',
  magicProjection: 'ANIMA.Magic.MagicProjection',
  summon: 'ANIMA.Magic.Summon',
  control: 'ANIMA.Magic.Control',
  bind: 'ANIMA.Magic.Bind',
  banish: 'ANIMA.Magic.Banish'
};

/**
 * Secondary Abilities categories
 * @type {Object}
 */
ANIMA.secondaryAbilityCategories = {
  athletics: 'ANIMA.Secondary.Athletics',
  social: 'ANIMA.Secondary.Social',
  perceptive: 'ANIMA.Secondary.Perceptive',
  intellectual: 'ANIMA.Secondary.Intellectual',
  vitality: 'ANIMA.Secondary.Vitality',
  subterfuge: 'ANIMA.Secondary.Subterfuge',
  creative: 'ANIMA.Secondary.Creative',
  other: 'ANIMA.Secondary.Other'
};

/**
 * Secondary Abilities definitions with their base characteristics
 */
ANIMA.secondaryAbilities = {
  athletics: {
    acrobatics: { name: "Acrobatie", baseChar: "agility" },
    athleticism: { name: "Athlétisme", baseChar: "agility" },
    climb: { name: "Escalade", baseChar: "agility" },
    jump: { name: "Saut", baseChar: "strength" },
    ride: { name: "Equitation", baseChar: "agility" },
    swim: { name: "Natation", baseChar: "agility" }
  },
  social: {
    etiquette: { name: "Étiquette", baseChar: "intelligence" },
    intimidate: { name: "Intimidation", baseChar: "strength" },
    leadership: { name: "Commandement", baseChar: "power" },
    persuasion: { name: "Persuasion", baseChar: "intelligence" },
    streetwise: { name: "Conn. de la rue", baseChar: "intelligence" },
    style: { name: "Style", baseChar: "dexterity" },
    trading: { name: "Commerce", baseChar: "intelligence" }
  },
  perceptive: {
    notice: { name: "Vigilance", baseChar: "perception" },
    search: { name: "Observation", baseChar: "perception" },
    track: { name: "Pistage", baseChar: "perception" }
  },
  intellectual: {
    animals: { name: "Animaux", baseChar: "intelligence" },
    appraisal: { name: "Estimation", baseChar: "intelligence" },
    architecture: { name: "Architecture", baseChar: "intelligence" },
    herbalLore: { name: "Herboristerie", baseChar: "intelligence" },
    history: { name: "Histoire", baseChar: "intelligence" },
    law: { name: "Loi", baseChar: "intelligence" },
    magicAppraisal: { name: "E. Magique", baseChar: "intelligence" },
    medicine: { name: "Médecine", baseChar: "intelligence" },
    memorize: { name: "Mémorisation", baseChar: "intelligence" },
    navigation: { name: "Navigation", baseChar: "intelligence" },
    occult: { name: "Occultisme", baseChar: "intelligence" },
    sciences: { name: "Sciences", baseChar: "intelligence" },
    tactics: { name: "Tactique", baseChar: "intelligence" }
  },
  vigor: {
    composure: { name: "Impassibilité", baseChar: "willpower" },
    featsOfStrength: { name: "P. Force", baseChar: "strength" },
    withstandPain: { name: "Res. Douleur", baseChar: "willpower" }
  },
  subterfuge: {
    disguise: { name: "Déguisement", baseChar: "dexterity" },
    hide: { name: "Camouflage", baseChar: "perception" },
    lockpicking: { name: "Crochetage", baseChar: "dexterity" },
    poisons: { name: "Poisons", baseChar: "intelligence" },
    sleightOfHand: { name: "Hab. Manuelle", baseChar: "dexterity" },
    stealth: { name: "Discrétion", baseChar: "agility" },
    theft: { name: "Larcin", baseChar: "dexterity" },
    trapLore: { name: "Piège", baseChar: "perception" }
  },
  creative: {
    alchemy: { name: "Alchimie", baseChar: "intelligence" },
    animism: { name: "Animisme", baseChar: "power" },
    art: { name: "Art", baseChar: "power" },
    dance: { name: "Danse", baseChar: "agility" },
    forging: { name: "Forge", baseChar: "dexterity" },
    jewelry: { name: "Orfévrerie", baseChar: "dexterity" },
    music: { name: "Musique", baseChar: "power" },
    ritualCalligraphy: { name: "Calligraphie rituelle", baseChar: "dexterity" },
    rune: { name: "Runes", baseChar: "dexterity" },
    tailoring: { name: "Confection", baseChar: "dexterity" }
  }
};

/**
 * Formula calculations for various game mechanics
 * @type {Object}
 */
ANIMA.formulas = {
  /**
   * Life Points (LP) calculations
   */
  lifePoints: {
    base: '25 + 10 * (CON_FINAL) + CON_MOD - ceil((CON_FINAL - 1) / CON_FINAL) * 5',
    total: 'LP_BASE + LP_MULTIPLES * CON_FINAL + LP_CLASS + LP_SPECIAL + LP_TEMP'
  },

  /**
   * Movement calculations
   */
  movement: {
    base: 'AGI_FINAL',
    total: '((MOVEMENT_BASE + MOVEMENT_BONUS + MOVEMENT_TEMP - abs(MOVEMENT_PENALTY) + ceil(AAP / 20)) + 1 + abs((MOVEMENT_BASE + MOVEMENT_BONUS + MOVEMENT_TEMP - abs(MOVEMENT_PENALTY) + ceil(AAP / 20)) - 1)) / 2'
  },

  /**
   * Fatigue calculations
   */
  fatigue: {
    base: 'CON_FINAL',
    total: 'FATIGUE_BASE + FATIGUE_CLASS + FATIGUE_SPECIAL + FATIGUE_TEMP'
  },

  /**
   * Development Points (DP) and Presence calculations
   */
  development: {
    dp: '(CHARACTER_LEVEL * 100) + 500',
    presence: '((CHARACTER_LEVEL * 100 + 500) / 20)'
  },

  /**
   * Attack calculations for weapons
   */
  weaponAttack: {
    base: 'WEAPON_QUALITY + ATTACK_BASE + (((CLASS_ATT_SUM + 50) - abs(CLASS_ATT_SUM - 50)) / 2) + DEX_MOD + ATTACK_SPECIAL + ATTACK_TEMP + AAM + (AM_TRANS_DRA_SCEAUX * 5) + WEAPON_ATTACK_MOD',
    total: 'WEAPON_ATTACK_BASE + FATIGUE_PENALTY + MODIFIERS'
  },

  /**
   * Block calculations for weapons
   */
  weaponBlock: {
    base: 'WEAPON_QUALITY + WEAPON_SHIELD_VAL + BLOCK_BASE + ((((CLASS_PAR_SUM + 50) - abs(CLASS_PAR_SUM - 50)) / 2)) + DEX_MOD + BLOCK_SPECIAL + BLOCK_TEMP + AAM + (AM_TRANS_DRA_SCEAUX * 5) + WEAPON_BLOCK_MOD',
    total: 'WEAPON_BLOCK_BASE + FATIGUE_PENALTY + MODIFIERS'
  },

  /**
   * Dodge calculations
   */
  weaponDodge: {
    base: '(DODGE_BASE + ((((CLASS_ESQ_SUM + 50) - abs(CLASS_ESQ_SUM - 50)) / 2)) + AGI_MOD + DODGE_SPECIAL + DODGE_TEMP + AAM + (AM_TRANS_DRA_SCEAUX * 5)) + WEAPON_DODGE_MOD',
    total: 'WEAPON_DODGE_BASE + FATIGUE_PENALTY + MODIFIERS'
  },

  /**
   * Weapon damage calculations
   */
  weaponDamage: {
    base: 'WEAPON_BASE_DMG + WEAPON_STR_BONUS + WEAPON_TWO_HANDED * WEAPON_STR_BONUS + 2 * WEAPON_QUALITY + AURA_EXTENSION + INCREASED_DAMAGE',
    total: 'WEAPON_DAMAGE_BASE'
  },

  /**
   * Weapon properties calculations
   */
  weaponProperties: {
    fortitude: '2 * WEAPON_QUALITY + WEAPON_BASE_FORT + AURA_EXTENSION',
    breakage: 'WEAPON_BASE_BREAKAGE + WEAPON_STR_BREAKAGE + WEAPON_QUALITY + AURA_EXTENSION / 2',
    presence: 'WEAPON_BASE_PRESENCE + 10 * WEAPON_QUALITY',
    speed: 'WEAPON_QUALITY + WEAPON_BASE_SPEED'
  },

  /**
   * Resistance calculations
   */
  resistances: {
    physical: 'RESIST_PHYSICAL_BASE + RESIST_PHYSICAL_SPECIAL + RESIST_PHYSICAL_TEMP',
    disease: 'RESIST_DISEASE_BASE + RESIST_DISEASE_SPECIAL + RESIST_DISEASE_TEMP',
    poison: 'RESIST_POISON_BASE + RESIST_POISON_SPECIAL + RESIST_POISON_TEMP',
    magic: 'RESIST_MAGIC_BASE + RESIST_MAGIC_SPECIAL + RESIST_MAGIC_TEMP',
    psychic: 'RESIST_PSYCHIC_BASE + RESIST_PSYCHIC_SPECIAL + RESIST_PSYCHIC_TEMP'
  },

  /**
   * Magic calculations
   */
  magic: {
    projection: 'MAGIC_PROJECTION_BASE + MAGIC_PROJECTION_SPECIAL + MAGIC_PROJECTION_TEMP',
    accumulation: 'MAGIC_ACCUMULATION_BASE + MAGIC_ACCUMULATION_SPECIAL + MAGIC_ACCUMULATION_TEMP',
    zeon: 'ZEON_BASE + ZEON_SPECIAL + ZEON_TEMP'
  },

  /**
   * Initiative calculations
   */
  initiative: {
    base: 'AGI_MOD + DEX_MOD + CLASS_INIT_SUM + AM_TRANS_DRA_SCEAUX + KI_INCREASED_SPEED + AAM',
    weapon: 'INIT_WEAPON',
    armor: 'INIT_ARMOR',
    special: 'INIT_SPECIAL',
    total: 'INITIATIVE_BASE + INITIATIVE_WEAPON + INITIATIVE_ARMOR + INITIATIVE_SPECIAL'
  },

  /**
   * Characteristic rolls
   */
  rolls: {
    characteristic: '1d10 + CHARACTERISTIC_FINAL + FATIGUE_PENALTY + MODIFIERS',
    opposed: '1d10 + CHARACTERISTIC_OPPOSED_FINAL + FATIGUE_PENALTY + MODIFIERS',
    critical: '12 + CHARACTERISTIC_FINAL + FATIGUE_PENALTY + MODIFIERS'
  },

  /**
   * Combat rolls
   */
  combatRolls: {
    attack: '1d100 + ATTACK_TOTAL + FATIGUE_PENALTY + MODIFIERS',
    block: '1d100 + BLOCK_TOTAL + FATIGUE_PENALTY + MODIFIERS',
    dodge: '1d100 + DODGE_TOTAL + FATIGUE_PENALTY + MODIFIERS'
  },

  /**
   * Ki calculations
   */
  ki: {
    points: 'KI_BASE + KI_SPECIAL + KI_TEMP',
    accumulation: 'KI_ACCUMULATION_BASE + KI_ACCUMULATION_SPECIAL + KI_ACCUMULATION_TEMP'
  },

  /**
   * Psychic calculations
   */
  psychic: {
    points: 'PSYCHIC_POINTS_BASE + PSYCHIC_POINTS_SPECIAL + PSYCHIC_POINTS_TEMP',
    potential: 'PSYCHIC_POTENTIAL_BASE + PSYCHIC_POTENTIAL_SPECIAL + PSYCHIC_POTENTIAL_TEMP',
    projection: 'PSYCHIC_PROJECTION_BASE + PSYCHIC_PROJECTION_SPECIAL + PSYCHIC_PROJECTION_TEMP'
  },

  /**
   * Aura calculations
   */
  aura: {
    extension: 'AURA_EXTENSION_BASE + AURA_EXTENSION_SPECIAL + AURA_EXTENSION_TEMP',
    intensity: 'AURA_INTENSITY_BASE + AURA_INTENSITY_SPECIAL + AURA_INTENSITY_TEMP'
  },

  /**
   * Advanced combat calculations (with mastery penalties)
   */
  advancedCombat: {
    attackWithMastery: 'ATTACK_BASE + FATIGUE_PENALTY + MODIFIERS + MASTERY_PENALTY',
    blockWithMastery: 'BLOCK_BASE + FATIGUE_PENALTY + MODIFIERS + MASTERY_PENALTY',
    dodgeWithMastery: 'DODGE_BASE + FATIGUE_PENALTY + MODIFIERS + MASTERY_PENALTY'
  },

  /**
   * Spell calculations
   */
  spells: {
    level: 'SPELL_PATH_LEVEL',
    system: 'SPELL_SYSTEM',
    zeon: {
      basic: 'SPELL_BASIC_ZEON',
      intermediate: 'SPELL_INTER_ZEON',
      advanced: 'SPELL_ADVAN_ZEON',
      arcane: 'SPELL_ARCAN_ZEON'
    },
    maintenance: {
      basic: 'SPELL_BASIC_MAINT',
      intermediate: 'SPELL_INTER_MAINT',
      advanced: 'SPELL_ADVAN_MAINT',
      arcane: 'SPELL_ARCAN_MAINT'
    },
    projection: 'SPELL_PROJECTION',
    totalZeon: 'SPELL_ZEON + SPELL_ZEON_MULTI'
  },

  /**
   * Psychic disciplines calculations
   */
  psychicDisciplines: {
    points: 'PSYCHIC_POINTS_BASE + PSYCHIC_POINTS_SPECIAL + PSYCHIC_POINTS_TEMP',
    potential: 'PSYCHIC_POTENTIAL_BASE + PSYCHIC_POTENTIAL_SPECIAL + PSYCHIC_POTENTIAL_TEMP',
    projection: 'PSYCHIC_PROJECTION_BASE + PSYCHIC_PROJECTION_SPECIAL + PSYCHIC_PROJECTION_TEMP',
    innate: 'INNATE_PSYCHIC_POINTS_PER_LEVEL * CHARACTER_LEVEL'
  },

  /**
   * Ki techniques calculations
   */
  kiTechniques: {
    cost: 'KI_TECHNIQUE_COST',
    level: 'KI_TECHNIQUE_LEVEL',
    frequency: 'KI_TECHNIQUE_FREQ',
    action: 'KI_TECHNIQUE_ACTION',
    characteristicCosts: {
      agility: 'KI_TECHNIQUE_AGI_COST',
      constitution: 'KI_TECHNIQUE_CON_COST',
      dexterity: 'KI_TECHNIQUE_DEX_COST',
      strength: 'KI_TECHNIQUE_STR_COST',
      power: 'KI_TECHNIQUE_POW_COST',
      willpower: 'KI_TECHNIQUE_WP_COST'
    },
    maintenanceCosts: {
      agility: 'KI_TECHNIQUE_AGI_MAINT',
      constitution: 'KI_TECHNIQUE_CON_MAINT',
      dexterity: 'KI_TECHNIQUE_DEX_MAINT',
      strength: 'KI_TECHNIQUE_STR_MAINT',
      power: 'KI_TECHNIQUE_POW_MAINT',
      willpower: 'KI_TECHNIQUE_WPI_MAINT'
    }
  },

  /**
   * Mental patterns calculations
   */
  mentalPatterns: {
    cost: 'MENTAL_PATTERN_COST',
    total: 'MENTAL_PATTERN_TOTAL',
    cancelled: 'MENTAL_PATTERN_CANCELLED'
  },

  /**
   * Innate magic calculations
   */
  innateMagic: {
    level: 'INNATE_MAGIC',
    zeonCost: 'INNATE_MAGIC_ZEON_COST',
    maintenance: 'INNATE_MAGIC_MAINTENANCE'
  },

  /**
   * Class level calculations
   */
  classLevels: {
    totalLevel: 'CLASSE_LVL_SUM',
    lifePoints: 'CLASSE_PV_SUM',
    initiative: 'CLASSE_INIT_SUM',
    attack: 'CLASSE_ATT_SUM',
    dodge: 'CLASSE_ESQ_SUM',
    block: 'CLASSE_PAR_SUM',
    wearArmor: 'CLASSE_PORT_ARMURE',
    damageIncrease: 'CLASSE_DI',
    psychicPoints: 'CLASSE_PPP',
    zeon: 'CLASSE_ZEON'
  },

  /**
   * Special class abilities (Summoning, Control, Binding, Banishing)
   */
  specialClassAbilities: {
    summon: 'CLASSE_SUMMON',
    control: 'CLASSE_CONTROL',
    bind: 'CLASSE_BIND',
    banish: 'CLASSE_BANISH',
    totalSummon: 'CHARACTER_LEVEL * CLASSE_SUMMON',
    totalControl: 'CHARACTER_LEVEL * CLASSE_CONTROL',
    totalBind: 'CHARACTER_LEVEL * CLASSE_BIND',
    totalBanish: 'CHARACTER_LEVEL * CLASSE_BANISH'
  },



  /**
   * Summoning and creature calculations
   */
  summoning: {
    creatureLevel: 'KI_CREATURE_LEVEL',
    creatureDifficulty: '10 * (KI_CREATURE_LEVEL - CHARACTER_LEVEL)',
    seals: 'KI_CREATURE_SEALS',
    summoningRoll: '1d100 + SUMMONING_TOTAL + MODIFIERS'
  },

  /**
   * Advanced magic calculations
   */
  advancedMagic: {
    metamagicLevel: 'METAMAGIC_LEVEL',
    spellTheorems: 'SPELL_THEOREMS',
    magicInnateLevel: 'MAGIC_INNATE_LEVEL'
  },

  /**
   * Regeneration calculations
   */
  regeneration: {
    magic: {
      base: 'MA_FINAL - MA_TEMP - MA_SPECIAL + MA_REGEN_TEMP + MA_REGEN_SPECIAL + MA_POW * MA_REGEN_MULTIPLES',
      final: 'MA_REGEN_BASE * MA_SUPERIOR - DAILY_SPELL_CREATURE_TOTALCOST',
      superior: 'MA_REGEN_BASE * MA_SUPERIOR',
      multiplier: 'MA_REGEN_MULTIPLES'
    },
    ki: {
      healing: 'KI_HEALING',
      superiorHealing: 'KI_SUPERIOR_HEALING',
      recovery: 'KI_RECOVERY',
      restoreOthers: 'KI_RESTORE_OTHERS'
    },
    daily: {
      spellCreature: 'DAILY_SPELL_CREATURE_REGEN',
      final: 'MA_REGEN_FINAL'
    }
  },

  /**
   * Advantages and Disadvantages
   */
  advantagesDisadvantages: {
    advantage: {
      cost: 'ADVANTAGE_COST',
      description: 'ADVANTAGE_DESC'
    },
    disadvantage: {
      benefit: 'DISADVANTAGE_BENEFIT',
      description: 'DISADVANTAGE_DESC',
      option: 'DISADVANTAGE_OPTION'
    }
  },

  /**
   * Circumstantial modifiers
   */
  circumstantialModifiers: {
    fatigue: {
      penalty: 'FATIGUE_PENALTY',
      trad: 'FATIGUE_TRAD'
    },
    modifiers: {
      trad: 'MODIFIERS_TRAD'
    },
    openRoll: {
      threshold: 'OPEN_ROLL_THRESHOLD',
      no: 'OPEN_ROLL_NO'
    },
    fumble: {
      threshold: 'FUMBLE_THRESHOLD',
      range: 'FUMBLE_RANGE'
    }
  },





  /**
   * Superior magic and accumulation calculations
   */
  superiorMagic: {
    accumulation: {
      base: 'MA_ACCUMULATION_BASE',
      final: 'MA_ACCUMULATION_FINAL',
      superior: 'MA_SUPERIOR_ACCUMULATION',
      multiples: 'MA_ACCUMULATION_MULTIPLES'
    },
    level: {
      base: 'MA_LEVEL_BASE',
      final: 'MA_LEVEL_FINAL',
      superior: 'MA_SUPERIOR_LEVEL'
    },
    pow: {
      base: 'MA_POW_BASE',
      final: 'MA_POW_FINAL'
    }
  },

  /**
   * Equipment weight and carrying capacity
   */
  equipmentWeight: {
    carryCapacity: {
      light: 'CARRY_CAPACITY_LIGHT',
      medium: 'CARRY_CAPACITY_MEDIUM',
      heavy: 'CARRY_CAPACITY_HEAVY',
      maximum: 'CARRY_CAPACITY_MAXIMUM'
    },
    liftCapacity: {
      light: 'LIFT_CAPACITY_LIGHT',
      medium: 'LIFT_CAPACITY_MEDIUM',
      heavy: 'LIFT_CAPACITY_HEAVY'
    },
    strengthRequirement: {
      weapon: 'WEAPON_STRENGTH_REQUIREMENT',
      armor: 'ARMOR_STRENGTH_REQUIREMENT'
    },
    encumbrance: {
      light: 'ENCUMBRANCE_LIGHT',
      medium: 'ENCUMBRANCE_MEDIUM',
      heavy: 'ENCUMBRANCE_HEAVY',
      maximum: 'ENCUMBRANCE_MAXIMUM'
    }
  },

  /**
   * Combat tables and critical systems
   */
  combatTables: {
    criticalHits: {
      normal: 'CRITICAL_HIT_NORMAL',
      good: 'CRITICAL_HIT_GOOD',
      excellent: 'CRITICAL_HIT_EXCELLENT',
      magnificent: 'CRITICAL_HIT_MAGNIFICENT',
      ranges: {
        normal: 90,
        good: 85,
        excellent: 80,
        magnificent: 75
      }
    },
    fumbles: {
      normal: 'FUMBLE_NORMAL',
      poor: 'FUMBLE_POOR',
      terrible: 'FUMBLE_TERRIBLE',
      ranges: {
        normal: 10,
        poor: 15,
        terrible: 20
      }
    },
    openRolls: {
      threshold: 90,
      no: 'OPEN_ROLL_NO'
    },
    superiorCritical: {
      threshold: 'SUPERIOR_CRITICAL_THRESHOLD',
      multiplier: 'SUPERIOR_CRITICAL_MULTIPLIER'
    },
    absoluteCritical: {
      threshold: 'ABSOLUTE_CRITICAL_THRESHOLD',
      multiplier: 'ABSOLUTE_CRITICAL_MULTIPLIER'
    }
  },

  /**
   * Resting and recovery calculations
   */
  resting: {
    resting: 'RESTING_VALUE',
    notResting: 'NOT_RESTING_VALUE',
    dailyRegeneration: 'DAILY_REGENERATION',
    finalDailyRegeneration: 'FINAL_DAILY_REGENERATION'
  }
};

/**
 * Constants and multipliers used in calculations
 * @type {Object}
 */
ANIMA.constants = {
  // Fatigue penalties
  fatiguePenalty: 15,

  // Development Points multiplier per level
  dpPerLevel: 100,

  // Base DP
  baseDP: 500,

  // Presence divisor
  presenceDivisor: 20,

  // Life Points base values
  baseLP: 25,
  lpPerCon: 10,

  // Weapon quality multipliers
  weaponQualityMultiplier: 2,
  weaponPresenceMultiplier: 10,

  // Aura extension effects
  auraExtensionDivisor: 2,

  // Initiative calculations
  aapDivisor: 20,

  // Critical roll minimum
  criticalMin: 12,

  // Combat roll base
  combatRollBase: 1,
  combatRollFumble: 1,

  // Dice types
  characteristicDie: '1d10',
  combatDie: '1d100',
  breakageDie: '1d10',

  // Weapon complexity penalties
  weaponComplexityPenalty: 2,

  // Shield values (examples)
  shieldValues: {
    small: 20,
    medium: 30,
    large: 40,
    tower: 50
  },

  // Armor penalties
  armorPenalties: {
    light: 0,
    medium: 10,
    heavy: 20,
    fullPlate: 30
  },

  // Movement penalties
  movementPenalties: {
    lightArmor: 0,
    mediumArmor: 5,
    heavyArmor: 10,
    fullPlate: 15
  },

  // Critical hit ranges
  criticalRanges: {
    normal: 90,
    good: 85,
    excellent: 80,
    magnificent: 75
  },

  // Fumble ranges
  fumbleRanges: {
    normal: 10,
    poor: 15,
    terrible: 20
  },

  // Open roll threshold
  openRollThreshold: 90,

  // Fumble threshold
  fumbleThreshold: 10,

  // Summoning constants
  summoningDifficultyMultiplier: 10,

  // Ki technique costs
  kiTechniqueCostBase: 20,

  // Mental pattern constants
  mentalPatternBaseCost: 0,

  // Innate magic constants
  innateMagicBaseLevel: 0,

  // Spell constants
  spellLevelMax: 100,
  spellSystemMax: 100,

  // Metamagic constants
  metamagicMaxLevel: 100,

  // Psychic discipline constants
  psychicDisciplineMaxLevel: 100,

  // Class level constants
  maxCharacterLevel: 100,

  // Special ability multipliers
  specialAbilityMultiplier: 1,

  // Regeneration constants
  regenerationConstants: {
    magicSuperiorMultiplier: 1,
    kiHealingBase: 0,
    dailyRegenerationBase: 0
  },

  // Advantage/Disadvantage constants
  advantageConstants: {
    baseCost: 0,
    maxAdvantages: 4,
    disadvantageBenefit: 0
  },



  // Superior magic constants
  superiorMagicConstants: {
    accumulationMultiplier: 1,
    levelMultiplier: 1,
    powMultiplier: 1
  },

  // Equipment weight constants (based on strength)
  equipmentWeightConstants: {
    carryLightMultiplier: 5,
    carryMediumMultiplier: 10,
    carryHeavyMultiplier: 15,
    carryMaxMultiplier: 20,
    liftLightMultiplier: 10,
    liftMediumMultiplier: 20,
    liftHeavyMultiplier: 30,
    encumbranceLight: 0,
    encumbranceMedium: 5,
    encumbranceHeavy: 10,
    encumbranceMax: 15
  },

  // Combat table constants
  combatTableConstants: {
    superiorCriticalThreshold: 95,
    superiorCriticalMultiplier: 2,
    absoluteCriticalThreshold: 100,
    absoluteCriticalMultiplier: 3,
    openRollMultiplier: 1
  },

  // Resting constants
  restingConstants: {
    restingValue: 0,
    notRestingValue: 0,
    dailyRegenerationMultiplier: 1
  },

  // Circumstantial modifier constants
  circumstantialConstants: {
    fatiguePenaltyPerLevel: 15,
    maxCircumstantialModifier: 50,
    minCircumstantialModifier: -50
  },

  // Game modifier constants
  gameModifierConstants: {
    flankingBonus: 10,
    surpriseBonus: 20,
    rangePenaltyPerIncrement: 10,
    coverBonus: {
      half: 20,
      threeQuarters: 30,
      nineTenths: 40,
      total: 50
    },
    pronePenalty: 20
  },

  // Status effect constants
  statusEffectConstants: {
    blindedPenalty: 50,
    deafenedPenalty: 20,
    stunnedPenalty: 100,
    unconsciousPenalty: 1000,
    pronePenalty: 20,
    grappledPenalty: 30,
    silencedPenalty: 100,
    confusionPenalty: 20,
    charmPenalty: 0,
    fearPenalty: 30,
    poisonedPenalty: 10,
    diseasedPenalty: 5,
    bleedingPenalty: 5,
    fatiguedPenalty: 10,
    exhaustedPenalty: 20
  },

  // Time and action constants
  timeActionConstants: {
    combatRoundSeconds: 6,
    freeActionTime: 0,
    swiftActionTime: 1,
    standardActionTime: 1,
    fullRoundActionTime: 1,
    reactionTime: 1,
    baseMovementSpeed: 10,
    runMovementMultiplier: 3,
    chargeMovementMultiplier: 2,
    withdrawMovementPenalty: 0.5
  }
};

/**
 * Legacy support - keeping old abilities for backward compatibility
 */
ANIMA.abilities = ANIMA.characteristics;
ANIMA.abilityAbbreviations = ANIMA.characteristicAbbreviations;
