#!/usr/bin/node

const x = process.argv[2];
if (process.argv.length === 2 || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let line = '';

    for (let j = 0; j < x; j++) {
      line += 'X';
    }

    console.log(line);
  }
}