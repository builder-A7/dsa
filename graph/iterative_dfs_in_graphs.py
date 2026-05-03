class Graph:
    """
    Graph Representation and Utilities Toolkit.
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default, but explicitly supports weights via `add_weighted_edge`.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[tuple[int, int]]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge (Default weight is 0)."""
        self.adj_list[u].append((v, 0))
        self.adj_list[v].append((u, 0))

    def add_weighted_edge(self, u: int, v: int, wt: int) -> None:
        """Adds an undirected edge with an explicitly specified weight."""
        self.adj_list[u].append((v, wt))
        self.adj_list[v].append((u, wt))

    # ... (Previous methods: bfs, dijkstra, topological_sort, etc. remain here) ...

    def iterative_dfs(self, src: int) -> None:
        """
        Executes Depth-First Search iteratively using a Stack.

        Time Complexity: O(V + E) - Every vertex and edge is processed at most once.
        Space Complexity: O(V) - For the Stack and the Visited set.
        """
        # Stack stores tuples of (current_vertex, path_so_far_string)
        # Using a standard list as a LIFO stack
        stack = [(src, str(src))]
        visited = set()

        while stack:
            # Step 1: Remove (Pop from the top/end of the stack)
            current, path_so_far = stack.pop()

            # Step 2: Mark (and Handle Cycles / Corner Case 1)
            # If the node was added to the stack via multiple paths, skip redundant processing
            if current in visited:
                continue

            # Late marking: mark as visited only after popping
            visited.add(current)

            # Step 3: Work (Format output exactly as requested in the video)
            # Video format prints: Vertex@Path (e.g., 2@012)
            print(f"{current}@{path_so_far}")

            # Step 4: Add (Push unvisited neighbors to the top of the stack)
            for neighbor, _ in self.adj_list[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path_so_far + str(neighbor)))

    def display(self):
        """Utility to visualize the Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # Setup 7 vertices (0 to 6)
    graph = Graph(7)

    # Adding unweighted, undirected edges
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    print("--- Graph Structure ---")
    graph.display()

    print("\n--- Iterative Depth First Traversal (Starting at 0) ---")
    # Expected Output format matches BFS but explores depth-first
    graph.iterative_dfs(src=0)


"""
Here are the problem-solving strategies, edge cases, and the specific algorithmic pattern for Iterative Depth First Search (DFS), maintaining your unweighted and undirected constraints.

The "Expectation-Faith" Note -
Because this algorithm relies on a Stack data structure to process nodes iteratively, the recursive "Expectation-Faith" thought process does not apply here.

The Problem-Solving Strategy: "Remove, Mark, Work, Add" (The BFS Twin)
A massive Mid-Senior interview insight highlighted in the video is that Iterative DFS is completely identical to Breadth-First Search (BFS), with only one data structure changed. 

By swapping the Queue (FIFO) for a Stack (LIFO), the traversal naturally dives deep into the graph rather than radiating outward. 

The exact same 4-step mantra is used:

Remove: Pop the element from the top of the Stack.
Mark: Mark the removed element as visited.
Work: Print or process the vertex.
Add: Push all unvisited neighbors of the current element to the top of the Stack.

Corner Cases & Scenarios to Handle -

Late Marking (Cycle Prevention): Exactly like BFS and Dijkstra, Iterative DFS requires "Late Marking". You must check if a vertex is in the visited set after you pop it from the stack, not before adding it. 

Because a graph can have cross-edges, a node might be pushed to the stack multiple times by different neighbors. Late marking ensures it is only processed once.

Order of Traversal Difference: While recursive DFS and iterative DFS both explore depth-first, their natural neighbor processing order is inverted. Because a stack is Last-In-First-Out (LIFO), the last neighbor pushed to the stack will be the first one explored.

--------------------------------------------------------------------------------
Python Code: iterative_dfs (Adjacency List + Stack)
Here is the Mid-Senior level implementation. We are integrating this into our ongoing Graph toolkit. I am using a standard Python list as the Stack, leveraging O(1) append() and pop() operations. Note that we continue to unpack the (neighbor, weight) tuples introduced in the Dijkstra prompt, simply ignoring the weight for this unweighted context.
"""
