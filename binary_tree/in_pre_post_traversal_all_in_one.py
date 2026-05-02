class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, get_size, get_sum, get_max, get_height remain here) ...

    # UNIFIED TRAVERSAL: Demonstrating Pre, In, and Post order in a single Euler Tour
    def traversals(self, node):
        # Critical Edge Case: Base condition to prevent AttributeError on leaf node children
        if node is None:
            return

        # SCENARIO 1: Pre-order (Processed before visiting any children)
        # In an interview, you might append to an array here instead of printing
        print(f"Pre-order: {node.data}")

        # Go deep into the left subtree
        self.traversals(node.left)

        # SCENARIO 2: In-order (Processed between the left and right subtrees)
        print(f"In-order: {node.data}")

        # Go deep into the right subtree
        self.traversals(node.right)

        # SCENARIO 3: Post-order (Processed after fully exploring both subtrees)
        print(f"Post-order: {node.data}")


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, you would call the traversal like this:
    # tree.traversals(root_node)
    pass


"""
Core Traversal Scenarios & Euler Tour Logic
The video explains binary tree traversals (Pre-order, In-order, Post-order) using a unified "Euler Tour" structural approach rather than treating them as entirely different algorithms.

A single recursive function can represent all three traversals simply by changing where the node is processed relative to the recursive calls.

Here are the specific execution scenarios expected:
Scenario 1: Pre-order (Node, Left, Right) / "Left Side": You process the node the first time you visit it, before making any recursive calls to its children. This is going deep into the recursion.

Scenario 2: In-order (Left, Node, Right) / "Between Calls": You process the node after returning from the left child's recursion, but before making the recursive call to the right child.

Scenario 3: Post-order (Left, Right, Node) / "Right Side": You process the node after returning from both the left and right children's recursive calls.

Specific Edge Cases Discussed
The Null Base Case: Just like the previous operations, making blind recursive calls (node.left and node.right) requires an explicit base case at the top of the function (if node is None: return) to bounce back gracefully when encountering an empty child.
"""
