export const ANIMA = {};

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
    athleticism: { name: "Athlétisme", baseChar: "strength" },
    climb: { name: "Escalade", baseChar: "strength" },
    jump: { name: "Saut", baseChar: "strength" },
    ride: { name: "Equitation", baseChar: "agility" },
    swim: { name: "Natation", baseChar: "strength" }
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
 * Legacy support - keeping old abilities for backward compatibility
 */
ANIMA.abilities = ANIMA.characteristics;
ANIMA.abilityAbbreviations = ANIMA.characteristicAbbreviations;
