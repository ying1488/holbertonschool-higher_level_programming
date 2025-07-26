#!/usr/bin/node

const arg1 = process.argv.slice(2).map(Number);

function getSecondLargest(array) {
  const n = array.length;
  // sort array in accending order
  array.sort((a, b)=> a - b);
  // from second last element as the last is the largest
  for (let i = n - 2; i >= 0; i--) {
  //return the the second largest element
    if (array[i] !== array[n - 1]) {
      return array[i];
    }
  }
  return 0;
}
console.log(getSecondLargest(arg1));
