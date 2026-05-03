from collections import deque


class Graph:
    """
    Graph Representation and Utilities Toolkit.
    - Context: UNDIRECTED and UNWEIGHTED by default.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # ... (Previous methods: bfs, get_all_paths, multisolver, etc. remain here) ...

    def is_cyclic(self) -> bool:
        """
        Determines if the graph contains at least one cycle using BFS.

        Time Complexity: O(V + E) - Every vertex and edge is processed at most once.
        Space Complexity: O(V) - For the Queue and Visited set.
        """
        visited = set()

        def _bfs_cycle_check(start: int) -> bool:
            # Queue stores the vertex to evaluate
            queue = deque([start])

            while queue:
                # Step 1: Remove
                current = queue.popleft()

                # Step 2: Mark & Evaluate (The Core Logic)
                # If the vertex is already visited when popped, a cycle exists
                if current in visited:
                    return True

                # Late marking: mark as visited only after popping
                visited.add(current)

                # Step 3 & 4: Work & Add Unvisited Neighbors
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            return False

        # Corner Case 1: Outer loop to handle disconnected components
        for v in range(self.num_vertices):
            if v not in visited:
                # If any component has a cycle, the entire graph is considered cyclic
                if _bfs_cycle_check(v):
                    return True

        return False

    def display(self):
        """Utility to visualize the unweighted Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # Scenario 1: Cyclic Graph
    graph_cyclic = Graph(7)
    graph_cyclic.add_edge(0, 1)
    graph_cyclic.add_edge(1, 2)
    graph_cyclic.add_edge(2, 3)
    graph_cyclic.add_edge(0, 3)  # This edge creates the cycle (0-1-2-3-0)
    graph_cyclic.add_edge(3, 4)
    graph_cyclic.add_edge(4, 5)
    graph_cyclic.add_edge(5, 6)
    graph_cyclic.add_edge(4, 6)  # This edge creates a second cycle (4-5-6-4)

    print("--- Scenario 1: Cyclic Graph ---")
    print(f"Contains Cycle: {graph_cyclic.is_cyclic()}")  # Expected: True

    # Scenario 2: Acyclic Graph (Tree)
    graph_acyclic = Graph(7)
    graph_acyclic.add_edge(0, 1)
    graph_acyclic.add_edge(1, 2)
    graph_acyclic.add_edge(2, 3)
    # Edge 0-3 omitted to prevent cycle
    graph_acyclic.add_edge(3, 4)
    graph_acyclic.add_edge(4, 5)
    graph_acyclic.add_edge(5, 6)
    # Edge 4-6 omitted to prevent cycle

    print("\n--- Scenario 2: Acyclic Graph ---")
    print(f"Contains Cycle: {graph_acyclic.is_cyclic()}")  # Expected: False


"""
Here are the problem-solving strategies, edge cases, and the specific Breadth-First Search (BFS) algorithmic pattern for detecting cycles in a graph, adhering strictly to your unweighted and undirected constraints.

The "Expectation-Faith" Note - 

Because this algorithm relies on Breadth-First Search (BFS) using a Queue rather than Depth-First Search (DFS) using recursion, the "Expectation-Faith" recursive thought process does not apply here.

The Problem-Solving Strategy: The "Popped Twice" Rule -

The video uses a brilliant and simple application of the "Remove, Mark, Work, Add" BFS mantra to detect cycles. In this specific BFS flavor, you only add unvisited neighbors to the Queue. If a graph is just a straight line (no cycles), every vertex will enter the Queue exactly once. However, if there is a cycle, two different paths will eventually discover the same unvisited vertex and both will push it into the Queue.

The logic becomes incredibly straightforward: When you pop a vertex from the front of the Queue (Remove), check if it is already marked as visited.
If it is, you have found a cycle. Return True.

Corner Cases & Scenarios to Handle - 
Disconnected Components (The Hidden Cycle): A single BFS traversal starting from vertex 0 will only check the component connected to 0. If vertices 4, 5, and 6 form an isolated triangle (cycle), a basic BFS will miss it.

Solution: You must wrap your BFS logic in an outer loop that iterates through every vertex. 
If the vertex is unvisited, trigger a new BFS cycle check.

Parent Tracking vs. Late Marking - 
In standard DFS cycle detection, you must explicitly track the "parent" vertex to avoid falsely identifying the edge you just walked across as a cycle. The video's BFS approach brilliantly bypasses this by practicing Late Marking—marking the node as visited after it is popped, rather than when it is added to the Queue. This allows the cycle check (if current in visited) to naturally handle undirected back-and-forth edges without extra parent-tracking variables.

--------------------------------------------------------------------------------
Python Code: is_cyclic (Adjacency List + BFS)
Here is the Mid-Senior level implementation. We continue building upon our existing Graph toolkit. I have encapsulated the BFS logic inside a helper function to easily manage the disconnected components loop.
"""
