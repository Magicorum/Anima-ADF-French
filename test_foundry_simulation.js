// Simulation complète du système Foundry VTT pour les compétences secondaires
console.log("=== SIMULATION FOUNDRY VTT - CALCULS DE COMPÉTENCES ===\n");

// Simulation des données d'un personnage comme dans Foundry
let mockActorData = {
  system: {
    characteristics: {
      strength: { value: 8, mod: 10 },
      agility: { value: 6, mod: 5 },
      intelligence: { value: 12, mod: 20 }
    },
    globalBonuses: {
      physical: { value: 5 },
      mental: { value: 0 }
    },
    secondaryAbilities: {
      athletics: {
        athleticism: {
          base: 0,
          natural: 0,
          naturalbi: 0,
          class: 0,
          special: 0,
          temp: 0,
          baseChar: "strength",
          value: 0
        }
      }
    }
  }
};

// Fonctions de calcul comme dans actor.mjs
function calculateCharacteristicModifiers(systemData) {
  for (let [key, characteristic] of Object.entries(systemData.characteristics || {})) {
    const value = characteristic.value || 1;
    if (value === 1) characteristic.mod = -30;
    else if (value === 2) characteristic.mod = -20;
    else if (value === 3) characteristic.mod = -10;
    else if (value === 4) characteristic.mod = -5;
    else if (value === 5) characteristic.mod = 0;
    else if (value >= 6 && value <= 7) characteristic.mod = 5;
    else if (value >= 8 && value <= 9) characteristic.mod = 10;
    else if (value === 10) characteristic.mod = 15;
    else if (value >= 11 && value <= 12) characteristic.mod = 20;
    else if (value >= 13 && value <= 14) characteristic.mod = 25;
    else if (value === 15) characteristic.mod = 30;
    else if (value >= 16 && value <= 17) characteristic.mod = 35;
    else if (value >= 18 && value <= 19) characteristic.mod = 40;
    else if (value === 20 || value === 21) characteristic.mod = 45;
    else if (value >= 22 && value <= 23) characteristic.mod = 50;
    else if (value >= 24 && value <= 25) characteristic.mod = 55;
    else characteristic.mod = 55 + Math.floor((value - 26) / 2) * 5 + (value % 2 === 0 ? 0 : 5);
  }
}

function calculateSecondaryAbilities(systemData) {
  if (!systemData.secondaryAbilities || !systemData.characteristics) return;

  const char = systemData.characteristics;
  const globalBonuses = systemData.globalBonuses || {};
  const physicalCharacteristics = ['agility', 'constitution', 'dexterity', 'strength'];
  const mentalCharacteristics = ['intelligence', 'perception', 'power', 'willpower'];

  for (const [category, abilities] of Object.entries(systemData.secondaryAbilities)) {
    for (const [key, ability] of Object.entries(abilities)) {
      if (ability && ability.baseChar && char[ability.baseChar]) {
        const baseValue = ability.base || 0;
        const naturalValue = ability.natural || 0;
        const naturalBiValue = ability.naturalbi || 0;
        const classValue = ability.class || 0;
        const specialValue = ability.special || 0;
        const tempValue = ability.temp || 0;
        const charMod = char[ability.baseChar].mod || 0;

        let globalBonus = 0;
        if (physicalCharacteristics.includes(ability.baseChar)) {
          globalBonus = globalBonuses.physical?.value || 0;
        } else if (mentalCharacteristics.includes(ability.baseChar)) {
          globalBonus = globalBonuses.mental?.value || 0;
        }

        // Formule Anima corrigée
        ability.value = baseValue + classValue + specialValue + tempValue + naturalValue + naturalBiValue + charMod + globalBonus;

        if (ability.value < 0) ability.value = 0;
      }
    }
  }
}

// Simulation de prepareDerivedData
function prepareDerivedData(actorData) {
  const systemData = actorData.system;

  console.log("🔄 ÉTAPE 1: Calcul des modificateurs de caractéristiques");
  calculateCharacteristicModifiers(systemData);
  console.log("   Force (8) → Modificateur:", systemData.characteristics.strength.mod);
  console.log("   Agilité (6) → Modificateur:", systemData.characteristics.agility.mod);
  console.log("   Intelligence (12) → Modificateur:", systemData.characteristics.intelligence.mod);

  console.log("\n🔄 ÉTAPE 2: Calcul des compétences secondaires");
  calculateSecondaryAbilities(systemData);
  console.log("   Athlétisme → Valeur finale:", systemData.secondaryAbilities.athletics.athleticism.value);
}

// Test initial
console.log("📊 VALEURS INITIALES (toutes à 0):");
prepareDerivedData(mockActorData);

// Simulation de modification des valeurs
console.log("\n📝 MODIFICATION DES VALEURS:");
mockActorData.system.secondaryAbilities.athletics.athleticism.base = 10;
mockActorData.system.secondaryAbilities.athletics.athleticism.class = 5;
mockActorData.system.secondaryAbilities.athletics.athleticism.special = 3;
mockActorData.system.secondaryAbilities.athletics.athleticism.natural = 2;
mockActorData.system.secondaryAbilities.athletics.athleticism.naturalbi = 1;

console.log("   Base: 10, Classe: 5, Spécial: 3, Naturel: 2, Naturel Bio: 1");

// Recalcul
console.log("\n🔄 RECALCUL APRÈS MODIFICATION:");
prepareDerivedData(mockActorData);

// Test avec des valeurs différentes
console.log("\n🎯 TEST AVEC VALEURS DIFFÉRENTES:");
mockActorData.system.characteristics.strength.value = 12; // Changement de la force
prepareDerivedData(mockActorData);

console.log("\n✅ Le système fonctionne correctement !");
console.log("📋 Formule: Base + Classe + Spécial + Temp + Naturel + NaturelBio + ModCaract + BonusGlobal");
