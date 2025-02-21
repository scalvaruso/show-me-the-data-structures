# Problem 5

## Reasoning Behind Decisions

The `Blockchain` and `Block` classes are designed to implement a simple blockchain system. Key design choices include:

1. **Immutable Block Structure**: Each `Block` contains a timestamp, data, a reference to the previous block's hash, and its own hash. This ensures the integrity of the blockchain.
2. **SHA-256 Hashing**: The `calc_hash` method securely hashes the block's contents, preventing tampering.
3. **Genesis Block Initialization**: The blockchain starts with a genesis block, ensuring that the chain always has at least one block.
4. **Sequential Block Addition**: New blocks are appended to the chain with a reference to the last block's hash, forming a continuous, verifiable chain.
5. **Data Validation**: The `add_block` method checks for non-empty data before adding a block, preventing invalid blocks from being added.

## Time Efficiency

The time complexity of operations in the blockchain implementation:

1. **Block Hash Calculation (`calc_hash`)**:
   - String concatenation and encoding run in **O(1)**.
   - SHA-256 hashing runs in **O(1)** for reasonably sized inputs.
   - Overall, `calc_hash()` runs in **O(1)**.

2. **Adding a Block (`add_block`)**:
   - Retrieving the previous block is **O(1)**.
   - Hash computation is **O(1)**.
   - Appending to a list is **O(1)**.
   - Overall, `add_block()` runs in **O(1)**.

3. **Creating the Blockchain (`Blockchain.__init__`)**:
   - Creating the genesis block is **O(1)**.
   - Overall, blockchain initialization runs in **O(1)**.

Since all operations are **O(1)**, the blockchain efficiently handles sequential block additions.

## Space Efficiency

The space complexity of the blockchain implementation:

1. **Block Storage**:
   - Each block stores a timestamp, data, previous hash, and its own hash.
   - If `N` is the number of blocks, space usage is **O(N)**.

2. **Blockchain Storage**:
   - The blockchain maintains a list of `N` blocks, requiring **O(N)** space.
   - Each block's hash is stored as a string of fixed length, contributing to **O(N)** total space.

3. **No Redundant Data Structures**:
   - The implementation does not use extra memory beyond necessary block storage.

Thus, the blockchain maintains an efficient space complexity of **O(N)** while ensuring security and integrity.
