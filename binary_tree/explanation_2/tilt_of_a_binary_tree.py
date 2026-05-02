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
    # SCENARIO: Tilt of a Binary Tree (Optimized O(N) Stateless)
    # ---------------------------------------------------------
    def get_tilt(self, node):
        # We only care about the accumulated tilt (index 1 of the returned tuple)
        # We start the recursive state machine by calling our helper
        _, total_tilt = self._get_sum_and_tilt(node)
        return total_tilt

    def _get_sum_and_tilt(self, node):
        # Edge Case: The mathematical identity of a null node
        # Both sum and tilt are 0
        if node is None:
            return 0, 0

        # FAITH: Retrieve the (sum, tilt) tuple from left and right subtrees
        left_sum, left_tilt = self._get_sum_and_tilt(node.left)
        right_sum, right_tilt = self._get_sum_and_tilt(node.right)

        # EXPECTATION LINK: Calculate the current node's state

        # 1. Local Tilt: Absolute difference between left sum and right sum
        local_tilt = abs(left_sum - right_sum)

        # 2. Accumulated Tilt: Sum of tilts from left, right, and current node
        current_total_tilt = left_tilt + right_tilt + local_tilt

        # 3. Current Sum: Total sum of the subtree rooted at this node
        current_sum = left_sum + right_sum + node.data

        # Return the newly updated state (sum, tilt) upwards to the parent
        return current_sum, current_total_tilt


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will output the integer representing the total tilt:
    # print(f"Total Tilt of the Tree: {tree.get_tilt(root_node)}")
    pass


"""
The "Expectation-Faith" Recursive Strategy
The video explicitly uses the Expectation-Faith framework to solve this problem, highlighting a critical difference: what you calculate (tilt) is different from what you return (sum).

The Example: Imagine a tree with root A, left child B (with its own children D, E), and right child C (with children F, G).

Expectation: We expect tilt(A) to calculate the total tilt of the entire tree. To find its own local tilt, A desperately needs the total sum of its left subtree and the total sum of its right subtree.

Faith: We blindly trust that if we call our function on B, it will seamlessly calculate the tilt of the B subtree, but crucially, it will return the sum of all nodes in its subtree (B + D + E). 

We have the same faith that calling C will calculate its tilt and return the sum (C + F + G).

The Link (Meeting Expectation): Once A receives the left sum and right sum, it calculates its local tilt: |left_sum - right_sum|. 
It adds this local tilt to the total running tilt. Finally, A calculates its own sum (left_sum + right_sum + A.data) and returns it upwards so its parent can do the same.

Core Scenarios & Logic
Scenario 1: The "Side-Effect" Strategy: The core problem is that a node needs a sum from its children, but the overall goal is to find the tilt. 
The standard way to solve this in an interview is to let the recursive function return the sum, while the tilt is accumulated as a "side effect" alongside it.

Scenario 2: The Tuple Return (Stateless Optimization): While the video suggests using a global or class-level variable to store the tilt, in a Mid-Senior Python interview, it is significantly better to avoid global state. You can achieve this by returning a tuple (current_sum, accumulated_tilt) at every recursive step.

Specific Edge Cases Discussed
The Null Base Case (Sum Identity): If a node is null, it contributes 0 to the sum and 0 to the tilt. Returning (0, 0) is the mathematical identity required to ensure leaf nodes correctly calculate their tilt as |0 - 0| = 0.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized implementation. By returning a tuple containing both the sum and the tilt, we solve the problem in a single post-order pass. This yields O(N) Time Complexity (visiting every node exactly once) and O(H) Space Complexity (dictated by the recursion stack depth).
"""
