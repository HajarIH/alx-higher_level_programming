#!/usr/bin/node
exports.esrever = function (list) {
  let r;
  const l = (list.length - 1) * 0.5;
  for (let i = 0; i < l; i++) {
    r = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = r;
  }
  return list;
};
