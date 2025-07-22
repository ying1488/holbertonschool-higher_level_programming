#!/usr/bin/node
const str = 'C is fun\n';
const x = parseInt(process.argv[2]);

if (!Number.isInteger(x)){
  console.log('Missing number of occurrences');
} else {
  console.log(str.repeat(x));
}