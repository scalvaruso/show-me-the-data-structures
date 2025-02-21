# Problem 3

## Reasoning Behind Decisions

The Huffman coding implementation consists of several key steps, ensuring an optimal prefix encoding scheme for lossless data compression:

1. **Frequency Calculation**:
   - A dictionary is used to count character occurrences, allowing efficient frequency computation in **O(N)** time.

2. **Priority Queue (Min-Heap) for Tree Construction**:
   - A min-heap (`heapq`) is used to efficiently extract the two least frequent nodes, ensuring the Huffman tree is built optimally.
   - This results in a time complexity of **O(K log K)**, where `K` is the number of unique characters.

3. **Huffman Tree Construction**:
   - Nodes are merged iteratively until a single root remains, guaranteeing an optimal prefix-free encoding.
   - Internal nodes store summed frequencies but no actual characters.

4. **Code Generation via Tree Traversal**:
   - A recursive depth-first traversal assigns binary codes to characters, ensuring no prefix conflicts.
   - If only one unique character exists, it is assigned `"0"`, preventing empty encodings.

5. **Encoding Process**:
   - The input string is converted using the generated Huffman codes in **O(N)** time.

6. **Decoding Process**:
   - The encoded string is traversed bit-by-bit using the Huffman tree, reconstructing the original text.
   - The traversal ensures that every encoded character maps to a unique path in **O(N)** time.

These choices guarantee an efficient and correct Huffman coding implementation.

## Time Efficiency

The overall time complexity of Huffman encoding and decoding is:

1. **Encoding Process**:
   - Frequency calculation: **O(N)**
   - Huffman tree construction: **O(K log K)**
   - Code generation via DFS: **O(K)**
   - Encoding the string: **O(N)**
   - **Total:** **O(N + K log K)**

2. **Decoding Process**:
   - Traversing the encoded bits using the Huffman tree: **O(N)**
   - **Total:** **O(N)**

Since `K` (the number of unique characters) is typically much smaller than `N`, the dominant term is **O(N log K)**, making Huffman coding highly efficient for text compression.

## Space Efficiency

The space complexity is **O(K + N)**:

1. **Storage for Frequency Dictionary & Huffman Codes**:
   - Both require **O(K)** space.

2. **Huffman Tree Storage**:
   - Uses **O(K)** space for tree nodes.

3. **Encoded String Storage**:
   - Requires **O(N)** space.

Thus, the implementation is both **memory-efficient** and **computationally optimal** for real-world text compression tasks.
