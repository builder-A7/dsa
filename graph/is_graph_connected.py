class Graph:
    """
    Graph Representation using Adjacency List (Array of Lists).
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def get_connected_components(self) -> list[list[int]]:
        """
        Gathers all isolated components in the graph.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        all_components = []

        def _dfs(current: int, current_comp: list[int]):
            visited.add(current)
            current_comp.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    _dfs(neighbor, current_comp)

        for v in range(self.num_vertices):
            if v not in visited:
                new_component = []
                _dfs(v, new_component)
                all_components.append(new_component)

        return all_components

    def is_connected(self) -> bool:
        """
        Determines if the entire graph is a single connected entity.
        Time Complexity: O(V + E) - Defers to get_connected_components.
        Space Complexity: O(V)
        """
        # Corner case handling for an empty graph
        if self.num_vertices == 0:
            return True

        # A graph is connected if and only if it has exactly 1 component
        return len(self.get_connected_components()) == 1

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

    # 1. Building a FULLY CONNECTED graph
    # Left Subgraph
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(0, 3)
    # Right Subgraph
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)
    # The "Bridge" Edge connecting Left and Right
    graph.add_edge(3, 4)

    print("--- Scenario 1: Fully Connected Graph ---")
    print(f"Is Graph Connected? {graph.is_connected()}")  # Expected: True

    # 2. Building a DISCONNECTED graph by simulating the removal of the Bridge Edge
    # We will instantiate a fresh graph without the (3, 4) edge.
    disconnected_graph = Graph(7)

    # Left Subgraph
    disconnected_graph.add_edge(0, 1)
    disconnected_graph.add_edge(1, 2)
    disconnected_graph.add_edge(2, 3)
    disconnected_graph.add_edge(0, 3)
    # Right Subgraph
    disconnected_graph.add_edge(4, 5)
    disconnected_graph.add_edge(5, 6)
    disconnected_graph.add_edge(4, 6)
    # Notice: NO edge between 3 and 4

    print("\n--- Scenario 2: Disconnected Graph (Bridge Edge Removed) ---")
    print(f"Is Graph Connected? {disconnected_graph.is_connected()}")


"""
Here are the problem-solving strategies and edge cases for determining if a graph is completely connected, strictly adhering to your constraints for unweighted and undirected graphs.

The Problem-Solving Strategy
The video introduces a highly optimized Mid-Senior level interview trick: Do not write a new algorithm from scratch.

Instead, reuse the get_connected_components() logic we built previously.

If a graph is fully connected, every vertex can reach every other vertex. 
Therefore, gathering all components will result in exactly 1 large component containing all vertices.

If the graph is disconnected, it will yield more than 1 component.

The logic simply becomes: return len(self.get_connected_components()) == 1.

The "Expectation-Faith" Recursive Thought Process
Because this approach directly calls the get_connected_components() method, it relies entirely on the exact same Expectation-Faith DFS framework we established in the previous prompt. No new recursive logic is needed.

Corner Cases & Scenarios to Handle -
Bridge Edges vs. Non-Bridge Edges:
Removing an edge that is part of a cycle (e.g., an edge between 4 and 5 in a triangle of 4-5-6) will not disconnect the graph. It remains 1 component.

Removing a "bridge" edge (e.g., the singular edge 3-4 connecting a left-side subgraph to a right-side subgraph) will instantly shatter the graph into 2 separate components, making it disconnected.

Graph with 0 or 1 Vertices (Edge Case): A graph with 0 vertices will return 0 components. Depending on the exact strictness of the interviewer, a 0-vertex graph might be considered vacuously connected or invalid. Our logic checks for strictly == 1.

--------------------------------------------------------------------------------
Python Code: is_connected (Adjacency List)
Here is the continued Mid-Senior level implementation. I have included the required prerequisite get_connected_components method so the class remains whole and functional.
"""
