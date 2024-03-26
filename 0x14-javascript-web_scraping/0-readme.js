#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
// funcion to read the file
function readF (path) {
  fs.readFile(`${path}`, 'utf-8', (error, data) => {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
}

if (!file) {
  process.exit(1);
} else {
  readF(file);
}
