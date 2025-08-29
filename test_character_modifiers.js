// Test des modificateurs de caractéristiques Anima
console.log("=== TEST DES MODIFICATEURS DE CARACTÉRISTIQUES ANIMA ===\n");

// Fonction de calcul des modificateurs (copiée du code principal)
function calculateCharacteristicModifiers(characteristics) {
  console.log("🔄 Calcul des modificateurs:");

  for (let [key, characteristic] of Object.entries(characteristics)) {
    // Calculate the final value from base + special + temp
    const value = (characteristic.base || 1) + (characteristic.special || 0) + (characteristic.temp || 0);
    const oldMod = characteristic.mod;

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

    // Update the final value
    characteristic.final = value;

    console.log(`   ${key}: valeur=${value} (base=${characteristic.base} + spécial=${characteristic.special} + temp=${characteristic.temp}), mod=${characteristic.mod}`);
  }
  console.log("✅ Fin calcul modificateurs");
}

// Test avec différentes valeurs
const testCharacteristics = {
  strength: { base: 5, special: 0, temp: 0 },
  agility: { base: 8, special: 2, temp: 1 },
  intelligence: { base: 12, special: 3, temp: 0 },
  power: { base: 15, special: 0, temp: 2 }
};

console.log("VALEURS DE TEST:");
console.log("=================");
calculateCharacteristicModifiers(testCharacteristics);

console.log("\nVÉRIFICATION DE LA TABLE ANIMA:");
console.log("===============================");
const testValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25];

testValues.forEach(val => {
  const char = { base: val, special: 0, temp: 0 };
  calculateCharacteristicModifiers({ test: char });
  console.log(`Valeur ${val}: modificateur ${char.mod}`);
});

console.log("\n✅ Test terminé - les modificateurs devraient maintenant fonctionner correctement !");
