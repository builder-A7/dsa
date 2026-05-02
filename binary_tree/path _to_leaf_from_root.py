class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, k_levels_far, etc., remain here) ...

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

        # Scenario: Accumulate state before processing children
        current_sum += node.data
        current_path.append(node.data)

        # Scenario: Leaf Node Identification
        if node.left is None and node.right is None:
            # Target Validation: Check if the leaf's final sum is within the strict (lo, hi) range
            if lo < current_sum < hi:
                # Append a copy of the path, because the original array will be mutated by backtracking
                result.append(list(current_path))
        else:
            # Recursive Step: Not a leaf, keep traversing down
            self._path_to_leaf_helper(
                node.left, lo, hi, current_sum, current_path, result
            )
            self._path_to_leaf_helper(
                node.right, lo, hi, current_sum, current_path, result
            )

        # BACKTRACKING: Remove the current node's data before returning to the parent
        # This keeps the Space Complexity strictly O(H)
        current_path.pop()


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find paths with sums strictly between 150 and 250:
    # Expected output: A list of lists containing the valid paths
    # print("Valid Paths:", tree.get_paths_to_leaf_in_range(root_node, 150, 250))
    pass


"""
Core Scenarios & "State Accumulation" Logic
The problem asks to find all paths from the root to leaf nodes where the sum of the nodes in that path falls strictly between a given lo and hi range.
The problem-solving intuition relies on State Accumulation (DFS): you pass the running sum and the path array down the tree recursively.
Here are the specific execution scenarios expected:
Scenario 1: Leaf Node Identification: A node is definitively a leaf only if both its left and right children are null.

Scenario 2: Target Validation (The Timing): You must only check if the accumulated sum is within the (lo, hi) range when you actually reach a leaf node. 
Validating the sum prematurely on a non-leaf node violates the problem's core requirement.

Scenario 3: Accumulating State: When moving from parent to child, the parent adds its own data to the running sum and the path before passing that state down.

Specific Edge Cases & Scenarios Discussed
The Single Child Trap (Null Pointer Prevention): If a node has a left child but no right child, it is not a leaf. If your code blindly calls the right child without a base case, it will crash. The first line of your recursive function must be an explicit if node is None: return to gracefully bounce back from these empty single branches.

The Range Boundary: The video specifically enforces a strict boundary condition where the sum must be strictly greater than lo and strictly less than hi (lo < sum < hi) rather than inclusive. You should clarify this boundary with your interviewer.

--------------------------------------------------------------------------------
Optimization Note: The video mentions passing a concatenated string for the path down the tree. For a mid-senior interview, string concatenation at every recursive step is a red flag because strings are immutable, leading to O(N ^ 2) time complexity for path building. The industry standard is to pass a single array and use Backtracking (append when going down, pop when coming up), reducing space complexity strictly to the recursion stack depth O(H).
"""
