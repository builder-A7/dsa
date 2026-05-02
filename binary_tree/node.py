class Node:
    def __init__(self, data):
        self.data = data
        # Pointers are initialized to None by default
        self.left = None
        self.right = None

# Building the tree and handling the specific scenarios discussed:
if __name__ == "__main__":
    # Root Node
    root = Node(50)
    
    # Scenario 1: Node with 2 children
    # Both left and right pointers are explicitly set to new nodes.
    root.left = Node(30)
    root.right = Node(70)
    
    # Scenario 2: Node with 1 child (Right child only)
    # The right pointer is set, while the left pointer is left as None.

    # THIS IS SO MUCH LIKE LINKED LISTS - .left.right, .next.next, .next.next.next -> Good way to visualize!
    root.left.right = Node(40) 
    
    # Scenario 3: Node with 1 child (Left child only)
    # The left pointer is set, while the right pointer is left as None.
    root.right.left = Node(60)

    # Scenario 4: Leaf Node (0 children)
    # Nodes like '40' and '60' currently have both left = None and right = None.