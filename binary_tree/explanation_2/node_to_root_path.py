class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, etc., remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Node to Root Path
    # ---------------------------------------------------------
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

        # Scenario 2: Faith in the left branch
        if self._find_and_fill_path(node.left, target, path):
            # Expectation met: Target is in the left branch, add self to path
            path.append(node.data)
            return True

        # Scenario 3: Faith in the right branch
        if self._find_and_fill_path(node.right, target, path):
            # Expectation met: Target is in the right branch, add self to path
            path.append(node.data)
            return True

        # Scenario 4: Dead-End
        return False


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find the path from 30 to the root:
    # Expected output for target 30: [1, 7-9]
    # print("Path from target to root:", tree.get_node_to_root_path(root_node, 30))
    pass


"""
The "Expectation-Faith" Recursive Strategy
Yes, the video explicitly uses the Expectation-Faith framework to build the recursive logic for this problem.

The Example: Imagine the root is 50, its left child is 25, and its right child is 75. You want to find the path to the target node 70.

Expectation: We expect our main function to search the entire tree and return True if 70 is found, while populating a path array.
Faith: We blindly trust that if we ask the left child 25, it will completely search its subtree. If it finds 70, it will return True. We have the exact same faith in the right child 75.

The Link (Meeting Expectation): If 50 is not the target, it delegates to 25. If 25 returns False, 50 delegates to 75. If 75 returns True, 50 simply says, "Since it was found in my right branch, I am part of the path to the root." It appends itself to the path array and returns True to its own parent.

Core Scenarios & Logic
The algorithm operates as a Boolean Depth-First Search (DFS) that constructs the path bottom-up as the recursive calls return True.

Scenario 1: Self-Match (The Origin): If the current node's data matches the target data, append its value to the path array and immediately return True.

Scenario 2: Left Subtree Match: If the node is not the target, make a recursive call to the left child. If that call returns True, append the current node to the path array and return True upwards.

Scenario 3: Right Subtree Match: If the left subtree returns False, make the same check on the right child. If True, append the current node and return True.

Scenario 4: Dead-End: If the target is not the node itself, not in the left subtree, and not in the right subtree, return False to signal the parent to keep searching elsewhere.

Specific Edge Cases Discussed
The Null Base Case: The absolute first check in your function must be if node is None: return False. 

This safely handles hitting the empty leaves of the tree without throwing an exception, correctly signifying that an empty branch does not contain the target.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the interview-optimized Python implementation. By using a boolean helper function to populate a passed list, we avoid the heavy space complexity of copying or instantiating new lists at every recursive step. 
This yields O(N) Time Complexity (visiting every node in the worst case) and O(H) Space Complexity (where H is the height of the tree, representing the recursion stack and the output path array).
"""
