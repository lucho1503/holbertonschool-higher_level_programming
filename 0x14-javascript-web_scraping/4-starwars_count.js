#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const match = 'https://swapi.co/api/people/18/';
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const res = JSON.parse(body);

  for (const i in res.results) {
    if (res.results[i].characters.includes(match)) {
      count++;
    }
  }

  console.log(count);
});
