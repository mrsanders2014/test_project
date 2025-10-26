/**
 * Simple test suite for the playground project
 */

const { greet, calculator, isEven } = require('./index.js');

// Simple test helper
function assert(condition, message) {
  if (!condition) {
    throw new Error(`❌ Test failed: ${message}`);
  }
  console.log(`✅ ${message}`);
}

function assertThrows(fn, message) {
  try {
    fn();
    throw new Error(`❌ Test failed: ${message} - Expected an error to be thrown`);
  } catch (error) {
    if (error.message.includes('Test failed')) {
      throw error;
    }
    console.log(`✅ ${message}`);
  }
}

console.log('🧪 Running tests...\n');

// Test greet function
console.log('Testing greet function:');
assert(greet() === 'Hello, World!', 'greet() returns default greeting');
assert(greet('Alice') === 'Hello, Alice!', 'greet("Alice") returns personalized greeting');

// Test calculator
console.log('\nTesting calculator:');
assert(calculator.add(2, 3) === 5, 'calculator.add(2, 3) equals 5');
assert(calculator.subtract(10, 4) === 6, 'calculator.subtract(10, 4) equals 6');
assert(calculator.multiply(3, 4) === 12, 'calculator.multiply(3, 4) equals 12');
assert(calculator.divide(15, 3) === 5, 'calculator.divide(15, 3) equals 5');
assertThrows(() => calculator.divide(10, 0), 'calculator.divide by zero throws error');

// Test isEven function
console.log('\nTesting isEven function:');
assert(isEven(4) === true, 'isEven(4) returns true');
assert(isEven(7) === false, 'isEven(7) returns false');
assert(isEven(0) === true, 'isEven(0) returns true');

console.log('\n🎉 All tests passed!');
