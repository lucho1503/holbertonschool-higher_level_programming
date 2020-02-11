#!/usr/bin/node

let numbers = 0;
exports.logMe = function (item) {
  console.log(numbers + ': ' + item);
  numbers += 1;
};
