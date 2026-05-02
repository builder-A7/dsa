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
    # MODIFIED HELPERS FOR "K LEVEL FAR"
    # ---------------------------------------------------------

    # Modified from previous prompt: Now accepts and checks a 'blocker' node
    def _get_k_levels_down_with_blocker(self, node, k, blocker, result):
        # Edge Case 1 & 2: Null node reached, invalid k, OR hitting the blocker node
        if node is None or k < 0 or node == blocker:
            return

        # Target Scenario: Node is exactly at the requested depth
        if k == 0:
            result.append(node.data)
            return

        # Recursive Step
        self._get_k_levels_down_with_blocker(node.left, k - 1, blocker, result)
        self._get_k_levels_down_with_blocker(node.right, k - 1, blocker, result)

    # Modified from previous prompt: Returns actual Node objects instead of just data
    def _get_node_to_root_path_objects(self, node, target_data, path):
        if node is None:
            return False

        if node.data == target_data:
            path.append(node)
            return True

        if self._get_node_to_root_path_objects(node.left, target_data, path):
            path.append(node)
            return True

        if self._get_node_to_root_path_objects(node.right, target_data, path):
            path.append(node)
            return True

        return False

    # ---------------------------------------------------------
    # SCENARIO: Nodes K Level Far (The Main Algorithm)
    # ---------------------------------------------------------
    def get_nodes_k_level_far(self, node, target_data, k):
        path = []
        # Get the path of Node objects from the target up to the root
        self._get_node_to_root_path_objects(node, target_data, path)

        result = []

        # Traverse the ancestors in the path
        for i in range(len(path)):
            ancestor = path[i]

            # The blocker is the node we just came from (i - 1).
            # Edge Case: For the target node itself (i == 0), blocker is None.
            blocker = path[i - 1] if i > 0 else None

            # The ancestor is at distance 'i' from the target.
            # Look downwards for the remaining distance 'k - i'.
            remaining_k = k - i

            # Edge Case: Only search if the remaining distance is valid
            if remaining_k >= 0:
                self._get_k_levels_down_with_blocker(
                    ancestor, remaining_k, blocker, result
                )

        return result


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find nodes 3 levels far from target '25':
    # Expected execution will leverage the blocker to prevent revisiting nodes
    # print("Nodes 3 levels far from 25:", tree.get_nodes_k_level_far(root_node, 25, 3))
    pass


"""
Core Scenarios & "Ancestor Backtracking" Logic:
To find all nodes exactly k distance away from a target node (which includes nodes below it, above it, and in separate branches), the video combines our two previously created algorithms: Node to Root Path and Print K Levels Down.

The problem-solving intuition is to first find the path array from the target node up to the root.

For any ancestor node located at index i in this path array, it is exactly i distance away from the target.

To find nodes that are a total of k distance away, we simply tell that ancestor to look downwards for the remaining distance: k - i.

Specific Edge Cases & Scenarios Discussed:
The Blocker Node Scenario (Crucial): When you ask an ancestor to look downwards, it will naturally try to search down both its left and right subtrees. You must prevent it from traversing back down the same branch that contains the target, otherwise, you will print incorrect nodes.

You achieve this by modifying the k_levels_down function to accept a "blocker" node. If the recursive call hits the blocker, it immediately returns.

Target Origin Edge Case: When processing the 0th index (the target node itself), there is no previous node in the path to block. The blocker must be passed as None (null) so it can freely search both of its own subtrees.

Negative Distance Edge Case: If k - i < 0, it means the current ancestor is already further away from the target than the requested distance k. You must ensure your downward search handles or ignores negative k values.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
To implement this while maintaining continuity with our BinaryTree class, we need to introduce a minor modification: our previous get_node_to_root_path returned an array of integers (data). For this algorithm, we need an array of the actual Node objects so we can compare references against the blocker.
"""
