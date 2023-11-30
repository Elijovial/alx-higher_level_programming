#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const argv = process.argv.slice(2);
  const intArgv = argv.sort((a, b) => a - b);
  console.log(intArgv[intArgv.length - 2]);
}
