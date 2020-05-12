#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    const tmp = list[i];
    const aux = list.length - i - 1;
    list[i] = list[aux];
    list[aux] = tmp;
  }
  return (list);
};
