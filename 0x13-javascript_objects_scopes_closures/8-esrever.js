#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    const tmp = list[i];
    const tmp_2 = list.length - i - 1;
    list[i] = list[tmp_2];
    list[tmp_2] = tmp;
  }
  return (list);
};
