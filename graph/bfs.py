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

    # ... (Previous methods: get_all_paths, multisolver, etc. remain here) ...

    def bfs(self, src: int) -> None:
        """
        Executes Breadth-First Search (BFS) to traverse the graph.
        Prints the shortest path to each reachable vertex.

        Time Complexity: O(V + E) - Every vertex and edge is processed at most once.
        Space Complexity: O(V) - For the Queue and the Visited set.
        """
        # Queue stores tuples of (current_vertex, path_so_far_string)
        # Using deque for O(1) pops from the front
        queue = deque([(src, str(src))])
        visited = set()

        while queue:
            # Step 1: Remove (Pop from the front of the queue)
            current, path_so_far = queue.popleft()

            # Step 2: Mark (and Handle Cycles / Corner Case 1)
            # If the node was added to the queue via multiple paths, skip redundant processing
            if current in visited:
                continue
            visited.add(current)

            # Step 3: Work (Format output exactly as requested in the video)
            # Video format prints: Vertex@Path (e.g., 2@012)
            print(f"{current}@{path_so_far}")

            # Step 4: Add (Push unvisited neighbors to the back of the queue)
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path_so_far + str(neighbor)))

    def display(self):
        """Utility to visualize the unweighted Adjacency List."""
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

    print("\n--- Breadth First Traversal (Starting at 2) ---")
    # The video specifically traces the queue behavior starting at Vertex 2
    # Expected Output formatting:
    # 2@2, 1@21, 3@23, 0@210, 4@234, 5@2345, 6@2346
    graph.bfs(src=2)


"""
Here are the problem-solving strategies, edge cases, and the specific algorithmic pattern for Breadth-First Search (BFS), adhering strictly to your unweighted and undirected constraints.

The "Expectation-Faith" Note - 
The video does not use the "Expectation-Faith" recursive thought process for this problem. BFS is an iterative algorithm that explores graphs level-by-level (radius-wise) using a Queue data structure, rather than diving deep using the recursion call stack.

The Problem-Solving Strategy: << "Remove, Mark, Work, Add" >>

To master BFS in an interview, the video introduces a strict 4-step iterative mantra that happens inside the while loop:

Remove: Pop the first element from the front of the Queue.
Mark: Mark the removed element as visited. (Crucial: check if it is already visited first).
Work: Perform your logic (e.g., printing the path, calculating distance).
Add: Push all unvisited neighbors of the current element to the back of the Queue.

Corner Cases & Scenarios to Handle - 
Cycle Prevention (The continue Trap): In a graph, multiple paths can lead to the same vertex. This means a vertex might be pushed into the Queue multiple times before it is finally popped and marked as visited. You must check if the popped vertex is already in the visited set immediately after removing it. If it is, continue (skip) to prevent processing cycles.

Path Tracking (State Coupling): Because BFS is iterative, you cannot rely on a recursion stack to remember "how you got there." The video solves this by creating a custom object (or in Python, a Tuple) that couples the vertex with its path_so_far as it travels through the Queue.

Shortest Path Property: In an unweighted graph, the very first time BFS visits a node, it is guaranteed to be via the shortest possible path (minimum number of edges).

--------------------------------------------------------------------------------
Python Code: bfs (Adjacency List)
Here is the Mid-Senior level implementation. We are seamlessly integrating this into our ongoing Graph class. I have used collections.deque instead of a standard list for the Queue to ensure O(1) time complexity for popleft().
"""
