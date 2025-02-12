from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional["Node"] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    tail : Optional[Node]
        The tail node of the linked list (for efficient appends).
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string.rstrip(" -> ")

    def append(self, value: int) -> None:
        """
        Append a new node with the given value in sorted order into the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        new_node = Node(value)

        # Insert at the beginning if list is empty or value is smaller than head
        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node  # Update tail if list was empty
            return

        # Find correct insertion point
        prev, current = None, self.head
        while current and current.value < value:
            prev = current
            current = current.next

        # Insert new node in the correct position
        prev.next = new_node
        new_node.next = current

        # Update tail if inserted at the end
        if current is None:
            self.tail = new_node

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    set_1 = linked_list_to_set(llist_1)
    set_2 = linked_list_to_set(llist_2)

    # Create a new linked list to store the union
    return set_to_linked_list(set_1 | set_2)


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    set_1 = linked_list_to_set(llist_1)
    set_2 = linked_list_to_set(llist_2)

    # Find the intersection of both sets
    # Create a new linked list to store the intersection
    return set_to_linked_list(set_1 & set_2)


def linked_list_to_set(l_list: LinkedList) -> set:
    """Convert a linked list to a set of its values."""
    set_list = set()
    current = l_list.head
    while current:
        set_list.add(current.value)  # Add each node's value to the set
        current = current.next
    return set_list


def set_to_linked_list(elements_set: set) -> LinkedList:
    """Convert a set of values to a linked list."""
    new_linked_list = LinkedList()
    for item in elements_set:
        new_linked_list.append(item)  # Append each item to the linked list
    return new_linked_list


if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3
    pass

    ## Test case 4
    pass
