class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, get_k_levels_down, etc., remain here) ...

    # SCENARIO: Node to Root Path
    def get_node_to_root_path(self, node, target):
        path = []
        # We use a helper function to strictly handle the boolean state-machine
        # while modifying the 'path' array in place by reference.
        self._find_and_fill_path(node, target, path)
        return path

    def _find_and_fill_path(self, node, target, path):
        # Edge Case: Null node reached, target is definitely not here
        if node is None:
            return False

        # Scenario 1: Target found at the current node
        if node.data == target:
            path.append(node.data)
            return True

        # Scenario 2: Check if target exists anywhere in the left branch
        if self._find_and_fill_path(node.left, target, path):
            path.append(node.data)
            return True

        # Scenario 3: Check if target exists anywhere in the right branch
        if self._find_and_fill_path(node.right, target, path):
            path.append(node.data)
            return True

        # Scenario 4: Target not found in this node or any of its subtrees
        return False


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find the path from 30 to the root:
    # Expected output for target 30: [1, 5-7]
    # print("Path from target to root:", tree.get_node_to_root_path(root_node, 30))
    pass


"""
Core Scenarios & "Faith and Backtrack" Logic
To find the path from a specific node to the root, the video outlines a Depth-First Search (DFS) approach returning a boolean value to signal success. 

As the recursive calls return True back up the call stack, each ancestor node appends itself to the path array, inherently constructing the path from the target bottom-up to the root.

Here are the specific execution scenarios to handle:
Scenario 1: Self-Match (The Origin): If the current node's data matches the target data, append its value to the path array and immediately return True.

Scenario 2: Left Subtree Match: If the node is not the target, make a recursive call to the left child. If that call returns True, it guarantees the target exists down that branch. Append the current node to the path array and return True upwards.

Scenario 3: Right Subtree Match: If the left subtree returns False, make the same check on the right child. If True, append the current node and return True.

Scenario 4: Dead-End: If the target is not the node itself, not in the left subtree, and not in the right subtree, return False to signal the parent to keep searching elsewhere.

Specific Edge Cases Discussed
The Null Base Case: The absolute first check in your function must be if node is None: return False. This safely handles hitting the end of a branch (leaf node's children) without throwing an exception, and correctly signifies that an empty branch does not contain the target.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the interview-optimized Python implementation. By using a boolean helper function to populate a passed list, we avoid the heavy space complexity of copying or instantiating new lists at every recursive step. This yields O(N) Time Complexity (visiting every node in the worst case) and O(H) Space Complexity (where H is the height of the tree, representing the recursion stack and the output path array).
"""
