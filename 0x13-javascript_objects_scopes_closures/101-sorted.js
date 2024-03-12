#!/usr/bin/node
const dict = require('./101-data.js').dict;

const list = Object.entries(dict);
const val = Object.values(dict);
const unqval = [...new Set(val)];
const newDict = {};
for (const j in unqval) {
  const l = [];
  for (const k in list) {
    if (list[k][1] === unqval[j]) {
      l.unshift(list[k][0]);
    }
  }
  newDict[unqval[j]] = l;
}
console.log(newDict);
