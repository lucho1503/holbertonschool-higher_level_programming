#!/usr/bin/node

const n = parseInt(process.argv[2], 10);

if (parseInt(n)) {
  console.log(`My number: ${n}`);
} else {
  console.log('Not a nomber');
}
