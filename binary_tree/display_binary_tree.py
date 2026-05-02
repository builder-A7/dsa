# Maintaining Continuity: Complete Binary Tree Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Pair:
    def __init__(self, node, state):
        self.node = node
        self.state = state


class BinaryTree:
    def __init__(self):
        self.root = None

    def construct_from_array(self, arr):
        # Corner Case: Empty array
        if not arr:
            return None

        self.root = Node(arr)
        stack = [Pair(self.root, 1)]
        idx = 1

        while stack:
            top = stack[-1]

            if top.state == 1:
                top.state += 1
                if idx < len(arr) and arr[idx] is not None:
                    top.node.left = Node(arr[idx])
                    stack.append(Pair(top.node.left, 1))
                idx += 1
            elif top.state == 2:
                top.state += 1
                if idx < len(arr) and arr[idx] is not None:
                    top.node.right = Node(arr[idx])
                    stack.append(Pair(top.node.right, 1))
                idx += 1
            else:
                stack.pop()

        return self.root

    # NEW: The Display Logic discussed in the video
    def display(self, node):
        # CRITICAL EDGE CASE: Base condition to prevent AttributeError on leaf nodes
        if node is None:
            return

        # Scenario formatting: Use actual data if child exists, otherwise use "."
        left_str = str(node.left.data) if node.left else "."
        right_str = str(node.right.data) if node.right else "."

        # Print the current node's immediate family
        print(f"{left_str} <- {node.data} -> {right_str}")

        # Recursive delegation to children
        self.display(node.left)
        self.display(node.right)


# Driver code demonstrating the entire flow
if __name__ == "__main__":
    # The exact array structure provided in the video examples
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

    # Trigger the display recursively starting from the root
    tree.display(root_node)


"""
Display Strategy & Edge Cases
To display a binary tree efficiently, the video employs a Recursive Family Printing strategy. Instead of printing everything at once, each node is only responsible for printing its immediate family (itself, its left child, and its right child) and then delegating the exact same task to its left and right children.

Here are the specific execution scenarios and edge cases expected in an interview:
Null Child Formatting (The Dot .): If a node lacks a left or right child, it must gracefully print a dot (.) in its place to visually represent the missing branch.

The Crucial Edge Case (Null Pointer Prevention): The video explicitly demonstrates that blindly making recursive calls (display(node.left) and display(node.right)) without checking for null will crash the program when it attempts to read the data of a missing child.

The Fix (Base Case): The first line of your recursive function must be an explicit check: if node is None: return. This allows you to write clean recursive calls without wrapping them in complex if-else blocks, safely bouncing back when hitting a dead end.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Here is the complete, integrated class continuing from our previous setup. The display method leverages Python's f-strings and inline ternary operators for clean, readable, and highly optimized string formatting.
"""
