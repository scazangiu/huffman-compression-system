from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

# Takes a MinHeap and an index, bubbles the element at that index
# up until the min-heap property is restored. Returns a new MinHeap.
def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    
    if index == 0:
        return MinHeap(data = new_data)
    
    parent = (index - 1) // 2
    
    if new_data[index] < new_data[parent]:
        temp = new_data[index]
        new_data[index] = new_data[parent]
        new_data[parent] = temp
        return heapify_up(MinHeap(data = new_data), parent)
        
    return MinHeap(data = new_data)

# Takes a MinHeap and a Node, appends the Node to the end
# and restores heap order via heapify_up. Returns a new MinHeap.
def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_data = heap.data + [element]
    new_heap = heapify_up(MinHeap(data = new_data), len(new_data) - 1)
    return new_heap

# Takes a MinHeap and an index, pushes the element at that index
# down until the min-heap property is restored. Returns a new MinHeap.
def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_data)
    
    if left >= size:
        return MinHeap(data = new_data)
        
    smallest = left
    
    if right < size and new_data[right] < new_data[left]:
        smallest = right
        
    if new_data[smallest] < new_data[index]:
        temp = new_data[index]
        new_data[index] = new_data[smallest]
        new_data[smallest] = temp
        return heapify_down(MinHeap(data = new_data), smallest)
        
    return MinHeap(data = new_data)

# Removes and returns the smallest Node from the heap.
# Replaces root with last element and restores order via heapify_down.
# Returns a tuple of (new MinHeap, min Node).
def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if len(heap.data) == 1:
        return MinHeap(data=[]), heap.data[0]
    min_element = heap.data[0]
    last_element = heap.data[-1]
    new_data = [last_element] + heap.data[1: -1]
    new_heap = heapify_down(MinHeap(data = new_data), 0)
    return new_heap, min_element

# Takes a string and returns a dictionary mapping
# each character to the number of times it appears.
def count_frequency(s: str)-> dict[str,int]:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else: 
            freq[char] = 1
    return freq

# Takes a frequency dictionary and builds a MinHeap
# by inserting each character as a Node with its frequency.
def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    new_heap = MinHeap(data = [])
    for char, freq in frequency.items():
        new_heap = insert(new_heap, Node(freq = freq, char = char))
    return new_heap

# Repeatedly extracts the two smallest nodes, combines them into
# a parent node, and reinserts until one root node remains.
def build_tree_from_queue(priority_queue: MinHeap) -> Node:
    while len(priority_queue.data) > 1:
        new_heap, left_node = extract_min(priority_queue)
        new_heap, right_node = extract_min(new_heap)
        new_freq = left_node.freq + right_node.freq
        new_char = left_node.char + right_node.char
        parent = Node(freq = new_freq, char = new_char, left = left_node, right = right_node)
        priority_queue = insert(new_heap, parent)
    return priority_queue.data[0]

# Recursively traverses the Huffman tree, assigning binary codes
# to each character. Left adds "0", right adds "1" to the prefix.
def generate_codes(node: Node | None, prefix="", code: dict | None = None)-> dict:
    if code is None:
        code = {}
    if node is None:
        return code
    if node.left is None and node.right is None:
        if prefix == "":
            code[node.char] = "0"
        else:
            code[node.char] = prefix
        return code
    left =  generate_codes(node.left, prefix + "0", code)
    right = generate_codes(node.right, prefix + "1", code)
    return code

# Replaces each character in the string with its
# corresponding binary code from the codes dictionary.
def encode(s: str, codes: dict)-> str:
    result = ""
    for char in s:
        result += codes[char]
    return result

# Traverses the Huffman tree bit by bit, adding a character
# to the result each time a leaf node is reached, then resets to root.
def decode(encoded_string: str, root: Node) -> str:
    result = ""
    current = root
    for i in encoded_string:
        if current.left is None and current.right is None:
            result += current.char
            current = root
            continue
        if i == "0":
            current = current.left
            if current.left is None and current.right is None:
                result += current.char
                current = root
        if i == "1":
            current = current.right
            if current.left is None and current.right is None:
                result += current.char
                current = root
    return result
    
def huffman_encoding(s:str):
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes
