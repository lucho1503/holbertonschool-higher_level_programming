#!/usr/bin/node

const n = parseInt(process.argv[2], 10);

if (isNaN(n)) {
  console.log('Not a nomber');
} else {
  console.log(`My number: ${n}`);
}
