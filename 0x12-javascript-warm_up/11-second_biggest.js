#!/usr/bin/node
const arg = process.argv.slice(2);
let secondBigg = 0;

if (arg.length > 1) {
  const integers = arg.map(Number);
  integers.sort((a, b) => b - a);
  secondBigg = integers[1];
}
console.log(secondBigg);
