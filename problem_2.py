import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Recursively finds all files within the given directory (including subdirectories)
    that end with the specified suffix.

    Parameters:
    -----------
    suffix : str
        The file extension or suffix to filter files by (e.g., ".txt").
    path : str
        The root directory path where the search begins.

    Returns:
    --------
    list[str]
        A sorted list of file paths that match the suffix.
    """

    # Check the suffix is a non-empty string
    if not isinstance(suffix, str) or not suffix:
        print("Error: Suffix must be a non-empty string.")
        return None  # Return None for invalid input
    
    # Check the path exists and is a string
    if not isinstance(path, str) or not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return None

    # Check the path is a directory
    if not os.path.isdir(path):
        print(f"Error: The path '{path}' is not a directory.")
        return None
    
    result = []  # List to store file paths
    stack = [path]  # Using a stack to implement Depth-First Search (DFS)

    while stack:
        current_path = stack.pop()  # Retrieve the last inserted directory (LIFO order)

        for item in os.listdir(current_path):  # Iterate over the items in the directory
            full_path = os.path.join(current_path, item)  # Get the full path of the item

            if os.path.isfile(full_path) and (full_path.endswith(suffix) or suffix == ".*"):
                # If it's a file and matches the given suffix, add it to results
                result.append(full_path)
            elif os.path.isdir(full_path):
                # If it's a directory, add it to the stack for further exploration
                stack.append(full_path)
    
    return sorted(result)  # Return a sorted list of matching files


def test_find_files(suffix, path, expected_output):
    """
    Test function to validate the find_files function.
    """
    result = find_files(suffix, path)

    try:
        assert result == expected_output
        print(f"\033[92m****    ****    Pass    ****    ****\033[0m\n{expected_output}\n\033[92m****    ****    ****    ****    ****\033[0m\n")

    except:
        print(f"\033[91m****    ****    Fail    ****    ****\033[0m\nExpected output:\n{expected_output}\nReturned:\n{result}\n\033[91m****    ****    ****    ****    ****\033[0m\n")


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    suffix = ".c"
    path = "./testdir"
    expected_output = ["./testdir/subdir1/a.c", "./testdir/subdir3/subsubdir1/b.c", "./testdir/subdir5/a.c", "./testdir/t1.c"]
    test_find_files(suffix, path, expected_output)

    # Test Case 2: Find all files regardless of suffix
    print("Test Case 2: Find all files regardless of suffix")
    suffix = ".*"
    path = "./testdir"
    expected_output = ["./testdir/subdir1/a.c", "./testdir/subdir1/a.h", "./testdir/subdir2/.gitkeep",
                        "./testdir/subdir3/subsubdir1/b.c", "./testdir/subdir3/subsubdir1/b.h", "./testdir/subdir4/.gitkeep",
                        "./testdir/subdir5/a.c", "./testdir/subdir5/a.h", "./testdir/t1.c", "./testdir/t1.h"
                        ]
    test_find_files(suffix, path, expected_output)

    # Test Case 3: Invalid suffix (empty string)
    print("Test Case 3: Invalid suffix")
    suffix = ""
    path = "./testdir"
    expected_output = None
    test_find_files(suffix, path, expected_output)

    # Test Case 4: Non-existing directory
    print("Test Case 4: Non-existing directory")
    suffix = ".c"
    path = "./test"
    expected_output = None
    test_find_files(suffix, path, expected_output)

    # Test Case 5: Path is not a directory
    print("Test Case 5: Path is not a directory")
    suffix = ".c"
    path = "./problem_2.py"
    expected_output = None
    test_find_files(suffix, path, expected_output)
