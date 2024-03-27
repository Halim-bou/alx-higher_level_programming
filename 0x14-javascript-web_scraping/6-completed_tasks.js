#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    const users = {};
    for (const user in JSON.parse(data)) {
      if (JSON.parse(data)[user].completed) {
        users[JSON.parse(data)[user].userId] = (users[JSON.parse(data)[user].userId] || 0) + 1;
      }
    }
    console.log(users);
  }
});
