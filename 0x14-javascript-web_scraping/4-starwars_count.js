#!/usr/bin/node

const request = require('request');

const url = 'http://swapi.co/api/films/';
let count = 0;

request(url, function (err, response, body) {
  const res = (JSON.parse(body).results);

  if (err) {
    console.log(err);
  }
  for (let i = 0; i < res.length; i++) {
    const ch = res[i].characters;

    for (let j = 0; j < ch.length; j++) {
      if (ch[j].includes('/18/')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
