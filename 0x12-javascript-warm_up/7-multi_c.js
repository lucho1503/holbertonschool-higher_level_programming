#!/usr/bin/node

const x = process.argv[2];
if (process.argv.length === 2 || !x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = x; i > 0; i--) {
    console.log('C is fun');
  }
}
