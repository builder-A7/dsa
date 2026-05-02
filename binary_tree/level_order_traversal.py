from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # ... (construct_from_array, display, get_size, traversals, etc., remain here) ...

    # SCENARIO: Level Order Traversal (Line by Line)
    def level_order(self, node):
        # Edge Case: If the starting node/root is None, return an empty list
        if node is None:
            return []

        # Space Optimization: deque provides O(1) time complexity for popleft()
        queue = deque([node])
        result = []

        # Outer loop manages the levels until the queue is fully empty
        while queue:
            # SCENARIO: Take a snapshot of how many nodes are in the current level
            level_size = len(queue)
            current_level = []

            # Process exactly 'level_size' nodes to isolate this specific level
            for _ in range(level_size):
                # Step 1: Remove
                curr = queue.popleft()

                # Step 2: Print / Process (Accumulating to our current level array)
                current_level.append(curr.data)

                # Step 3: Add Children
                # Critical Edge Case: Only push non-null children to the queue
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

            # SCENARIO: Line break equivalent. Append the fully processed level to the result.
            result.append(current_level)

        return result


# Driver code to test the level order scenario
if __name__ == "__main__":
    # Example tree setup (Assuming construct_from_array is defined as before)
    # data_array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    # tree = BinaryTree()
    # root_node = tree.construct_from_array(data_array)

    # In an interview, executing this will return:
    # [, [3], [4, 5], [6]]
    # print(tree.level_order(root_node))
    pass


"""
Core Scenarios & "Remove, Print, Add Children" Logic
The video details the Level Order Traversal (Breadth-First Search) using a Queue data structure.

The core algorithm relies on a repeating three-step mantra for every node: Remove, Print, Add Children.

To print each level on a completely separate line (a standard interview requirement), you cannot just blindly process the queue. You must handle the following execution scenarios:
Level Isolation Scenario (The size snapshot): Before removing nodes, you must take a snapshot of the queue's current size (level_size = queue.size()).

You then run a loop exactly level_size times. This isolates the nodes of the current level and prevents you from accidentally processing the children that are actively being added to the back of the queue.

The Line Break Scenario: Once the inner level_size loop finishes, you know the current level is complete, and you execute a line break (Enter) before the outer loop continues to the next level.

Specific Edge Cases Discussed
Null Child Enqueue Prevention: You must explicitly check if node.left and node.right are not null before attempting to add them to the queue.
Pushing null into the queue will break the "Remove, Print, Add" loop on the next iteration because you will attempt to read data from a null object.

--------------------------------------------------------------------------------
Python Code (Interview Standard Integration)
Continuing our BinaryTree class, here is the interview-ready Python implementation.
Optimization Note: In Python, you should never use a standard list as a queue (using pop(0)), because it takes O(N) time to shift elements. For mid-senior interviews, you must use collections.deque which provides O(1) time complexity for popping from the front. Instead of just printing, the standard interview expectation is to return an array of arrays (List[List[int]]).
"""
