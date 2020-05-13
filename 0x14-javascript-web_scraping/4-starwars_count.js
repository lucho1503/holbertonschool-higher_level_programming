#!/usr/bin/node

const request = require('request');
const match = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/people/18/';

let count = 0;

request.get(match, function (err, resp, body) {
  if (err) {
    console.log(err);
  }

  const res = JSON.parse(body);
  for (let i in res.results) {
    if (res.results[i].characters.includes(url)) {
      count++;
    }
  }
  console.log(count);
});
