class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array and display methods from previous prompts remain here) ...

    # 1. SIZE: Total number of nodes
    def get_size(self, node):
        # Edge Case: Null node contributes 0 to the size
        if node is None:
            return 0

        left_size = self.get_size(node.left)
        right_size = self.get_size(node.right)

        return left_size + right_size + 1

    # 2. SUM: Sum of all node values
    def get_sum(self, node):
        # Edge Case: Null node contributes 0 to the sum
        if node is None:
            return 0

        left_sum = self.get_sum(node.left)
        right_sum = self.get_sum(node.right)

        return left_sum + right_sum + node.data

    # 3. MAX: Maximum value in the tree
    def get_max(self, node):
        # Critical Edge Case: Must return -Infinity to handle trees with negative numbers
        if node is None:
            return float("-inf")

        left_max = self.get_max(node.left)
        right_max = self.get_max(node.right)

        # Compare left max, right max, and current node's data
        return max(node.data, max(left_max, right_max))

    # 4. HEIGHT: Depth of the tree in terms of edges
    def get_height(self, node):
        # Critical Edge Case: Return -1 so a single-node tree evaluates to height 0
        if node is None:
            return -1

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return max(left_height, right_height) + 1


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, you would call them like this:
    # print(f"Size: {tree.get_size(root_node)}")
    # print(f"Sum: {tree.get_sum(root_node)}")
    # print(f"Max: {tree.get_max(root_node)}")
    # print(f"Height: {tree.get_height(root_node)}")
    pass


"""
Core Scenarios & Logic
The video covers four fundamental recursive operations: Size, Sum, Max, and Height. For each operation, the recursive logic relies on faith: you ask the left child for its answer, the right child for its answer, and then process those alongside the current node's data.

Unlike Generic Trees where you loop through an arbitrary number of children (skipping empty ones naturally), Binary Trees explicitly call left and right pointers regardless of whether they exist. This makes Null Pointer Base Cases the most critical edge cases to handle to prevent exceptions.

Specific Edge Cases & Base Cases Discussed
Size & Sum Base Case (The Zero Identity): When a node is null, it contributes nothing to the count or the total. The base case must explicitly return 0 so size(left) + size(right) + 1 evaluates correctly without breaking.

Max Base Case (The Negative Infinity Edge Case): When finding the maximum value, a null node cannot return 0. If the tree contains entirely negative numbers, returning 0 for a null leaf would incorrectly make 0 the maximum value. You must return the mathematical identity of maximum, which is -Infinity (-float('inf') in Python).

Height Base Case (Edges vs. Nodes): Height is usually measured in terms of edges (distance). A tree with a single node has a height of 0.
Therefore, the base case for a null node must return -1. This ensures that when the leaf node calculates max(-1, -1) + 1, it correctly results in 0.
"""
