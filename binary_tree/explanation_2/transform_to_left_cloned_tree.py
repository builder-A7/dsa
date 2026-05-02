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
    # SCENARIO: Transform to Left Cloned Tree
    # ---------------------------------------------------------
    def transform_to_left_cloned_tree(self, node):
        # Edge Case / Base Case: Return None for empty branches
        if node is None:
            return None

        # FAITH (Post-order Traversal):
        # Recursively transform the left and right subtrees FIRST
        lcr = self.transform_to_left_cloned_tree(node.left)
        rcr = self.transform_to_left_cloned_tree(node.right)

        # EXPECTATION LINK (The Rewiring Scenario):
        # 1. Create the clone node with the current node's data
        clone_node = Node(node.data)

        # 2. Attach the transformed left subtree (LCR) to the clone's left
        clone_node.left = lcr
        # Explicit Edge Case handling: The clone's right must remain None
        clone_node.right = None

        # 3. Rewire the current node's pointers
        node.left = clone_node
        node.right = rcr

        # Return the fully transformed node up to its parent
        return node


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will mutate the tree in-place:
    # tree.transform_to_left_cloned_tree(root_node)

    # You would typically follow this up by calling your display() or traversal method
    # to prove to the interviewer that the structure has been successfully cloned.
    pass

"""
The "Expectation-Faith" Recursive Strategy
The video explicitly teaches recursion through an Expectation-Faith framework.

The Example: Imagine a root node A with a left child B and a right child C.

Expectation: We want transform(A) to return a fully left-cloned version of the entire tree.

Faith: We blindly trust that if we call transform(B), it will correctly do all the complex work to left-clone the entire subtree rooted at B. We call this result the Left Cloned Root (LCR). 
We have the exact same faith that transform(C) will yield the Right Cloned Root (RCR).

The Link (Meeting Expectation): Once B and C are transformed into LCR and RCR, A's only responsibility is to handle itself. It creates a new A_clone node. It sets A_clone.left = LCR. Then, it updates its own pointers: A.left = A_clone and A.right = RCR.

Core Scenarios & Edge Cases
Post-Order Execution Scenario (Crucial): The video highlights that the rewiring must happen in the post-order region of the recursion (after the left and right calls return).
If you try to clone and re-wire before traversing down (pre-order), you will lose your original pointers and trap the algorithm in an infinite loop traversing down the newly created clones.

The Null Base Case: The absolute first check must be if node is None: return None. This acts as the anchor.
When a leaf node asks its null children for their transformed subtrees, this base case safely returns None, allowing the leaf to clone itself and attach None as the subtrees.

Clone Right-Pointer Scenario: When the duplicate node is instantiated, its right pointer must explicitly be initialized and kept as None.

The clone only intercepts the left branch.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized implementation. This achieves O(N) Time Complexity (since we visit each node exactly once to clone it) and O(H) Space Complexity (dictated by the recursion stack depth, where H is the height of the tree).
"""
