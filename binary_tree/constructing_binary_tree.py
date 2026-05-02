# Maintaining continuity: Core Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Helper class to manage the state machine during construction
class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state


class BinaryTree:
    def __init__(self):
        self.root = None

    def construct_from_array(self, arr):
        # Corner Case: Empty array or null root
        if not arr or arr is None:
            return None

        self.root = Node(arr)
        # Initialize stack with the root node and State 1
        stack = [Pair(self.root, 1)]
        idx = 1

        # Process until the stack is empty
        while len(stack) > 0:
            top = stack[-1]

            # Scenario 1: State 1 -> Process Left Child
            if top.state == 1:
                top.state += 1  # Increment state immediately

                # Edge Case: Check for None to skip node creation
                if idx < len(arr) and arr[idx] is not None:
                    left_node = Node(arr[idx])
                    top.node.left = left_node
                    stack.append(Pair(left_node, 1))
                idx += 1

            # Scenario 2: State 2 -> Process Right Child
            elif top.state == 2:
                top.state += 1  # Increment state immediately

                # Edge Case: Check for None to skip node creation
                if idx < len(arr) and arr[idx] is not None:
                    right_node = Node(arr[idx])
                    top.node.right = right_node
                    stack.append(Pair(right_node, 1))
                idx += 1

            # Scenario 3: State 3 -> Both children processed, pop from stack
            else:
                stack.pop()

        return self.root


# Driver code to test the scenarios
if __name__ == "__main__":
    # Array representation with None (null) representing no children
    data_array = [
        50,
        25,
        12,
        None,
        None,
        37,
        30,
        None,
        None,
        None,
        75,
        62,
        None,
        70,
        None,
        None,
        87,
        None,
        None,
    ]

    tree = BinaryTree()
    root_node = tree.construct_from_array(data_array)

    # root_node now contains the fully constructed tree.


"""
Explanation Notes:

Construction Scenarios & State Machine Logic
To construct a Binary Tree from an array representation (e.g., [50, 25, 12, None, None, 37...]), the video utilizes an iterative approach with a Stack and a State Machine. A Pair object is placed in the stack holding a Node and an integer representing its State.

Here are the specific execution scenarios expected:
State 1 (Attach Left): When the top element's state is 1, you read the next element in the array. If it is a valid value, create a new Node, attach it as the left child of the top node, increment the top node's state to 2, and push the newly created Node onto the stack with a fresh state of 1.

State 2 (Attach Right): When the top element's state is 2, you read the next array element. If valid, create a new Node, attach it as the right child, increment the top node's state to 3, and push the new Node onto the stack with state 1.

State 3 (Pop / Processed): When the top element's state reaches 3, it means both its left and right subtrees have been fully processed. The node is popped from the stack.

Edge Cases & Corner Cases
Encountering None (Null values): If the array value read for a Left (State 1) or Right (State 2) attachment is None, you do not create a node or push anything to the stack. You simply increment the top node's state to move to the next operation, leaving that child pointer as None.

Empty Array / None Root: An implicit edge case to handle in interviews. If the input array is empty or the 0th index is None, the tree cannot be constructed and should return None.

--------------------------------------------------------------------------------
Python Code (Interview Standard)
Continuing from our foundational Node class, here is the highly optimized, interview-ready Python implementation using an explicit Stack to achieve O(N) Time Complexity (traversing the array once) and O(H) Space Complexity (where H is the height of the tree, representing the max depth of the stack).

"""
