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

    # ... (Previous methods: get_all_paths, multisolver, count_islands, etc.) ...

    def hamiltonian_path_and_cycle(self, src: int) -> None:
        """
        Finds and prints all Hamiltonian Paths and Cycles starting from `src`.
        Paths are marked with '.' and Cycles are marked with '*'.

        Time Complexity: O(N!) - Exponential, as it explores all permutations.
        Space Complexity: O(V) - For the visited set and the recursion call stack.
        """
        visited = set()

        def _dfs_hamiltonian(current: int, path_so_far: list[int]):
            # Pre-order: Mark the current node as visited and add to path
            visited.add(current)
            path_so_far.append(current)

            # Base Case / Corner Case 4: Have we visited EVERY vertex?
            if len(visited) == self.num_vertices:
                # Corner Case 1: Check for the closing edge to determine Path vs Cycle
                # We check if the original `src` is a neighbor of the `current` (last) vertex
                is_cycle = src in self.adj_list[current]

                # Format output as requested by the video's logic
                path_str = " -> ".join(map(str, path_so_far))
                if is_cycle:
                    print(f"{path_str} (Cycle *)")
                else:
                    print(f"{path_str} (Path .)")
            else:
                # Expectation-Faith: Explore unvisited neighbors
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        _dfs_hamiltonian(neighbor, path_so_far)

            # Post-order / Corner Case 2: Backtrack to explore other permutations
            visited.remove(current)
            path_so_far.pop()

        # Trigger the DFS
        _dfs_hamiltonian(src, [])

    def display(self):
        """Utility to visualize the unweighted Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # The video uses a specific graph structure (Vertices 0 to 6)
    # to demonstrate both paths and cycles.
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
    graph.add_edge(2, 5)  # Additional edge from the video to create complex routes

    print("--- Graph Structure ---")
    graph.display()

    print("\n--- Hamiltonian Paths & Cycles (Starting at Vertex 0) ---")
    graph.hamiltonian_path_and_cycle(src=0)


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for identifying Hamiltonian Paths and Cycles, strictly adhering to your constraints for undirected and unweighted graphs.
The Problem-Solving Strategy: Path vs. Cycle
A Hamiltonian Path is a path that visits every single vertex in the graph exactly once.
 
A Hamiltonian Cycle is a Hamiltonian Path that has one extra property: there is a direct edge connecting the last visited vertex back to the original starting vertex.

The strategy is a direct evolution of the "Find All Paths" backtracking algorithm. Instead of stopping when a specific destination is reached, the base case triggers when the number of visited vertices equals the total number of vertices in the graph. 

At that exact moment, you check for the closing edge to determine if it is a Path or a Cycle.

The "Expectation-Faith" Recursive Thought Process
Expectation: You are at a starting vertex (e.g., 0) and expect the DFS to find all paths that touch every other vertex in the graph without repeating any.
Faith: You have faith that if you mark the current vertex as visited and recursively call DFS on your unvisited neighbors, those neighbors will successfully navigate the rest of the unvisited vertices.

Corner Cases & Scenarios to Handle - 
Cycle Verification (The Closing Edge): The most critical scenario occurs at the base case. Just because you visited all vertices does not mean you have a cycle. You must explicitly check if the original source vertex is in the neighbor list of your current (final) vertex. The video prints a * for cycles and a . for paths.

Mandatory Backtracking: Just like finding all paths, Hamiltonian paths require exploring every possible permutation. When a DFS call returns, you must unmark the current vertex (visited.remove(current)) and pop it from the path tracking array
. If you fail to unmark it, you will only ever find a maximum of one path.
Disconnected Graphs: If the graph is disconnected, or if a vertex is a dead-end that prevents further exploration, the len(visited) == total_vertices condition will simply never be met. The DFS naturally collapses and backtracks without printing invalid paths.
Base Case Timing: A common interview trap is checking the visited size before adding the final node. The cleanest implementation adds the node to the visited set first, checks if the set size equals V, and then evaluates.

--------------------------------------------------------------------------------
Python Code: hamiltonian_path_and_cycle (Adjacency List)
Here is the continued Mid-Senior level implementation. We are integrating this directly into our ongoing Graph class.
"""
