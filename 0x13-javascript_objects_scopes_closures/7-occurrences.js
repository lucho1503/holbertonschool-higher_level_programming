#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      res = res + 1;
    }
  }
  return (res);
};
