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
        Finds all connected components in the graph.
        Time Complexity: O(V + E) - Every vertex and edge is processed exactly once.
        Space Complexity: O(V) - For the visited set, recursion stack, and output list.
        """
        visited = set()
        all_components = []

        # Helper function to encapsulate the DFS state
        def _dfs(current: int, current_comp: list[int]):
            # Pre-order: Mark as visited and add to the current component
            visited.add(current)
            current_comp.append(current)

            # Expectation-Faith: Ask neighbors to populate the rest of the component
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    _dfs(neighbor, current_comp)

        # Outer loop to handle disconnected islands
        for v in range(self.num_vertices):
            # Corner Case 2: Only trigger a new component if the vertex is untouched
            if v not in visited:
                new_component = []
                _dfs(v, new_component)
                all_components.append(new_component)

        return all_components

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
    # Creating a graph with 3 distinct components:
    # Component 1: 0-1, 1-2, 2-3, 0-3 (Vertices 0,1,2,3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(0, 3)

    # Component 2: 4-5, 5-6, 4-6 (Vertices 4,5,6)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    # Notice we intentionally DID NOT connect (3, 4) or any node between the two groups.
    # We will also add an isolated vertex 7 to test edge cases, meaning we need an 8 vertex graph.
    # Let's adjust the graph size dynamically for the test.
    graph_test = Graph(8)
    graph_test.add_edge(0, 1)
    graph_test.add_edge(1, 2)
    graph_test.add_edge(2, 3)
    graph_test.add_edge(0, 3)
    graph_test.add_edge(4, 5)
    graph_test.add_edge(5, 6)
    graph_test.add_edge(4, 6)
    # Vertex 7 is left completely alone with no edges.

    print("--- Graph Structure ---")
    graph_test.display()

    print("\n--- Connected Components ---")
    components = graph_test.get_connected_components()

    print(f"Total Components Found: {len(components)}")
    for idx, comp in enumerate(components):
        print(f"Component {idx + 1}: {comp}")


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for finding all Connected Components in a graph, adapted to your strict unweighted and undirected constraints.

The Recursive Thought Process & The "Expectation-Faith" Model:

To find connected components, the video uses a combination of an outer loop and the classic DFS "Expectation-Faith" recursion:

Expectation: You are at an unvisited vertex (e.g., 0) and expect the DFS to completely traverse and gather all nodes connected to 0 into a single list (a component).
Faith: You have faith that if you add 0 to the component list and call DFS on its unvisited neighbors, they will recursively traverse their respective sub-graphs and append all reachable nodes into that exact same component list.

Corner Cases & Scenarios to Handle

Fragmented / Disconnected Graphs: A single DFS traversal starting from vertex 0 will only discover the nodes connected to 0. If vertices 4, 5, and 6 form an isolated island, they will be missed.
Solution: You must wrap the DFS in an outer loop that checks every single vertex from 0 to V-1.

Already Visited Nodes (Preventing Duplicates): Because of the outer loop, once vertex 0's DFS finishes, it might have visited 1 and 2. When the outer loop reaches 1, you must strictly skip it. If you don't, you will generate redundant components.

Fully Disconnected Graph (Edge Case): If there are no edges at all, the outer loop will trigger the DFS V times. The result will be V separate components, each containing exactly one vertex.
Fully Connected Graph (Edge Case): The outer loop triggers DFS on node 0, visits everything, and skips the rest. The result is exactly 1 component containing all nodes.

--------------------------------------------------------------------------------
Python Code: get_connected_components (Adjacency List)
Here is the Mid-Senior level implementation. We continue building the exact Graph class from our previous interactions, strictly maintaining the Adjacency List, Undirected, and Unweighted constraints.
"""
