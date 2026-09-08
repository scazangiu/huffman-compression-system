import unittest
from huffman import *

class TestStudentHuffman(unittest.TestCase):

    # heapify_up tests
    def test_heapify_up_single(self):
        heap = MinHeap(data=[Node(freq=1, char='a')])
        result = heapify_up(heap, 0)
        self.assertEqual(len(result.data), 1)

    def test_heapify_up_swaps(self):
        heap = MinHeap(data=[Node(freq=5, char='a'), Node(freq=1, char='b')])
        result = heapify_up(heap, 1)
        self.assertEqual(result.data[0].freq, 1)

    # insert tests
    def test_insert_single(self):
        heap = MinHeap(data=[])
        result = insert(heap, Node(freq=3, char='a'))
        self.assertEqual(len(result.data), 1)

    def test_insert_maintains_order(self):
        heap = MinHeap(data=[])
        heap = insert(heap, Node(freq=5, char='a'))
        heap = insert(heap, Node(freq=2, char='b'))
        heap = insert(heap, Node(freq=8, char='c'))
        self.assertEqual(heap.data[0].freq, 2)

    # extract_min tests
    def test_extract_min_returns_smallest(self):
        heap = MinHeap(data=[])
        heap = insert(heap, Node(freq=3, char='a'))
        heap = insert(heap, Node(freq=1, char='b'))
        heap = insert(heap, Node(freq=5, char='c'))
        new_heap, min_node = extract_min(heap)
        self.assertEqual(min_node.freq, 1)

    def test_extract_min_reduces_size(self):
        heap = MinHeap(data=[])
        heap = insert(heap, Node(freq=3, char='a'))
        heap = insert(heap, Node(freq=1, char='b'))
        new_heap, _ = extract_min(heap)
        self.assertEqual(len(new_heap.data), 1)

    # edge cases
    def test_single_character(self):
        encoded, decoded, codes = huffman_encoding("a")
        self.assertEqual(decoded, "a")

    def test_repeated_characters(self):
        encoded, decoded, codes = huffman_encoding("aaaa")
        self.assertEqual(decoded, "aaaa")

    def test_two_characters(self):
        encoded, decoded, codes = huffman_encoding("ab")
        self.assertEqual(decoded, "ab")

    def test_decoded_matches_input(self):
        for s in ["hello", "aaabbc", "mississippi", "zzzz"]:
            _, decoded, _ = huffman_encoding(s)
            self.assertEqual(decoded, s)

if __name__ == "__main__":
    unittest.main()
