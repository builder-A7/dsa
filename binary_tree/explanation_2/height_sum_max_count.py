class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, path algorithms, etc., remain here) ...

    # ---------------------------------------------------------
    # SCENARIO 1: SIZE (Total number of nodes)
    # ---------------------------------------------------------
    def get_size(self, node):
        # Edge Case: Null identity for addition is 0
        if node is None:
            return 0

        # FAITH: Trust children to return their correct sizes
        left_size = self.get_size(node.left)
        right_size = self.get_size(node.right)

        # EXPECTATION LINK: Combine sub-answers + 1 (for the current node)
        return left_size + right_size + 1

    # ---------------------------------------------------------
    # SCENARIO 2: SUM (Sum of all node values)
    # ---------------------------------------------------------
    def get_sum(self, node):
        # Edge Case: Null identity for addition is 0
        if node is None:
            return 0

        # FAITH
        left_sum = self.get_sum(node.left)
        right_sum = self.get_sum(node.right)

        # EXPECTATION LINK: Combine sub-answers + current node's data
        return left_sum + right_sum + node.data

    # ---------------------------------------------------------
    # SCENARIO 3: MAX (Maximum value in the tree)
    # ---------------------------------------------------------
    def get_max(self, node):
        # Critical Edge Case: Must return -Infinity to handle entirely negative trees
        if node is None:
            return float("-inf")

        # FAITH
        left_max = self.get_max(node.left)
        right_max = self.get_max(node.right)

        # EXPECTATION LINK: Find the max between the children's maxes and the current node
        return max(node.data, max(left_max, right_max))

    # ---------------------------------------------------------
    # SCENARIO 4: HEIGHT (Depth of the tree in terms of edges)
    # ---------------------------------------------------------
    def get_height(self, node):
        # Critical Edge Case: Return -1 so a single leaf node evaluates to height 0
        if node is None:
            return -1

        # FAITH
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        # EXPECTATION LINK: Max depth of children + 1 (the edge connecting them)
        return max(left_height, right_height) + 1


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing these methods:
    # print(f"Size: {tree.get_size(root_node)}")
    # print(f"Sum: {tree.get_sum(root_node)}")
    # print(f"Max: {tree.get_max(root_node)}")
    # print(f"Height: {tree.get_height(root_node)}")
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly uses the Expectation-Faith framework to build the recursive thought process for all four of these operations.
    
The Example: Imagine a root node 50 with a left child 25 and a right child 75.

Expectation: We expect size(50) (or sum/max/height) to return the correct total value for the entire tree.

Faith: We blindly trust that if we call size(25), it will correctly calculate and return the total number of nodes in the entire left subtree. We have the exact same faith that size(75) will return the correct answer for the right subtree.

The Link (Meeting Expectation): Once 25 and 75 return their sub-answers, the parent 50 just adds its own contribution. For size, it calculates: left_size + right_size + 1 (itself). 
For sum, it calculates: left_sum + right_sum + 50.

Core Scenarios & "Mathematical Identity" Edge Cases

    Because a binary tree restricts nodes to exactly left and right pointers, the standard traversal explicitly delegates calls to node.left and node.right regardless of whether they exist.
To prevent crashes, you must handle the null node edge cases by returning their specific Mathematical Identities.

Size & Sum Base Case (The Zero Identity): A null node contributes nothing. The base case must explicitly return 0.

Max Base Case (The Negative Infinity Edge Case): When finding the maximum value, returning 0 for a null node will yield incorrect results if the tree contains entirely negative numbers. 
You must return the mathematical identity of maximum, which is -Infinity (-float('inf') in Python).

Height Base Case (Edges vs. Nodes Edge Case): Height in this context is measured in edges (distance). 
A tree with a single node has a height of 0.
Therefore, the base case for a null child must return -1.
This ensures that when a leaf node evaluates max(-1, -1) + 1, the result is correctly 0.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here are the highly optimized implementations demonstrating the Expectation-Faith logic. Each method achieves O(N) Time Complexity (visiting every node exactly once) and O(H) Space Complexity (dictated by the recursion stack depth).
"""
