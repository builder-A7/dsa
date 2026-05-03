class Graph:
    """
    Graph Representation using Adjacency List (Array of Lists).
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Array of lists (Adjacency List)
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def get_all_paths(self, src: int, dest: int) -> list[list[int]]:
        """
        Uses DFS Backtracking to find ALL paths from src to dest.
        Time Complexity: Exponential O(V!) in the worst-case complete graph,
                         but practically proportional to the number of paths.
        Space Complexity: O(V) for the visited set, path array, and recursion stack.
        """
        all_paths = []
        visited = set()

        # Helper function to encapsulate the recursive state
        def _dfs_backtrack(current: int, path_so_far: list[int]):
            # Base Case / Scenario 2: Reached the destination
            if current == dest:
                # We found a path. Append a COPY of the current path_so_far.
                all_paths.append(list(path_so_far))
                return

            # Pre-order: Mark the current node as visited (prevent cycles)
            visited.add(current)

            # Expectation-Faith: Ask all neighbors
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    # Add neighbor to path before recursing
                    path_so_far.append(neighbor)

                    # Faith: Let the neighbor explore all its routes
                    _dfs_backtrack(neighbor, path_so_far)

                    # Backtrack (Path): Remove neighbor after exploring
                    path_so_far.pop()

            # Post-order / Scenario 1: The crucial unmarking step
            # Remove the visited mark so other paths can use this vertex later
            visited.remove(current)

        # Initialize the recursion with the source node
        _dfs_backtrack(src, [src])
        return all_paths

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

    # Adding unweighted, undirected edges as defined in the video
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    print("--- Graph Structure ---")
    graph.display()

    print("\n--- DFS All Paths Finding ---")
    # Test finding all paths from 0 to 6
    # The video outputs 4 paths: 0123456, 012346, 03456, 0346
    paths = graph.get_all_paths(0, 6)

    print(f"Total paths found: {len(paths)}")
    for p in paths:
        print(p)


"""
Here are the problem-solving strategies, edge cases, and the recursive thought process for finding all possible paths using Depth First Search (DFS), maintaining your strict unweighted and undirected constraints.

The Recursive Thought Process & The "Expectation-Faith" Model:
While the explicit words "Expectation-Faith" are mostly a callback to the previous foundation, the video extends this exact recursive framework for backtracking:
Expectation: You are at a source vertex (0) and expect to find every valid path to the destination (6)
.
Faith: You have faith that if you ask your unvisited neighbors (1 and 3), they will discover all paths from themselves to 6 and append them to the "path so far"
.
The Crucial Addition (Backtracking): To find all paths, you cannot permanently block off a vertex once visited. Example from the video: If you travel 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6, you found one path. When you step back (backtrack) from 5 to 4, you must unmark 5 as visited
. This ensures that if another route reaches 5 later, it is still allowed to pass through
.
Corner Cases & Scenarios to Handle
Backtracking (Unmarking Visited Nodes): This is the most critical difference between finding one path and all paths. You must mark a node as visited on the way down (Pre-order) to prevent infinite cyclic loops, but you must remove the visited mark on the way back up (Post-order)
.
Base Case Match: When source == destination, a valid path is formed. Record the path, but do not terminate the entire process—you merely return to the previous caller to continue exploring other branches
.
Dead Ends: If all neighbors are either visited or lead to dead ends, the function naturally resolves and falls back up the call stack, unmarking the node as it exits
.

--------------------------------------------------------------------------------
Python Code: DFS get_all_paths (Adjacency List + Backtracking)
For a Mid-Senior interview, returning a list of paths (Lists of integers) is the industry standard over simply printing them as a string (which the video does)
. The below implementation uses standard Backtracking.
"""
