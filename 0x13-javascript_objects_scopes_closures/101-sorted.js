#!/usr/bin/node
const dict = require('./101-data.js').dict;

const list = Object.entries(dict);
const val = Object.values(dict);
const unq_val = [...new Set(val)];
const newDict = {};
for (let j in unq_val) {
  const l = [];
  for (let k in list) {
    if (list[k][1] === unq_val[j]) {
      l.unshift(list[k][0]);
    }
  }
  newDict[unq_val[j]] = l;
}
console.log(newDict);
