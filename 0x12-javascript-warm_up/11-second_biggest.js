#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const secondBiggest = process.argv;
if (secondBiggest.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest.sort((x, y) => y - x).slice(3)[0]);
}
