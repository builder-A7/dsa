import heapq


class Graph:
    """
    Graph Representation and Utilities Toolkit.
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default, explicitly supports weights via `add_weighted_edge`.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[tuple[int, int]]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append((v, 0))
        self.adj_list[v].append((u, 0))

    def add_weighted_edge(self, u: int, v: int, wt: int) -> None:
        """Adds an undirected edge with an explicitly specified weight."""
        self.adj_list[u].append((v, wt))
        self.adj_list[v].append((u, wt))

    # ... (Previous methods: dijkstra, bfs, is_cyclic, spread_infection, etc. remain here) ...

    def prims(self, src: int = 0) -> None:
        """
        Executes Prim's Algorithm to find the Minimum Spanning Tree (MST).

        Time Complexity: O(E log V) - Standard Min-Heap Prim's performance.
        Space Complexity: O(V + E) - For the Priority Queue and Visited set.
        """
        # Min-Heap stores tuples: (edge_weight, current_vertex, acquiring_vertex)
        # Python's heapq automatically sorts by the first element (edge_weight)

        # Corner Case 1: Initialization with dummy acquiring vertex (-1)
        pq = [(0, src, -1)]
        visited = set()

        while pq:
            # Step 1: Remove the edge with the smallest weight
            edge_weight, current, acquiring = heapq.heappop(pq)

            # Step 2: Mark (Late Marking for Cycle Prevention)
            if current in visited:
                continue
            visited.add(current)

            # Step 3: Work (Format exactly as requested in the video: vertex via acquirer @ weight)
            # We ignore the dummy start node
            if acquiring != -1:
                print(f"{current} via {acquiring} @ {edge_weight}")

            # Step 4: Add unvisited neighbors to the Priority Queue
            for neighbor, weight in self.adj_list[current]:
                if neighbor not in visited:
                    # Crucial Difference: We push ONLY the specific edge_weight,
                    # NOT the accumulated path weight.
                    heapq.heappush(pq, (weight, neighbor, current))

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

    print("--- Graph Structure (Weighted for MST) ---")
    graph.display()

    print("\n--- Prim's Minimum Spanning Tree (Starting at 0) ---")
    # Expected Output formatting based on the video:
    # 1 via 0 @ 10
    # 2 via 1 @ 10
    # 3 via 2 @ 10
    # 4 via 3 @ 2
    # 5 via 4 @ 3
    # 6 via 5 @ 3
    # (Notice it entirely avoids the expensive 0-3 (40) and 4-6 (8) edges to prevent cycles)
    graph.prims(src=0)


"""
Here are the problem-solving strategies, edge cases, and the specific algorithmic pattern for Prim's Algorithm to find a Minimum Spanning Tree (MST).
Because MST strictly calculates the minimum cost to connect all nodes, edge weights are explicitly specified and required.

The "Expectation-Faith" Note -
Prim's Algorithm operates iteratively using a Priority Queue (Min-Heap). Therefore, the recursive DFS "Expectation-Faith" thought process does not apply here.

The Problem-Solving Strategy: "Remove, Mark, Work, Add" (The Dijkstra Variant)
Prim's algorithm shares the exact same 4-step "Remove, Mark, Work, Add" structure as Dijkstra's Algorithm. 

However, there is one crucial Mid-Senior distinction you must mention in an interview:
Dijkstra evaluates paths based on the Accumulated Weight from the source to the destination.
Prim's evaluates the Individual Edge Weight required to acquire the next unvisited vertex into the growing spanning tree. You do not add previous weights together.

Corner Cases & Scenarios to Handle -
The Dummy Start Node (Acquiring Vertex): To kick off the algorithm, you insert the starting vertex into the Priority Queue. But since no node "acquired" it, the video uses a dummy acquiring vertex -1 with a weight of 0. 

During the "Work" step, you must check if acquiring_vertex != -1 before evaluating or printing the edge to ensure the dummy edge isn't treated as part of the actual MST.

Cycle Prevention (Late Marking): Exactly like BFS and Dijkstra, multiple nodes in the growing MST might try to "acquire" the same unvisited neighbor at different costs. 

When you pop an element from the Min-Heap, you must check if it is already in the visited set immediately. If it is, continue to prevent forming a cycle.

Spanning Tree Properties: By definition, an MST must be acyclic and connect all vertices. If a graph is disconnected, Prim's will only find the Minimum Spanning Forest for the component containing the starting vertex. (The video assumes a connected graph).

--------------------------------------------------------------------------------
Python Code: prims (Adjacency List)
To maintain continuity, we are inserting this method into our existing Graph toolkit. We use the explicitly weighted edge method we introduced for Dijkstra.
"""
