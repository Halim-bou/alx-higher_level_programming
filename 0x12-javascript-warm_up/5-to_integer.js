#!/usr/bin/node

const ar = process.argv[2];
const convertNum = parseInt(ar);
console.log(isNaN(convertNum) ? 'Not a number' : 'My number: ' + convertNum);
