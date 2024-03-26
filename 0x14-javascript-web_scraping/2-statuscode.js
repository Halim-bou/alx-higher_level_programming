#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
// funcion to request a GET
request.get(`${url}`).on('response', function (response) {
  console.log('code: ', response.statusCode);
});
