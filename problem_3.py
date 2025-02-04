import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq


def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    frequency = defaultdict(int)    # Default dictionary to initialize frequencies to 0
    for char in data:
        frequency[char] += 1    # Increment frequency count for each character
    return dict(frequency)


def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    # Create a priority queue (min-heap) with leaf nodes for each character
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)   # Convert the list into a valid min-heap
    
    # Continue merging nodes until one root node remains
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)    # Extract node with smallest frequency
        right = heapq.heappop(priority_queue)   # Extract second smallest node

        # Create a new internal node with combined frequency
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add new node back to the heap
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]    # Return root node of the Huffman Tree


def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return
    
    # If the node is a leaf (has a character), store its code
    if node.char is not None:
        huffman_codes[node.char] = code
    
    # Recur for left and right children with appropriate bit added to code
    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if  data is None or not data:   # Edge case: Handle empty or None input
        return "", None
    
    frequency = calculate_frequencies(data) # Calculate character frequencies
    root = build_huffman_tree(frequency)    # Build Huffman Tree
    huffman_codes = {}
    
    # Edge case: If only one unique character exists, assign the code "0" as its code
    if len(frequency) == 1:
        only_char = next(iter(frequency))
        huffman_codes[only_char] = "0"
    else:
        generate_huffman_codes(root, "", huffman_codes) # Generate Huffman codes

    # Encode data by replacing characters with their Huffman codes
    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, root


def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not encoded_data or tree is None:    # Handle empty input cases
        return ""
    
    # Edge case: If the tree consists of only one character
    if tree.left is None and tree.right is None:
        return tree.char * len(encoded_data)  # Repeat the character for all bits
    
    decoded_data = ""   # Initialize decoded string
    current_node = tree # Start traversal from root

    for bit in encoded_data:
        current_node = current_node.left if bit == "0" else current_node.right

        # If a leaf node is reached, append character and restart from root
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree # Reset to root for next character
    
    return decoded_data


# Main Function
if __name__ == "__main__":

    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Single character repeated
    print("\nTest Case 2: Single character repeated")
    sentence = "aaaaaaa"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 3: Empty string
    print("\nTest Case 3: Empty string")
    sentence = ""
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 4: Large input
    print("\nTest Case 4: Large input")
    sentence = "abcd" * 50000  # Very large input
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data[:40],"...",encoded_data[-40:])
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data[:20],"...",decoded_data[-20:])
    assert sentence == decoded_data
    print("Large input test passed.")

    # Test Case 5: Null input
    print("\nTest Case 5: Null input")
    sentence = None
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert encoded_data == "" and decoded_data == ""
