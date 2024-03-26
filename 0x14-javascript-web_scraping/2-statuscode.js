#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
// funcion to request a GET
function requestGet (link) {
  request(`${link}`, function (response) {
    console.log('code: ', response.statusCode);
  });
}
requestGet(url);
