#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!Number.isInteger(x)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < x; i++) {
        let row = '';
        for (let j = 0; j < x; j++)
        {
            row += 'x'
        }
    console.log(row);
  }
}
