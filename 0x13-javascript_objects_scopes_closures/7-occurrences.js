#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const reduced = function (count, value) {
    count += (value === searchElement) ? 1 : 0;
    return count;
  };
  return list.reduce(reduced, 0);
};
