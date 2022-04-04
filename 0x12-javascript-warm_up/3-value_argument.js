#!/usr/bin/node
// script that prints the first argument passed to it
const argvFirst = process.argv[2];
if (argvFirst === undefined) {
  console.log('No argument');
} else {
  console.log(argvFirst);
}
