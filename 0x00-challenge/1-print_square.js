#!/usr/local/bin/node

const size = parseInt(process.argv[2]); // Parse the size from the command line argument

// Check if the size is a valid number
if (isNaN(size) || size <= 0) {
  console.log('Missing or invalid size');
} else {
  // Loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('#'.repeat(size)); // Print a row of the square
  }
}
