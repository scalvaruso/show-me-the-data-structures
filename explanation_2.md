# Problem 2

## Reasoning Behind Decisions

The `find_files` function is designed to recursively search for files with a specific suffix in a given directory. The key design choices include:

1. **Depth-First Search (DFS) Using a Stack**: A stack is used to implement DFS, making the traversal efficient without requiring recursion.
2. **Validation Checks**:
   - Ensures `suffix` is a non-empty string.
   - Checks if `path` exists and is a valid directory.
   - Handles cases where `path` is not a directory.
3. **Handling All Files Option (`.*`)**:
   - Allows searching for all files regardless of suffix, providing flexibility.
4. **Sorting the Output**:
   - The resulting list of files is sorted to ensure consistent output order.

These choices ensure robustness, efficiency, and ease of use for file searching.

## Time Efficiency

The time complexity of `find_files` is **O(N)**, where `N` is the total number of files and directories within the given path. The breakdown is:

1. **Directory Traversal**:
   - Every directory and file in the given path is visited once, leading to **O(N)** complexity.
2. **File Name Matching**:
   - Checking if a file ends with the given suffix takes **O(1)**.
3. **Sorting**:
   - Sorting the final list takes **O(M log M)**, where `M` is the number of matched files.

Overall, the function runs in **O(N + M log M)** time.

## Space Efficiency

The space complexity of `find_files` is **O(N)**:

1. **Stack Storage**:
   - The stack stores directory paths for DFS traversal, leading to **O(D)** space usage, where `D` is the depth of the directory tree.
2. **Result Storage**:
   - The function stores paths of matching files in a list, consuming **O(M)** space.
3. **No Extra Data Structures**:
   - The implementation does not use additional structures, keeping memory usage minimal.

Thus, the overall space complexity is **O(N)**, making the function efficient for searching large directory structures.
