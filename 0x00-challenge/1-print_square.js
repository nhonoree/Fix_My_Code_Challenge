#!/usr/bin/node

// This script prints a square of a given size using '#'.
if (process.argv.length !== 3) {
  console.log('Usage: ./1-print_square.js <size>');
  process.exit(1);
}

const size = parseInt(process.argv[2], 10);

// Validate that the input is a positive integer
if (isNaN(size) || size <= 0) {
  console.log('Size must be a positive integer');
  process.exit(1);
}

// Generate the square
for (let i = 0; i < size; i++) {
  console.log('#'.repeat(size));
}
