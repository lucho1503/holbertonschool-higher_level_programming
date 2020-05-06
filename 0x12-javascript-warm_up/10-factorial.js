#!/usr/bin/node

const fac = function factrec (n) {
  if (n < 2) {
    return 1;
  }
  return n * factrec(n - 1);
};

if (process.argv[2]) {
  const f = parseInt(process.argv[2]);
  console.log(fac(f));
} else {
  console.log(fac(1));
}
