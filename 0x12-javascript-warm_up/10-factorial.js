#!/usr/bin/node
/**
 * factorial - Computes the factorial of a number.
 * @param {Number} num - The number.
 *
 * @returns The factorial of the number.
 */
function factorial (num) {
  if (Number.isNaN(num) || (num <= 0)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number.parseInt(process.argv[2])));
