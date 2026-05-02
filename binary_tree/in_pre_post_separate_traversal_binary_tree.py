class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, get_size, get_sum, get_max, get_height, traversals remain here) ...

    # SCENARIO 1: Pre-order Split
    def pre_order(self, node, result=[]):

        # Critical Edge Case: Base condition for null children
        if node is None:
            return result

        # Process Left Side (Before recursion)
        result.append(node.data)
        self.pre_order(node.left, result)
        self.pre_order(node.right, result)

        return result

    # SCENARIO 2: In-order Split
    def in_order(self, node, result=[]):

        # Critical Edge Case: Base condition for null children
        if node is None:
            return result

        self.in_order(node.left, result)
        # Process Between Calls (After left, before right)
        result.append(node.data)
        self.in_order(node.right, result)

        return result

    # SCENARIO 3: Post-order Split
    def post_order(self, node, result=[]):

        # Critical Edge Case: Base condition for null children
        if node is None:
            return result

        self.post_order(node.left, result)
        self.post_order(node.right, result)
        # Process Right Side (After full recursion)
        result.append(node.data)

        return result


# Driver code to test the split scenarios
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, you would execute and return arrays like this:
    # print(f"Pre-order List: {tree.pre_order(root_node)}")
    # print(f"In-order List: {tree.in_order(root_node)}")
    # print(f"Post-order List: {tree.post_order(root_node)}")
    pass


"""
Split Traversal Scenarios & Logic
The video explicitly categorizes the three traversals based on where the node sits in the execution flow of the recursion (the Euler Tour). 

When splitting them into individual functions, the structural scenarios are as follows:
Pre-order (Root, Left, Right): The node is processed immediately upon visitation (the "left side" of the node). The root is always the very first element processed.

In-order (Left, Root, Right): The node is processed strictly between the completion of the left subtree and the start of the right subtree.
Post-order (Left, Right, Root): The node is processed only after both left and right subtrees are fully resolved (the "right side" of the node).

Specific Edge Cases
The Null Base Case: For all three individual traversals, blindly calling node.left or node.right will result in an exception when reaching leaf nodes. The explicit edge case handling (if node is None: return) must be the first line of every split function.

For a mid-senior DSA interview, simply printing the values is rarely accepted. Interviewers expect you to accumulate and return the elements in an array/list. Here is the split implementation continuing our BinaryTree class, optimized to return lists without relying on global variables.
"""
