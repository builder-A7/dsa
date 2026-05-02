class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, algorithms, etc., remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Path to Leaf from Root (in Range)
    # ---------------------------------------------------------
    def get_paths_to_leaf_in_range(self, node, lo, hi):
        result = []
        # We use a helper function to manage the backtracking array 'current_path'
        # and the running integer 'current_sum' without polluting the main signature.
        self._path_to_leaf_helper(node, lo, hi, 0, [], result)
        return result

    def _path_to_leaf_helper(self, node, lo, hi, current_sum, current_path, result):
        # Edge Case: Prevent AttributeError on nodes with only a single child
        if node is None:
            return

        # Scenario 1: Accumulate state (Top-Down) before processing children
        current_sum += node.data
        current_path.append(node.data)

        # Scenario 2: Leaf Node Identification & Range Validation
        if node.left is None and node.right is None:
            if lo < current_sum < hi:
                # Append a copy of the path, because the original array will be mutated by backtracking
                result.append(list(current_path))
        else:
            # Recursive Step: Not a leaf, keep passing the state down
            self._path_to_leaf_helper(
                node.left, lo, hi, current_sum, current_path, result
            )
            self._path_to_leaf_helper(
                node.right, lo, hi, current_sum, current_path, result
            )

        # BACKTRACKING: Remove the current node's data before returning to the parent
        # This keeps the Space Complexity strictly O(H) (height of the tree)
        current_path.pop()


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find paths with sums strictly between 150 and 250:
    # Expected output: A list of lists containing the valid paths (e.g., [[1, 4-6], ...])
    # print("Valid Paths:", tree.get_paths_to_leaf_in_range(root_node, 150, 250))
    pass


"""
The Recursive Thought Process: Top-Down State vs. Expectation-Faith
Regarding your special note: This specific video does not use the "Expectation-Faith" (bottom-up) framework.

In "Expectation-Faith" (used for problems like finding the Max or Transforming a Tree), you ask your children for an answer, wait for them to return it, and then build your answer based on theirs.

However, for "Path to Leaf", the problem requires Top-Down State Accumulation. You cannot ask a child "What is your path?" because the path starts from the root. Instead, the parent accumulates the state (its own data + the running sum) and passes it down to the children. 

The recursive thought process here is: "I will add myself to the running sum and path, and hand this updated information to my left and right children so they know the story so far."

Core Scenarios & Logic
Scenario 1: Pre-order State Update: When you land on a node, you immediately add its value to the current_sum and append it to the current_path before making any recursive calls to the children.

Scenario 2: Leaf Node Identification & Validation: A node is confirmed as a leaf only if both its left and right children are null
. Once confirmed, you check if the current_sum falls strictly between the lo and hi limits. 

If it does, the path is valid and recorded.
Specific Edge Cases Discussed
The Single Child Trap (Null Pointer Prevention): If a node has a left child but no right child, it is not a leaf. If your code blindly makes a recursive call to the missing right child, the program will crash when it attempts to read the null node's data. 

The explicit base case if node is None: return gracefully catches this and bounces back without crashing.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context. In the video, they pass strings to build the path. For a mid-senior interview, passing immutable strings in recursion creates an \
    O(N ^ 2 ) time complexity overhead. The optimized standard is to use an array and Backtrack (append when going down, pop when coming up), keeping space complexity at strictly O(H).
"""
