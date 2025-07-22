#!/usr/bin/node
const str = 'C is fun';
const x = parseInt(process.argv[2]);

if (!Number.isInteger(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
