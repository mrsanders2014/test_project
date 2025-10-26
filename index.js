/**
 * Playground Project - A simple project to try things out
 */

// A simple greeting function
function greet(name = 'World') {
  return `Hello, ${name}!`;
}

// A simple calculator with basic operations
const calculator = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => {
    if (b === 0) {
      throw new Error('Cannot divide by zero');
    }
    return a / b;
  }
};

// A function to check if a number is even
function isEven(num) {
  return num % 2 === 0;
}

// Export functions for testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    greet,
    calculator,
    isEven
  };
}

// Run some examples when executed directly
if (require.main === module) {
  console.log('🎮 Welcome to the Playground Project!\n');
  
  console.log(greet());
  console.log(greet('Developer'));
  
  console.log('\n📊 Calculator Examples:');
  console.log(`5 + 3 = ${calculator.add(5, 3)}`);
  console.log(`10 - 4 = ${calculator.subtract(10, 4)}`);
  console.log(`6 * 7 = ${calculator.multiply(6, 7)}`);
  console.log(`20 / 5 = ${calculator.divide(20, 5)}`);
  
  console.log('\n🔢 Even Number Check:');
  console.log(`Is 4 even? ${isEven(4)}`);
  console.log(`Is 7 even? ${isEven(7)}`);
  
  console.log('\n✨ Feel free to modify this code and experiment!');
}
