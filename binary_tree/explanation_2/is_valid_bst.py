class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, algorithms, get_tilt, etc., remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Is a tree Binary Search Tree (Optimized O(N) Stateless)
    # ---------------------------------------------------------
    def is_bst(self, node):
        # We only care about the boolean status (index 0 of the returned tuple)
        is_bst_flag, _, _ = self._is_bst_helper(node)
        return is_bst_flag

    def _is_bst_helper(self, node):
        # Edge Case: The mathematical identity of an empty branch
        # A null node is a valid BST. Its min is Infinity, max is -Infinity.
        if node is None:
            return True, float("inf"), float("-inf")

        # FAITH: Retrieve the (is_bst, min, max) state from children
        left_is_bst, left_min, left_max = self._is_bst_helper(node.left)
        right_is_bst, right_min, right_max = self._is_bst_helper(node.right)

        # EXPECTATION LINK: Calculate the current node's state

        # 1. Scenario 1: Validate BST rules against the subtree extremes
        is_node_bst = (
            left_is_bst
            and right_is_bst
            and (node.data > left_max)
            and (node.data < right_min)
        )

        # 2. Scenario 3: Calculate the absolute min and max of the tree rooted here
        current_min = min(node.data, min(left_min, right_min))
        current_max = max(node.data, max(left_max, right_max))

        # Return the newly updated state (is_bst, min, max) upwards to the parent
        return is_node_bst, current_min, current_max


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will output a boolean True/False:
    # print(f"Is the tree a valid BST?: {tree.is_bst(root_node)}")
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly utilizes the Expectation-Faith framework to solve this problem, as a parent node cannot independently verify if its entire subtree is a Binary Search Tree (BST) without deep knowledge of its children's extreme values.

The Example: Imagine a root node 50 with a left child 25 (which has children 12 and 37) and a right child 75.

Expectation: We expect is_bst(50) to evaluate the entire tree. For 50 to know if it's a valid BST, it strictly needs three things from both sides: 1) Is the subtree itself a valid BST? 2) What is the maximum value in the left subtree? 3) What is the minimum value in the right subtree?

Faith: We blindly trust that if we call our helper function on the left child 25, it will correctly return a package of three data points: (is_bst_status, min_value, max_value) for the entire left branch. We have the same faith for the right child 75.

The Link (Meeting Expectation): Once 50 receives the data, it links them together. It evaluates itself as a BST only if:
The left subtree reported True.
The right subtree reported True.

50 is strictly greater than the left subtree's maximum (37 in this case).
50 is strictly less than the right subtree's minimum. 
Finally, 50 calculates its own overall minimum and maximum to return upward to its parent.

Core Scenarios & Logic
Scenario 1: The Immediate Child Trap: A common mistake is just checking if node.left.data < node.data < node.right.data. The video emphasizes that a node must be greater than all nodes in its left subtree, not just the immediate child. 
Comparing against the left subtree's overall max guarantees this.

Scenario 2: The Multi-State Return (Tuple Optimization): Since Java doesn't support returning multiple primitives easily, the video builds a BSTPair class. In Python, we optimize space by returning a tuple (is_bst, min, max) at every recursive step, achieving a stateless O(N) single-pass solution.

Scenario 3: The Parent Requirement: Even if a node calculates that it is not a BST, it still must calculate and return its correct min and max. Why? Because its parent still needs those values to calculate its own min and max to pass up the chain.

Specific Edge Cases Discussed
The Null Base Case (Mathematical Identities): When the recursion hits a null leaf, it must return a valid tuple so the leaf nodes don't crash when comparing values. A null node is technically a valid BST (True). Its min should be Infinity (float('inf')), and its max should be -Infinity (float('-inf')).
This acts as a mathematical identity, ensuring that when a real leaf node calculates min(node.data, inf), it correctly evaluates to node.data.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized implementation. This achieves O(N) Time Complexity (visiting every node exactly once) and O(H) Space Complexity (dictated by the recursion stack depth).
"""
