class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, etc., remain here) ...

    # SCENARIO: Print / Get K Levels Down
    def get_k_levels_down(self, node, k, result=None):
        if result is None:
            result = []

        # Edge Case 1 & 2: Null node reached OR invalid negative k
        if node is None or k < 0:
            return None

        # Target Scenario: Node is exactly at the requested depth
        if k == 0:
            result.append(node.data)
            # Optimization: Return immediately. No need to explore k-1 (which would be -1)
            return result

        # Recursive Step: The target is k-1 levels away from the children
        self.get_k_levels_down(node.left, k - 1, result)
        self.get_k_levels_down(node.right, k - 1, result)

        return result


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this to find nodes 2 levels down from the root:
    # print("Nodes 2 levels down:", tree.get_k_levels_down(root_node, 2))
    pass


"""
Core Logic & Relative Depth Scenario
The problem asks to find all nodes exactly k levels down from a given starting node. The problem-solving intuition here relies on Relative Depth: if the target nodes are k distance away from the current node, they are exactly k - 1 distance away from its immediate children. 

By decrementing k with each recursive call, the target depth naturally becomes 0.
Specific Edge Cases & Scenarios Discussed
To prevent runtime exceptions and optimize the recursion, the video highlights these exact conditions:

Target Reached Scenario (k == 0): When k reaches 0, the current node is at the correct depth. Record its data and stop recursing deeper down that branch.

Null Node Edge Case: If you reach a None node before k becomes 0, it means that specific branch is too short. You must immediately return.

Negative k Corner Case: If the initial k provided is less than 0, or if the code accidentally overshoots, explicitly checking for k < 0 prevents invalid memory access or unnecessary operations.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context. In standard interviews, instead of just printing the values to the console as done in the video, you are expected to accumulate them in a list and return them. 

This implementation achieves O(N) Time Complexity (in the worst-case skewed tree) and O(H) Space Complexity (for the recursive call stack).
"""
