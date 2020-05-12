#!/usr/bin/node

exports.converter = function (base) {
  return function (b) {
    return b.toString(base);
  };
};
