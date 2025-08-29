// Test script for global bonuses system
console.log("=== SYSTÈME DE BONUS GLOBAUX ANIMA ===\n");

// Simulation des données d'un personnage
const mockSystemData = {
  characteristics: {
    agility: { mod: 10 },
    constitution: { mod: 5 },
    dexterity: { mod: 15 },
    strength: { mod: 0 },
    intelligence: { mod: 20 },
    perception: { mod: 10 },
    power: { mod: 15 },
    willpower: { mod: 5 }
  },
  globalBonuses: {
    physical: { value: 5 },
    mental: { value: 8 }
  },
  secondaryAbilities: {
    athletics: {
      acrobatics: { base: 10, natural: 0, naturalbi: 0, class: 5, special: 0, temp: 0, baseChar: "agility" },
      athleticism: { base: 15, natural: 0, naturalbi: 0, class: 0, special: 0, temp: 0, baseChar: "strength" }
    },
    intellectual: {
      animals: { base: 5, natural: 0, naturalbi: 0, class: 10, special: 0, temp: 0, baseChar: "intelligence" },
      appraisal: { base: 8, natural: 0, naturalbi: 0, class: 3, special: 0, temp: 0, baseChar: "intelligence" }
    }
  }
};

// Fonction de calcul simplifiée pour test
function calculateSecondaryAbility(ability, charMod, globalBonus) {
  const baseValue = ability.base || 0;
  const naturalValue = ability.natural || 0;
  const naturalBiValue = ability.naturalbi || 0;
  const classValue = ability.class || 0;
  const specialValue = ability.special || 0;
  const tempValue = ability.temp || 0;

  // Formule simplifiée pour test
  const bonNat = naturalValue + naturalBiValue;
  const compNat = baseValue;
  const naturalBonus = (((bonNat + 1) * charMod + compNat + 100) - Math.abs((bonNat + 1) * charMod + compNat - 100)) / 2;

  return Math.max(0, naturalBonus + classValue + specialValue + tempValue + globalBonus);
}

console.log("COMPÉTENCES AVEC BONUS PHYSIQUE (+5) :");
console.log("========================================");

// Compétences physiques
const acrobaticsResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.athletics.acrobatics,
  mockSystemData.characteristics.agility.mod,
  mockSystemData.globalBonuses.physical.value
);

const athleticismResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.athletics.athleticism,
  mockSystemData.characteristics.strength.mod,
  mockSystemData.globalBonuses.physical.value
);

console.log(`Acrobatie (AGI: +10) : ${acrobaticsResult}`);
console.log(`Athlétisme (FOR: +0) : ${athleticismResult}`);

console.log("\nCOMPÉTENCES AVEC BONUS MENTAL (+8) :");
console.log("====================================");

// Compétences mentales
const animalsResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.intellectual.animals,
  mockSystemData.characteristics.intelligence.mod,
  mockSystemData.globalBonuses.mental.value
);

const appraisalResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.intellectual.appraisal,
  mockSystemData.characteristics.intelligence.mod,
  mockSystemData.globalBonuses.mental.value
);

console.log(`Animaux (INT: +20) : ${animalsResult}`);
console.log(`Estimation (INT: +20) : ${appraisalResult}`);

console.log("\n=== RÉSUMÉ ===");
console.log(`Bonus Physique appliqué à : AGI, CON, DEX, FOR`);
console.log(`Bonus Mental appliqué à : INT, PER, POU, VOL`);
console.log(`\nToutes les compétences de leur catégorie respective reçoivent automatiquement le bonus approprié !`);
