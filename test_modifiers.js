// Test script for Anima modifier calculations
function calculateModifier(value) {
  if (value === 1) return -30;
  else if (value === 2) return -20;
  else if (value === 3) return -10;
  else if (value === 4) return -5;
  else if (value === 5) return 0;
  else if (value >= 6 && value <= 7) return 5;
  else if (value >= 8 && value <= 9) return 10;
  else if (value === 10) return 15;
  else if (value >= 11 && value <= 12) return 20;
  else if (value >= 13 && value <= 14) return 25;
  else if (value === 15) return 30;
  else if (value >= 16 && value <= 17) return 35;
  else if (value >= 18 && value <= 19) return 40;
  else if (value === 20 || value === 21) return 45;
  else if (value >= 22 && value <= 23) return 50;
  else if (value >= 24 && value <= 25) return 55;
  else return 55 + Math.floor((value - 26) / 2) * 5 + (value % 2 === 0 ? 0 : 5);
}

console.log("=== TABLE DE CONVERSION DES MODIFICATEURS ANIMA ===");
console.log("Caractéristique | Modificateur");
console.log("---------------|-------------");

for (let i = 1; i <= 25; i++) {
  const mod = calculateModifier(i);
  const sign = mod >= 0 ? "+" : "";
  console.log(`${i.toString().padStart(14)} | ${sign}${mod}`);
}

console.log("\n=== TESTS SPÉCIAUX ===");
console.log("DEX 1 = -30:", calculateModifier(1) === -30);
console.log("DEX 5 = 0:", calculateModifier(5) === 0);
console.log("DEX 10 = +15:", calculateModifier(10) === 15);
console.log("DEX 15 = +30:", calculateModifier(15) === 30);
console.log("DEX 20 = +45:", calculateModifier(20) === 45);
console.log("DEX 21 = +45:", calculateModifier(21) === 45);
console.log("DEX 22 = +50:", calculateModifier(22) === 50);
console.log("DEX 24 = +55:", calculateModifier(24) === 55);
