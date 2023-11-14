#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (arg1, arg2) {
  if (isNaN(arg1) || isNaN(arg2)) {
    return (NaN);
  } else {
    return (parseInt(arg1) + parseInt(arg2));
  }
}
console.log(add(arg1, arg2));
