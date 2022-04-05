#!/usr/bin/node
// script that computes and prints a factorial
const argv = parseInt(process.argv[2]);
function factorial (number) {
  if ((Number.isNaN(number)) || (number === 1)) {
    return 1;
  }
  return factorial(number - 1) * number;
}
console.log(factorial(argv));
