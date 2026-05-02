class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, path algorithms, transform_to_left_cloned_tree, etc., remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Transform Back from a Left Cloned Tree
    # ---------------------------------------------------------
    def transform_back_from_left_cloned_tree(self, node):
        # Edge Case / Base Case: Handle empty branches and the null children of leaf clones
        if node is None:
            return None

        # FAITH:
        # 1. Normalize the true left subtree.
        # Scenario: The true left child is always at node.left.left (bypassing the clone)
        # Note: We safely assume node.left is never None here because the problem guarantees a valid left-cloned tree input.
        left_normalized = self.transform_back_from_left_cloned_tree(node.left.left)

        # 2. Normalize the true right subtree.
        # Right children were not shifted, so they remain at node.right
        right_normalized = self.transform_back_from_left_cloned_tree(node.right)

        # EXPECTATION LINK (The Rewiring Scenario):
        # Overwrite the current node's pointers with the normalized subtrees.
        # This completely severs the connection to the clone (node.left), letting it be garbage collected.
        node.left = left_normalized
        node.right = right_normalized

        # Return the fully restored node up to its parent
        return node


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, you would demonstrate this as a two-step process:
    # 1. First, clone the tree (from our previous prompt)
    # tree.transform_to_left_cloned_tree(root_node)

    # 2. Then, restore it using our new algorithm
    # restored_root = tree.transform_back_from_left_cloned_tree(root_node)
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly uses the Expectation-Faith framework to formulate the solution, utilizing a tree structure with nodes A (root), B (left child), and C (right child).

The Example: In the left-cloned tree, node A's immediate left child is its clone A'. The real left child B is pushed down to A.left.left (which also has its own clone B'). Node C remains at A.right (but has its own clone C').

Expectation: We expect transform_back(A) to completely normalize the entire tree, stripping away all clones and returning the original structure A -> B and A -> C.

Faith: We blindly trust that if we call transform_back on the actual left child B (located at A.left.left), it will perfectly normalize the B subtree. We have the same faith that transform_back(C) (located at A.right) will perfectly normalize the C subtree.

The Link (Meeting Expectation): Once B and C return as normalized subtrees, A simply overwrites its pointers. It sets A.left = normalized_B and A.right = normalized_C. By doing this, the clone A' is entirely bypassed and dropped to the garbage collector.

Core Scenarios & Logic
Scenario 1: Bypassing the Clone (The Left Leap): Because every original node has a clone inserted as its immediate left child, the true left subtree always resides exactly at node.left.left. Your recursive call must leap over the clone to process the real subtree.

Scenario 2: The Rewiring (Severing the Clone): You must rewrite both the left and right pointers of the current node after the recursive calls return. Updating node.left breaks the link to the clone, effectively restoring the tree to its original state.

Specific Edge Cases Discussed
The Null Base Case: The function must begin with if node is None: return None. When the algorithm reaches a true leaf node (say D), it will attempt to process D.left.left. Since D.left is the clone D', and D' has no children, D.left.left evaluates to None. The base case catches this, safely returning None to be attached as the normalized left child.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized implementation. This achieves O(N) Time Complexity (visiting only the original nodes) and O(H) Space Complexity (dictated by the recursion stack depth).

"""
