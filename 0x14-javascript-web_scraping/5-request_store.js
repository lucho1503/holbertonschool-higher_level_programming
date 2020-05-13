#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  }

  const result = body;
  fs.writeFile(process.argv[3], result, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
