#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];
// funcion to read the file
function readF (path) {
  fs.writeFile(`./${path}`, `${text}`, (error, data) => {
    if (error) {
      console.log(error);
    }
  });
}

readF(file);
