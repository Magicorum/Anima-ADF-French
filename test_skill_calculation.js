// Test script for secondary skill calculations
console.log("=== TEST DES CALCULS DE COMPÉTENCES SECONDAIRES ===\n");

// Simulation des données d'un personnage
const mockSystemData = {
  characteristics: {
    strength: { value: 8, mod: 10 }, // Force 8 = +10 selon la table Anima
    agility: { value: 6, mod: 5 },   // Agilité 6 = +5
    intelligence: { value: 12, mod: 20 } // Intelligence 12 = +20
  },
  globalBonuses: {
    physical: { value: 5 },
    mental: { value: 0 }
  },
  secondaryAbilities: {
    athletics: {
      athleticism: {
        base: 10,
        natural: 2,
        naturalbi: 1,
        class: 5,
        special: 3,
        temp: 0,
        baseChar: "strength",
        value: 0
      },
      acrobatics: {
        base: 8,
        natural: 0,
        naturalbi: 0,
        class: 3,
        special: 0,
        temp: 2,
        baseChar: "agility",
        value: 0
      }
    },
    intellectual: {
      medicine: {
        base: 5,
        natural: 1,
        naturalbi: 0,
        class: 8,
        special: 2,
        temp: 0,
        baseChar: "intelligence",
        value: 0
      }
    }
  }
};

// Fonction de calcul corrigée
function calculateSecondaryAbility(ability, charMod, globalBonus) {
  const baseValue = ability.base || 0;
  const naturalValue = ability.natural || 0;
  const naturalBiValue = ability.naturalbi || 0;
  const classValue = ability.class || 0;
  const specialValue = ability.special || 0;
  const tempValue = ability.temp || 0;

  // Formule Anima simple : Base + Class + Special + Temp + Natural + NaturalBi + Char Mod + Global Bonus
  const finalValue = baseValue + classValue + specialValue + tempValue + naturalValue + naturalBiValue + charMod + globalBonus;

  console.log(`  Base: ${baseValue}`);
  console.log(`  Classe: ${classValue}`);
  console.log(`  Spécial: ${specialValue}`);
  console.log(`  Temp: ${tempValue}`);
  console.log(`  Naturel: ${naturalValue}`);
  console.log(`  Naturel Bio: ${naturalBiValue}`);
  console.log(`  Modificateur ${ability.baseChar}: ${charMod}`);
  console.log(`  Bonus global: ${globalBonus}`);
  console.log(`  → Valeur finale: ${finalValue}`);

  return Math.max(0, finalValue);
}

console.log("ATHLÉTISME (Force):");
console.log("================");
const athleticismResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.athletics.athleticism,
  mockSystemData.characteristics.strength.mod,
  mockSystemData.globalBonuses.physical.value
);

console.log("\nACROBATIE (Agilité):");
console.log("===================");
const acrobaticsResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.athletics.acrobatics,
  mockSystemData.characteristics.agility.mod,
  mockSystemData.globalBonuses.physical.value
);

console.log("\nMÉDECINE (Intelligence):");
console.log("========================");
const medicineResult = calculateSecondaryAbility(
  mockSystemData.secondaryAbilities.intellectual.medicine,
  mockSystemData.characteristics.intelligence.mod,
  mockSystemData.globalBonuses.mental.value
);

console.log("\n=== RÉSUMÉ ===");
console.log(`Athlétisme: ${athleticismResult} (devrait être: 10+5+3+0+2+1+10+5 = 36)`);
console.log(`Acrobatie: ${acrobaticsResult} (devrait être: 8+3+0+2+0+0+5+5 = 23)`);
console.log(`Médecine: ${medicineResult} (devrait être: 5+8+2+0+1+0+20+0 = 36)`);

console.log("\n✅ Si les valeurs correspondent, le calcul fonctionne correctement !");
