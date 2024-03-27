#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, data) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(`${filePath}`, `${data}`, (error) => {
    if (error) {
      console.log(error);
    }
  });
});
