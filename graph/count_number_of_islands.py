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

    # ... (Previous methods: get_all_paths, multisolver, is_connected, etc.) ...

    @staticmethod
    def count_islands(grid: list[list[int]]) -> int:
        """
        Counts the number of islands in a 2D grid.
        Note: 0 represents Land, 1 represents Water based on the video's context.

        Time Complexity: O(M * N) - Every cell is processed at most twice.
        Space Complexity: O(M * N) - For the visited set and the recursion call stack.
        """
        if not grid or not grid:
            return 0

        rows = len(grid)
        cols = len(grid)
        visited = set()
        island_count = 0

        def _dfs_virtual(r: int, c: int):
            # Base Case / Corner Cases [6]:
            # 1. Out of bounds
            # 2. Reached water (1)
            # 3. Already visited
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == 1
                or (r, c) in visited
            ):
                return

            # Mark the current land cell as visited [7]
            visited.add((r, c))

            # Expectation-Faith: Explore the 4 implicit neighbors (North, East, South, West) [5, 6]
            _dfs_virtual(r - 1, c)  # North
            _dfs_virtual(r, c + 1)  # East
            _dfs_virtual(r + 1, c)  # South
            _dfs_virtual(r, c - 1)  # West

        # Outer loop to find every disconnected island component [3, 4]
        for i in range(rows):
            for j in range(cols):
                # Trigger a new DFS only if it's unvisited land [4]
                if grid[i][j] == 0 and (i, j) not in visited:
                    _dfs_virtual(i, j)
                    # Once the DFS finishes, one entire island has been mapped [5]
                    island_count += 1

        return island_count


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # 0 represents Land, 1 represents Water
    # Creating a grid that forms exactly 3 distinct islands [2]
    virtual_grid = [[2]]

    print("--- Counting Islands in Virtual Graph ---")

    # Called as a static method directly from the class
    total_islands = Graph.count_islands(virtual_grid)

    print(f"Total Islands Found: {total_islands}")  # Expected: 3


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for the "Count Number of Islands" problem.

Mid-Senior Interview Insight: The "Virtual Graph"
While you requested the Adjacency List implementation, the video explicitly emphasizes that for 2D Grid problems, building a physical Adjacency List is an interview red flag because it wastes O(V+E) space.

Instead, the grid itself acts as a Virtual Graph. 
The adjacency list is implicit: every cell is a vertex, and its connected edges are automatically its North, South, East, and West neighbors. 
For optimal space and time complexity, we traverse the matrix directly. 
I have designed this as a @staticmethod in our Graph class to reflect strict Object-Oriented standards, as it operates independently of our self.adj_list state.

The "Expectation-Faith" Recursive Thought Process:
Expectation: When you encounter an unvisited piece of land (a 0), you expect the DFS function to completely traverse, discover, and mark every connected piece of that single island.

Faith: You have faith that if you blindly call DFS on your 4 directional neighbors (North, South, East, West), they will recursively handle the rest of the island's terrain for you.

Corner Cases & Scenarios to Handle:
Water vs. Land Representation: In this specific video's context, 0 represents Land and 1 represents Water. This is an inverse of standard LeetCode problems, so you must carefully check grid[i][j] == 1 to stop recursion.

Boundary Out of Bounds (Edge Case): 
Before accessing a neighbor, you must verify the indices haven't fallen off the grid (e.g., i < 0 or j >= cols). If they have, you must return immediately to prevent an IndexError. (OutOfBounds Exception)

Already Visited Land: To prevent infinite loops (bouncing between two adjacent 0s), you must track visited cells. The video uses a boolean 2D array. 
In Python, a set of tuples (i, j) is optimal for O(1) lookups.

--------------------------------------------------------------------------------
Python Code: count_islands (Virtual Graph DFS)
Here is the continued Mid-Senior level implementation. I have included the ongoing Graph class structure and added the count_islands method as a static utility, which is exactly how a Senior Engineer would structure a graph library handling both explicit and implicit graphs.
"""
