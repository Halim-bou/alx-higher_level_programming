#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    for (const character of JSON.parse(data).characters) {
      request(character, (error, response, data) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(data).name);
        }
      });
    }
  }
});
