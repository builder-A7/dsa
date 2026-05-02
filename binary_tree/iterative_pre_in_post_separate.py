class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, level_order, unified iterative_traversals remain here) ...

    # ---------------------------------------------------------
    # INDEPENDENT ITERATIVE SPLITS (Highly Optimized)
    # ---------------------------------------------------------

    # SCENARIO 1: Independent Iterative Pre-order
    def iterative_pre_order_split(self, node):
        # Edge Case: Empty tree prevention
        if node is None:
            return []

        stack = [node]
        result = []

        while len(stack) > 0:
            curr = stack.pop()
            result.append(curr.data)

            # SCENARIO: Push Right first so Left is popped first (LIFO)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)

        return result

    # SCENARIO 2: Independent Iterative In-order
    def iterative_in_order_split(self, node):
        stack = []
        result = []
        curr = node  # Explicit pointer needed to traverse deep left

        # SCENARIO: Loop continues if there are unprocessed nodes in stack OR a valid current node
        while len(stack) > 0 or curr is not None:
            if curr is not None:
                # Dive deep into the left branch
                stack.append(curr)
                curr = curr.left
            else:
                # Hit a null leaf: Pop, process, and pivot right
                curr = stack.pop()
                result.append(curr.data)
                curr = curr.right

        return result

    # SCENARIO 3: Independent Iterative Post-order (The Hack)
    def iterative_post_order_split(self, node):
        # Edge Case: Empty tree prevention
        if node is None:
            return []

        stack = [node]
        result = []

        while len(stack) > 0:
            curr = stack.pop()
            result.append(curr.data)

            # SCENARIO: Push Left first so Right is popped first
            # This generates the sequence: Root -> Right -> Left
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)

        # SCENARIO: Reversing the sequence yields: Left -> Right -> Root
        return result[::-1]


# Driver code to test the scenarios
if __name__ == "__main__":
    # Assuming construct_from_array and root_node are set up as before...
    # print("Iterative Pre-order:", tree.iterative_pre_order_split(root_node))
    # print("Iterative In-order:", tree.iterative_in_order_split(root_node))
    # print("Iterative Post-order:", tree.iterative_post_order_split(root_node))
    pass


"""
Iterative Split Scenarios & Standard Interview Logic:

While the video exclusively teaches a unified State-Machine approach (using a Pair of Node and State) to simulate the Euler Tour and extract all three traversals simultaneously, a mid-senior interviewer will look for something different if you are asked to write them as independent functions.

When splitting them, you are expected to drop the Pair state-machine overhead entirely and use highly-optimized, direct stack manipulations. (Note: The specific independent algorithms detailed below represent the industry standard for DSA interviews and go beyond the provided video source material. You may want to independently verify them, but they are exactly what you should write on the whiteboard).

Here are the specific execution scenarios and edge cases for the independent iterative functions:

Iterative Pre-order (Right-First Push Scenario): Because a Stack is Last-In-First-Out (LIFO), if you want to process the left child first, you must push the right child into the stack before the left child.

Iterative In-order (The Pointer Scenario): You cannot rely solely on popping from the stack. You must maintain a curr pointer to dive as deep as possible into the left subtrees. Only when curr hits None do you pop from the stack, process the node, and pivot to the right child.

Iterative Post-order (The Reverse Hack Scenario): Standard iterative post-order is notoriously complex to write with one stack. The most interview-optimized way to solve it is to mirror the Pre-order logic (process node, push left, push right) which generates a Root -> Right -> Left sequence. Once the loop is done, you simply reverse the resulting array to get Left -> Right -> Root.

"""
