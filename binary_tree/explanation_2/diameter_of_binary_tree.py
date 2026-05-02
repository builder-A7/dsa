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
    # SCENARIO: Diameter of a Binary Tree (Optimized O(N))
    # ---------------------------------------------------------
    def get_diameter(self, node):
        # We only care about the diameter (index 1 of the returned tuple)
        # We start the recursive state machine by calling our helper
        _, final_diameter = self._get_height_and_diameter(node)
        return final_diameter

    def _get_height_and_diameter(self, node):
        # Edge Case: The mathematical identity of a null node
        # Height (in edges) is -1, Diameter is 0
        if node is None:
            return -1, 0

        # FAITH: Retrieve the (height, diameter) tuple from left and right
        left_height, left_dia = self._get_height_and_diameter(node.left)
        right_height, right_dia = self._get_height_and_diameter(node.right)

        # EXPECTATION LINK: Calculate the current node's state

        # Current node's height (max depth of children + 1 edge to connect to them)
        current_height = max(left_height, right_height) + 1

        # Scenario 3: The distance of the path crossing the current root
        cross_dia = left_height + right_height + 2

        # Current node's diameter is the maximum of the 3 scenarios
        current_dia = max(cross_dia, max(left_dia, right_dia))

        # Return the newly updated state upwards
        return current_height, current_dia


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will output the integer representing the longest path:
    # print(f"Diameter of the Tree: {tree.get_diameter(root_node)}")
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly relies on the Expectation-Faith framework to optimize the solution from a naive O(N ^ 2 ) to a highly efficient O(N).

The Example: To find the diameter (maximum distance between any two nodes) of a tree, you need to know three things: the diameter of the left subtree, the diameter of the right subtree, and the maximum depth (height) of both to see if a path crossing the current root is longer.

Expectation: We expect our recursive function to return both the height and the diameter of a subtree simultaneously so we don't have to redundantly calculate height in a separate O(N) pass.

Faith: We blindly trust that if we call get_diameter(node.left), it will return the correct (left_height, left_diameter) pair. We have the exact same faith for get_diameter(node.right).

The Link (Meeting Expectation): The current node receives these two pairs and calculates its own state:
Its own height becomes: max(left_height, right_height) + 1.

Its own diameter becomes the maximum of three candidates: left_diameter, right_diameter, or the path crossing itself (left_height + right_height + 2). 
It then returns its own (height, diameter) pair up the chain.

Core Scenarios & Edge Cases

Scenario 1: Left Subtree Dominance: The longest path might lie entirely within the left branch, never passing through the current node. This corresponds to the left_diameter.

Scenario 2: Right Subtree Dominance: The longest path might lie entirely within the right branch, corresponding to the right_diameter.

Scenario 3: Cross-Root Path: The longest path spans from the deepest node on the left, crosses the current node, and goes to the deepest node on the right. This distance is explicitly left_height + right_height + 2.

The Overlapping Subproblems Trap (Crucial): If you calculate diameter recursively, and inside that call you recursively calculate height, you traverse the same nodes repeatedly, resulting in an O(N ^ 2 ) time complexity. Passing up a combined pair/tuple solves this in O(N).
The Base Case Identity: For a null node, the diameter is 0. However, its height (measured in edges) must be returned as -1. 

This mathematically guarantees that a leaf node correctly calculates its crossing diameter as -1 + -1 + 2 = 0.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context. While the Java video creates a specific DiaPair class, the industry-standard for Python is to return a tuple and unpack it. This strictly adheres to O(N) Time Complexity (single post-order pass) and O(H) Space Complexity (recursion stack depth) without the memory overhead of instantiating thousands of wrapper objects.
"""
