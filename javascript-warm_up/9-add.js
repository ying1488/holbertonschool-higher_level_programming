#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);


if (!Number.isInteger(num1) || !Number.isInteger(num2)) {
  console.log('NaN');
} else {
    let sum = num1 + num2;
    console.log(sum)
}
