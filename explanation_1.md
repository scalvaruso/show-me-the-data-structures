# Problem 1

## Reasoning Behind Decisions

The `LRU_Cache` class is implemented using an `OrderedDict` from the `collections` module to efficiently maintain a Least Recently Used (LRU) cache. The key design choices include:

1. **OrderedDict Usage**: `OrderedDict` maintains key-value pairs in the order of insertion, allowing easy access and updates while preserving the LRU ordering.
2. **Move-to-End Strategy**: The `get` and `set` methods use `move_to_end(key)` to update the order of recently accessed items, ensuring the least recently used item is always at the front.
3. **Eviction Mechanism**: When the cache reaches its capacity, the least recently used item is removed using `popitem(last=False)`, which efficiently removes the first inserted key-value pair.
4. **Handling Edge Cases**:
   - If the cache capacity is `0`, it does not store any elements.
   - Ensures only integer keys are stored, preventing invalid insertions.
   - Maintains correct behavior even when a single-item cache is used.

These choices ensure an efficient and robust LRU cache implementation.

## Time Efficiency

The implemented `LRU_Cache` provides optimal time complexity:

1. **Get Operation (`get`)**:
   - Checking key existence (`if key not in self.cache`) takes **O(1)**.
   - Moving the accessed key to the end (`move_to_end(key)`) takes **O(1)**.
   - Fetching the value from `OrderedDict` is **O(1)**.
   - Overall, `get()` runs in **O(1)** time.

2. **Set Operation (`set`)**:
   - Checking if a key exists (`if key in self.cache`) takes **O(1)**.
   - If inserting a new key and the cache is full, `popitem(last=False)` removes the least recently used item in **O(1)**.
   - Adding or updating a key-value pair takes **O(1)**.
   - Overall, `set()` runs in **O(1)** time.

Since both `get` and `set` operations have **O(1)** complexity, this LRU cache is highly efficient even for large-scale usage.

## Space Efficiency

The space complexity of `LRU_Cache` is **O(N)**, where `N` is the cache's maximum capacity. The primary space considerations include:

1. **OrderedDict Storage**:
   - Stores up to `N` key-value pairs, leading to **O(N)** space usage.
   - Uses a hashmap and a doubly linked list internally, slightly increasing memory usage.

2. **No Extra Data Structures**:
   - The implementation only relies on `OrderedDict`, avoiding unnecessary memory overhead.

Thus, the space complexity remains **O(N)**, making this LRU cache implementation memory-efficient while ensuring quick access and updates.

