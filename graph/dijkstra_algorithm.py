import heapq


class Graph:
    """
    Graph Representation and Utilities Toolkit.
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default, but explicitly supports weights via `add_weighted_edge`.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # We now store tuples of (neighbor, weight) to accommodate explicit weights
        self.adj_list: list[list[tuple[int, int]]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge (Default weight is 0)."""
        self.adj_list[u].append((v, 0))
        self.adj_list[v].append((u, 0))

    def add_weighted_edge(self, u: int, v: int, wt: int) -> None:
        """Adds an undirected edge with an explicitly specified weight."""
        self.adj_list[u].append((v, wt))
        self.adj_list[v].append((u, wt))

    # ... (Previous methods: get_all_paths, bfs, is_cyclic, etc. adapted to ignore tuple weights) ...

    def dijkstra(self, src: int) -> None:
        """
        Executes Dijkstra's Algorithm to find the shortest path in weights
        from the source to all reachable vertices.

        Time Complexity: O(E log V) - Standard Min-Heap Dijkstra performance.
        Space Complexity: O(V + E) - For the Priority Queue and Visited set.
        """
        # Min-Heap stores tuples: (weight_so_far, current_vertex, path_so_far)
        # Python's heapq automatically sorts by the first element of the tuple (weight_so_far)
        pq = [(0, src, str(src))]
        visited = set()

        while pq:
            # Step 1: Remove the path with the smallest accumulated weight
            weight_so_far, current, path_so_far = heapq.heappop(pq)

            # Step 2: Mark (Late Marking for Cycle & Redundancy Prevention)
            if current in visited:
                continue
            visited.add(current)

            # Step 3: Work (Format exactly as requested in the video: vertex via path @ weight)
            print(f"{current} via {path_so_far} @ {weight_so_far}")

            # Step 4: Add unvisited neighbors to the Priority Queue
            for neighbor, edge_weight in self.adj_list[current]:
                if neighbor not in visited:
                    # Accumulate the weight for the new path
                    heapq.heappush(
                        pq,
                        (
                            weight_so_far + edge_weight,
                            neighbor,
                            path_so_far + str(neighbor),
                        ),
                    )

    def display(self):
        """Utility to visualize the weighted Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # Setup 7 vertices (0 to 6)
    graph = Graph(7)

    # Adding EXPLICITLY weighted, undirected edges as defined in the video
    graph.add_weighted_edge(0, 1, 10)
    graph.add_weighted_edge(1, 2, 10)
    graph.add_weighted_edge(2, 3, 10)
    graph.add_weighted_edge(0, 3, 40)
    graph.add_weighted_edge(3, 4, 2)
    graph.add_weighted_edge(4, 5, 3)
    graph.add_weighted_edge(5, 6, 3)
    graph.add_weighted_edge(4, 6, 8)

    print("--- Graph Structure (Weighted) ---")
    graph.display()

    print("\n--- Dijkstra's Algorithm (Source: 0) ---")
    # Expected Output formatting based on the video:
    # 0 via 0 @ 0
    # 1 via 01 @ 10
    # 2 via 012 @ 20
    # 3 via 0123 @ 30 (Notice it avoids the 0-3 edge which costs 40)
    # 4 via 01234 @ 32
    # 5 via 012345 @ 35
    # 6 via 0123456 @ 38 (Notice it avoids the 4-6 edge which costs 40)
    graph.dijkstra(src=0)


"""
Here are the problem-solving strategies, edge cases, and the specific algorithmic pattern for Dijkstra's Algorithm.
Because Dijkstra explicitly calculates the "Shortest Path in Weights", edge weights are explicitly specified and required for this algorithm.

The "Expectation-Faith" Note -
Dijkstra's Algorithm operates iteratively using a Priority Queue (Min-Heap) rather than Depth-First Search (DFS) using recursion. Therefore, the recursive "Expectation-Faith" thought process does not apply here.

The Problem-Solving Strategy: "Remove, Mark, Work, Add" (Priority Queue)
Dijkstra's algorithm is structurally identical to Breadth-First Search (BFS). However, instead of a standard Queue, it uses a Priority Queue to continually explore the path with the smallest accumulated weight.
 
The mantra remains the same:
Remove: Pop the path with the minimum total weight from the Priority Queue.
Mark: Mark the removed vertex as visited.
Work: Print the vertex, its path, and its total weight.
Add: Push all unvisited neighbors into the Priority Queue, accumulating the weight.

Corner Cases & Scenarios to Handle -

Redundant Paths (The "Late Marking" Trap): Because multiple paths can lead to the same vertex with different weights, a vertex might be pushed into the Priority Queue multiple times before it is processed. You must check if the vertex is already visited immediately after popping it (Late Marking). If it is visited, you continue (skip) to prevent infinite cycles and redundant processing.

Shortest Path Guarantee: The fundamental property of Dijkstra is that the very first time a vertex is popped from the Min-Heap, it is guaranteed to be via the absolute shortest weighted path. 

Any subsequent times that vertex is popped (via longer paths), the "Late Marking" check will safely discard it.

Object/Tuple Construction: You cannot just store the vertex in the Priority Queue. You must store a coupled state containing the current_vertex, path_so_far, and weight_so_far. The Priority Queue must be configured to sort primarily by weight_so_far.

--------------------------------------------------------------------------------
Python Code: dijkstra (Adjacency List)
To maintain continuity with our overarching Graph class while accommodating your constraint ("NO edge weights unless explicitly specified"), I have added an add_weighted_edge method specifically for algorithms like Dijkstra that explicitly require weights.
"""
