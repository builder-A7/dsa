class Graph:
    """
    Graph Representation using Adjacency List (Array of Lists).
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Array of lists as requested (Adjacency List)
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def has_path(self, src: int, dest: int, visited: set) -> bool:
        """
        Uses Depth First Search (DFS) to determine if a path exists.
        Time Complexity: O(V + E)
        Space Complexity: O(V) for the visited set and recursion call stack.
        """
        # Base Case / Corner Case 1: Source is the destination
        if src == dest:
            return True

        # Mark the current node as visited to prevent cyclic infinite loops
        visited.add(src)

        # Expectation-Faith: Ask neighbors if they have a path to the destination
        for neighbor in self.adj_list[src]:
            # Corner Case 2: Only visit unvisited neighbors
            if neighbor not in visited:
                # Faith: If the neighbor finds a path, bubble up the True result
                if self.has_path(neighbor, dest, visited):
                    return True

        # Corner Case 3: Dead end. All neighbors checked, no path found.
        return False

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

    print("\n--- DFS Path Finding ---")
    # Test path from 0 to 6 (Expected: True)
    print(f"Path from 0 to 6 exists: {graph.has_path(0, 6)}")

    # Let's test a scenario where a path doesn't exist
    # By artificially creating an isolated vertex 7 (if we expanded the graph to 8 vertices)
    # But for the current 0-6 graph, let's just confirm it works:
    print(f"Path from 1 to 5 exists: {graph.has_path(1, 5)}")


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for finding a path using Depth First Search (DFS), adapted to your strict unweighted and undirected constraints.

# The "Expectation-Faith" Recursive Thought Process

To master DFS on graphs, the video uses the Expectation-Faith (High-Level) recursive framework:

Expectation: You are at a source vertex (e.g., 0) and you want to know if there is a path to the destination (e.g., 6).

Faith: You have faith in your direct neighbors. The neighbors of 0 are 1 and 3. 
You ask them: "Do you have a path to 6?".

Resolution: If neighbor 1 or neighbor 3 returns True (meaning they found a path to 6), then vertex 0 definitely has a path to 6 through them. You return True immediately.

Corner Cases & Scenarios to Handle
Infinite Loops (Cycles): Because graphs are undirected, 0 connects to 1, and 1 connects back to 0. Without a mechanism to track where you have been, the recursive calls will bounce between 0 and 1 infinitely, causing a Stack Overflow.

Solution: You must mark the current vertex as visited immediately upon entry, and only make a recursive call to a neighbor if it has not been visited.

Base Case (Immediate Match): If the source is exactly the same as the destination (e.g., you are at 6 looking for 6), the path length is 0, but a path does exist. You must return True immediately.

Dead Ends: If you iterate through all neighbors of a vertex and none of them return True, you have hit a dead end. You must return False after the loop exhausts.

--------------------------------------------------------------------------------
Python Code: DFS has_path (Adjacency List)
To maintain continuity with our overarching goal while strictly adhering to your new constraints (Undirected, Unweighted, and explicitly reverting to the Adjacency List from the video as requested in Special Note 2), here is the Mid-Senior level implementation.

Note: I am using a Python set for the visited tracker instead of the boolean array from the Java video. A set is the Pythonic standard for O(1) lookups and prevents the need to pass the graph size down the recursion tree.
"""
