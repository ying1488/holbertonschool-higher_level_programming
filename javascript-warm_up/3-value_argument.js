#!/usr/bin/node
const arg = process.argv.slice(2);

if (!arg[0]) {
  console.log('No argument');
} else {
  console.log(arg[0]);
}
