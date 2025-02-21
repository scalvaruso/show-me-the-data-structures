# Problem 6

## Union Function

### Reasoning Behind Decisions (Union)

The `union` function is designed to compute the union of two linked lists efficiently. Key design choices include:

1. **Set Data Structure**: The use of sets allows for O(1) average time complexity for insertion and membership tests, making it suitable for collecting unique elements from both linked lists.
2. **Helper Functions**: The function relies on two helper functions: `linked_list_to_set`, which converts a linked list to a set, and `set_to_linked_list`, which converts a set back to a linked list. This separation of concerns promotes code modularity and reusability.
3. **Type Checking**: Before processing, the function checks if the inputs are valid linked lists, returning an empty linked list if not. This decision enhances robustness by ensuring that incorrect inputs do not cause runtime errors.

### Time Efficiency of Union Function

The `union` function achieves an efficient time complexity:

1. **Set Conversion (`linked_list_to_set`)**:
   - Iterating through the first linked list to create `set_1` takes **O(N)** time, where `N` is the number of nodes in the first linked list.
   - Similarly, creating `set_2` from the second linked list also takes **O(M)** time, where `M` is the number of nodes in the second linked list.

2. **Union Operation**:
   - The union of the two sets, `set_1 | set_2`, runs in **O(N + M)**, where the resulting set contains unique elements from both lists.

3. **Conversion to Linked List (`set_to_linked_list`)**:
   - Sorting the set and appending its elements back to a linked list takes **O(K log K)**, where `K` is the number of unique elements in the union.

Overall, the time complexity of the `union` function is **O(N + M + K log K)**, making it efficient for large datasets.

### Space Efficiency of Union Function

The space efficiency of the `union` function is as follows:

1. **Set Storage**:
   - Both `set_1` and `set_2` require **O(N)** and **O(M)** space, respectively, to store the unique elements from the linked lists.
   - The maximum space required would be when all elements are unique, which leads to a total space complexity of **O(N + M)** for the sets.

2. **Output Linked List**:
   - The new linked list that contains the union of unique elements also requires space proportional to the number of unique elements, which can be up to **O(K)**.

In total, the space complexity for the `union` function is **O(N + M + K)**, which is reasonable considering the functionality it provides.

## Intersection Function

### Reasoning Behind Decisions (Intersection)

The `intersection` function computes the intersection of two linked lists by leveraging the efficiency of set operations. Key design choices include:

1. **Set Data Structure**: Similar to the union function, using sets allows for quick identification of common elements between the two linked lists.
2. **Helper Functions**: The reliance on `linked_list_to_set` ensures that the conversion from a linked list to a set is efficient and concise, encapsulating the logic within a dedicated function.
3. **Input Validation**: The function checks if the inputs are valid linked lists and returns an empty linked list otherwise. This decision improves code stability and prevents processing invalid data.

### Time Efficiency of Intersection Function

The `intersection` function maintains an efficient time complexity:

1. **Set Conversion (`linked_list_to_set`)**:
   - Converting the first linked list to a set (`set_1`) takes **O(N)** time, where `N` is the number of nodes in the first linked list.
   - Converting the second linked list to a set (`set_2`) takes **O(M)** time, where `M` is the number of nodes in the second linked list.

2. **Intersection Operation**:
   - The intersection operation, `set_1 & set_2`, runs in **O(min(N, M))** on average, as it processes the smaller set to check membership.

3. **Conversion to Linked List (`set_to_linked_list`)**:
   - Converting the resulting intersection set back to a linked list involves sorting and appending, which takes **O(K log K)**, where `K` is the number of unique elements in the intersection.

In summary, the time complexity of the `intersection` function is **O(N + M + K log K)**, making it suitable for various input sizes.

### Space Efficiency of Intersection Function

The space efficiency of the `intersection` function can be summarized as follows:

1. **Set Storage**:
   - Both `set_1` and `set_2` require **O(N)** and **O(M)** space, respectively, leading to a maximum combined space complexity of **O(N + M)** if all elements are unique.

2. **Output Linked List**:
   - The new linked list for storing the intersection requires **O(K)** space, where `K` is the number of unique common elements.

Therefore, the overall space complexity for the `intersection` function is **O(N + M + K)**, which is efficient given its design and purpose.
