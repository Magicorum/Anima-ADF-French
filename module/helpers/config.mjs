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
    acrobatics: { name: "Acrobaties", baseChar: "agility" },
    athletics: { name: "Athlétisme", baseChar: "strength" },
    climb: { name: "Escalade", baseChar: "strength" },
    jump: { name: "Saut", baseChar: "strength" },
    ride: { name: "Équitation", baseChar: "agility" },
    swim: { name: "Natation", baseChar: "strength" }
  },
  social: {
    style: { name: "Style", baseChar: "dexterity" },
    intimidate: { name: "Intimidation", baseChar: "strength" },
    leadership: { name: "Commandement", baseChar: "power" },
    persuasion: { name: "Persuasion", baseChar: "intelligence" },
    trading: { name: "Commerce", baseChar: "intelligence" },
    etiquette: { name: "Étiquette", baseChar: "intelligence" }
  },
  perceptive: {
    notice: { name: "Perception", baseChar: "perception" },
    search: { name: "Fouille", baseChar: "perception" },
    track: { name: "Pistage", baseChar: "perception" }
  },
  intellectual: {
    animals: { name: "Animaux", baseChar: "intelligence" },
    science: { name: "Science", baseChar: "intelligence" },
    law: { name: "Droit", baseChar: "intelligence" },
    herbs: { name: "Herboristerie", baseChar: "intelligence" },
    history: { name: "Histoire", baseChar: "intelligence" },
    tactics: { name: "Tactique", baseChar: "intelligence" },
    arcane: { name: "Arcanes", baseChar: "intelligence" }
  },
  other: {
    sleightOfHand: { name: "Escamotage", baseChar: "dexterity" },
    disguise: { name: "Déguisement", baseChar: "dexterity" },
    hide: { name: "Dissimulation", baseChar: "perception" },
    theft: { name: "Vol", baseChar: "dexterity" },
    trapLore: { name: "Connaissance des Pièges", baseChar: "perception" },
    poisons: { name: "Poisons", baseChar: "intelligence" },
    lockpicking: { name: "Crochetage", baseChar: "dexterity" }
  }
};

/**
 * Legacy support - keeping old abilities for backward compatibility
 */
ANIMA.abilities = ANIMA.characteristics;
ANIMA.abilityAbbreviations = ANIMA.characteristicAbbreviations;
