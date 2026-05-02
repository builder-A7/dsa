class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, traversals, algorithms, transform methods remain here) ...

    # ---------------------------------------------------------
    # SCENARIO: Get Single Child Nodes
    # ---------------------------------------------------------
    def get_single_child_nodes(self, node, parent=None, result=None):
        if result is None:
            result = []

        # Edge Case 1: Reached an empty branch
        if node is None:
            return result

        # Edge Case 2: The Root Parent Trap
        # We MUST ensure parent is not None before evaluating its children
        if parent is not None:
            # Scenario 1: Current node is an only LEFT child
            if parent.left == node and parent.right is None:
                result.append(node.data)

            # Scenario 2: Current node is an only RIGHT child
            elif parent.right == node and parent.left is None:
                result.append(node.data)

        # Recursive Step: The current node becomes the 'parent' for its children
        self.get_single_child_nodes(node.left, node, result)
        self.get_single_child_nodes(node.right, node, result)

        return result


# Driver code to test the scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will return an array of all single children:
    # Expected output: A list of nodes that don't have a sibling
    # print("Single Child Nodes:", tree.get_single_child_nodes(root_node))
    pass


"""
The Recursive Thought Process: Top-Down State Passing
Regarding your special note: This specific video does not use the "Expectation-Faith" (bottom-up) framework.

To determine if a node is an only child, a node cannot figure that out by asking its own children (bottom-up). Instead, it needs information from above. The problem relies on Top-Down State Passing, where the parent node passes a reference to itself down to its children. 

The child then evaluates: "Am I your only child?"
Core Scenarios & Logic
The problem asks us to find and collect all nodes that are the exclusive child of their parent.

Scenario 1: Single Left Child: If the current node is the left child of the passed parent, and the parent's right child is null, the current node is an only child. Record it.

Scenario 2: Single Right Child: If the current node is the right child of the passed parent, and the parent's left child is null, record it.

Recursive Delegation: Regardless of whether the current node is a single child or not, it must continue the search by calling the function on its own children, passing itself as the new parent parameter.

Specific Edge Cases Discussed
The Root Parent Trap (Crucial): When initiating the traversal at the root node, you must pass null (or None) as its parent since it has no ancestor.

The video explicitly warns that if your code blindly checks parent.left or parent.right without first verifying if parent is not None, the program will immediately crash with a Null Pointer Exception on the root node.

The Null Base Case: As always, the function must handle empty branches gracefully with an if node is None: return base case to prevent crashing when reaching the bottom of the tree.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class context, here is the optimized implementation. In standard interviews, you should accumulate these nodes into a list rather than just printing them. This yields O(N) Time Complexity (visiting every node exactly once) and O(H) Space Complexity (dictated by the recursion stack depth, where H is the height of the tree).
"""
