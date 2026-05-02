class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, algorithms, transform methods remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Remove Leaves
    # ---------------------------------------------------------
    def remove_leaves(self, node):
        # Edge Case: Hit an empty branch
        if node is None:
            return None

        # SCENARIO 1: The Erasure (Target Identification)
        # If the current node is a leaf, return None to sever it from its parent
        if node.left is None and node.right is None:
            return None

        # FAITH & THE REASSIGNMENT TRAP (Scenario 3)
        # You MUST catch the returned subtrees and overwrite the current pointers.
        # This is where the actual unlinking of the leaf nodes happens.
        node.left = self.remove_leaves(node.left)
        node.right = self.remove_leaves(node.right)

        # SCENARIO 2: Survival
        # If the node was not a leaf originally, it returns itself up the chain
        return node


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will mutate the tree in place:
    # tree.remove_leaves(root_node)

    # Standard practice is to run your display() or level_order() traversal
    # afterward to prove to the interviewer that all leaf nodes are gone.
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly relies on the Expectation-Faith framework, framing it around how parent nodes receive updated information from their subtrees.

The Example: Imagine node 25, which has leaf nodes 12 (left) and 37 (right).

Expectation: We expect remove_leaves(25) to thoroughly scrub the entire subtree of leaves and return the updated, leaf-free tree rooted at 25.

Faith: We blindly trust that calling remove_leaves(12) will clean the left side. Since 12 is a leaf, our faith tells us it will correctly return null (erasing itself). We similarly trust that remove_leaves(37) will correctly return null.

The Link (Meeting Expectation): Node 25 takes these returned results and overwrites its own pointers: 25.left = null and 25.right = null. Even though 25 now looks like a leaf because it lost its children, it originally wasn't one. Therefore, it returns itself (25) back to its parent (50) to survive.

Core Scenarios & Edge Cases

The problem operates on a strict bottom-up state reassignment strategy.
Scenario 1: The Erasure (Pre-order Leaf Check): A node is a leaf if both its left and right pointers are null. When this is true, the node must return null instead of itself. This effectively deletes the node when the parent catches the return value.

Scenario 2: Single Child Survival: If a node only has one child (e.g., left is null but right has a node), it is not a leaf. It must process its existing child and then return itself to remain in the tree.

Crucial Edge Case (The Reassignment Trap): The video explicitly warns that you must assign the recursive call back to the pointers (node.left = self.remove_leaves(node.left)). If you only make the recursive call without catching the returned null, the leaves will never actually be disconnected from the parent, and the tree will remain unchanged.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized implementation. The leaf validation must happen before the recursive calls to ensure nodes that become leaves (after their children are deleted) are not accidentally cascadingly deleted. This yields O(N) Time Complexity and O(H) Space Complexity.
"""
