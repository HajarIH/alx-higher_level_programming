#!/usr/bin/node

if (process.argv[2] === undefined || process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2).map(Number);
  const max2 = array.sort(function (a, b) { return b - a; })[1];
  console.log(max2);
}
