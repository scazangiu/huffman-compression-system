# Huffman Compression System

Python implementation of Huffman encoding and decoding using custom min-heap and binary tree data structures.

## Features

- Counts character frequencies from input text
- Builds a custom functional min-heap without modifying the original heap
- Constructs a Huffman tree by repeatedly combining the lowest-frequency nodes
- Recursively generates binary codes for each character
- Encodes text into a binary representation using Huffman codes
- Decodes binary strings back into the original text
- Includes unit tests for heap operations and encoding/decoding behavior

## Technologies Used

- Python
- Dataclasses
- Min-Heaps
- Binary Trees
- Recursion
- Dictionaries
- Unit Testing

## Example Functionality

The program can:

- Analyze character frequency within a string
- Create a priority queue from frequency data
- Build a Huffman encoding tree
- Generate variable-length binary codes for characters
- Encode strings using generated Huffman codes
- Decode encoded data back into its original form
- Verify encoding and decoding across different test cases

## What I Learned

- Implementing a min-heap and binary tree from scratch
- Using recursion to traverse tree-based data structures
- Applying data structures to a real compression algorithm
- Working with immutable data and functional programming concepts
- Designing encoding and decoding logic
- Writing unit tests for algorithms and edge cases

## Attribution

The `Node` and `MinHeap` data structures were provided as starter code for the course project. I implemented the heap operations, Huffman tree construction, frequency analysis, code generation, encoding, decoding, and unit tests.
