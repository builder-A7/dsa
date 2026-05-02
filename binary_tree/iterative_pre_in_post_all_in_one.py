class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Reusing the Pair class we established during the constructor prompt
class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, level_order, etc., remain here) ...

    # SCENARIO: Iterative Pre, In, and Post Order Traversal in a single pass
    def iterative_traversals(self, node):
        # Edge Case: Empty tree
        if node is None:
            return [], [], []

        pre_order = []
        in_order = []
        post_order = []

        # Initialize stack with the root node and State 1
        stack = [Pair(node, 1)]

        while len(stack) > 0:
            top = stack[-1]

            # SCENARIO 1: State 1 -> Pre-order & Left Descent
            if top.state == 1:
                pre_order.append(top.node.data)
                top.state += 1  # Move to next state

                # Edge Case: Prevent pushing null children
                if top.node.left is not None:
                    stack.append(Pair(top.node.left, 1))

            # SCENARIO 2: State 2 -> In-order & Right Descent
            elif top.state == 2:
                in_order.append(top.node.data)
                top.state += 1  # Move to next state

                # Edge Case: Prevent pushing null children
                if top.node.right is not None:
                    stack.append(Pair(top.node.right, 1))

            # SCENARIO 3: State 3 -> Post-order & Backtrack (Pop)
            else:
                post_order.append(top.node.data)
                stack.pop()

        # Returning all three traversals as a tuple of lists
        return pre_order, in_order, post_order


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will yield the three distinct arrays simultaneously:
    # pre, in_ord, post = tree.iterative_traversals(root_node)
    # print("Pre-order:", pre)
    # print("In-order:", in_ord)
    # print("Post-order:", post)
    pass


"""
Core Scenarios & State Machine Logic
To perform Pre-order, In-order, and Post-order traversals iteratively (without recursion), the video introduces a single unified algorithm using a Stack and a Pair class (containing the Node and an integer State). This approach explicitly simulates the call stack of the recursive Euler Tour.

The execution relies on three specific scenarios based on the node's current state:
Scenario 1 (State == 1 / Pre-order): This is the first time the node is visited. You append the node's data to the Pre-order result, increment its state to 2, and if a left child exists, push it to the stack with a fresh State of 1.

Scenario 2 (State == 2 / In-order): The node is visited after returning from the left subtree. You append the node's data to the In-order result, increment its state to 3, and if a right child exists, push it to the stack with a fresh State of 1.

Scenario 3 (State == 3 / Post-order): The node is visited after both subtrees are processed. You append the node's data to the Post-order result and pop the node from the stack.

Specific Edge Cases Discussed
Null Child Push Prevention: Unlike the recursive approach where base cases handle nulls, the iterative approach requires an explicit edge case check: if top.node.left is not None. You must never push a null node into the stack, as reading its state on the next loop iteration will throw an AttributeError.

Empty Tree: If the root is None initially, the function must immediately return empty lists to prevent stack initialization errors.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the highly optimized iterative traversal. It uses a single stack to process all three traversals simultaneously, yielding O(N) Time Complexity (visiting each node exactly 3 times) and O(H) Space Complexity (where H is the height of the tree, representing the max depth of the stack).
"""
