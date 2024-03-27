#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, data) {
  if (error) {
    console.error(error);
  } else {
    for (const film in JSON.parse(data).results) {
      for (const acteur in JSON.parse(data).results[film].characters) {
        if (JSON.parse(data).results[film].characters[acteur].includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
