class Graph:
    """
    Highly Optimized Graph Representation using an Adjacency Map (Dict of Dicts).
    - Vertices are stored as keys in a dictionary.
    - Edges are stored as a nested dictionary: { neighbor_vertex : weight }

    Time Complexities (Average):
    - Add Vertex: O(1)
    - LookUp Vertex: O(1)
    - Add/Update Edge: O(1)
    - LookUp Edge: O(1)
    - Remove Edge: O(1)
    - Remove Vertex: O(V) - Must remove incoming edges from other vertices.
    """

    def __init__(self):
        # Dictionary to map vertex -> {neighbor: weight}
        self.adj_map: dict[int, dict[int, int]] = {}

    def add_vertex(self, v: int) -> None:
        """Adds a vertex to the graph in O(1) time."""
        if v not in self.adj_map:
            self.adj_map[v] = {}

    def lookup_vertex(self, v: int) -> bool:
        """Checks if a vertex exists in O(1) time."""
        return v in self.adj_map

    def add_edge(self, u: int, v: int, wt: int, is_directed: bool = False) -> None:
        """Adds or updates an edge in O(1) time."""
        # Ensure vertices exist (corner case handling)
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_map[u][v] = wt
        if not is_directed:
            self.adj_map[v][u] = wt

    def lookup_edge(self, u: int, v: int) -> bool:
        """Checks if an edge exists in O(1) time."""
        return u in self.adj_map and v in self.adj_map[u]

    def remove_edge(self, u: int, v: int, is_directed: bool = False) -> None:
        """Removes an edge in O(1) time."""
        if self.lookup_edge(u, v):
            del self.adj_map[u][v]

        if not is_directed and self.lookup_edge(v, u):
            del self.adj_map[v][u]

    def remove_vertex(self, v: int) -> None:
        """
        Removes a vertex and all its connected edges.
        Time Complexity: O(V) because we must remove references from neighbors.
        """
        if v not in self.adj_map:
            return

        # 1. Remove references to `v` from all its neighbors
        for neighbor in self.adj_map[v]:
            if v in self.adj_map[neighbor]:
                del self.adj_map[neighbor][v]

        # 2. Completely delete the vertex `v`
        del self.adj_map[v]

    def display(self):
        """Utility to visualize the Adjacency Map."""
        for vertex, edges in self.adj_map.items():
            # Formatting to show (Neighbor @ Weight) to match previous output
            formatted_edges = [f"({nbr} @ {wt})" for nbr, wt in edges.items()]
            print(f"Vertex {vertex} -> {formatted_edges}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    graph = Graph()

    # Adding edges as described in the video [3, 4]
    # (Source, Neighbor, Weight)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 3, 40)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 3, 10)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 5, 3)
    graph.add_edge(5, 6, 3)
    graph.add_edge(4, 6, 8)

    print("--- Initial Graph ---")
    graph.display()

    print("\n--- O(1) Operations ---")
    print(f"Lookup edge 0->1: {graph.lookup_edge(0, 1)}")  # Expected: True

    graph.remove_edge(0, 1)
    print(
        f"Lookup edge 0->1 after removal: {graph.lookup_edge(0, 1)}"
    )  # Expected: False

    print("\n--- Graph after removing Vertex 3 ---")
    graph.remove_vertex(3)
    graph.display()


"""
According to the provided material, the Adjacency List (implemented as an array of lists containing edges) is presented as the "proper implementation" because it efficiently manages space. It avoids the massive O(V ^ 2 ) memory waste of an Adjacency Matrix, which becomes completely unviable if a graph has more than 10,000 vertices.

However, to address your specific questions about achieving the absolute lowest time complexity for dynamic operations like vertex/edge removals and lookups, I must include information from outside of the given sources, which you may want to independently verify. The provided sources only cover the basic Adjacency Matrix and Adjacency List (Array of Lists).

Is the Array of Lists the MOST optimal?
For a Mid-Senior interview, a standard Adjacency List (Array of Lists) is optimal for Space Complexity O(V+E) and Graph Traversals (like BFS/DFS). However, it is not optimal for targeted lookups and deletions. In an Array of Lists, checking if a specific edge exists (lookUp edge) or removing an edge (remove edge) takes O(K) time (where K is the degree of the vertex), because you must linearly search through the vertex's list of neighbors.

What is the Most Optimal Data Structure?
If the interview focuses heavily on modifying the graph dynamically, the most optimal data structure is an Adjacency Map (A Hash Map of Hash Maps / Dictionary of Dictionaries). By using Hash Maps, add vertex, add edge, remove edge, lookUp vertex, and lookUp edge all drop to an average O(1) time complexity.

Do I need an updated representation of Graph?
Yes. If you want to demonstrate Mid-Senior level problem-solving for dynamic graph modifications, you should upgrade the representation.

Below is the upgraded Python class maintaining continuity with our previous code, but entirely re-architected using a Dictionary of Dictionaries to meet your strict time-complexity requirements.

--------------------------------------------------------------------------------
Python Code: Mid-Senior Level Optimized Graph (Adjacency Map)
"""


"""
Further explanation of the Data structure:

Yes, you can absolutely have a dictionary where the key is an integer and the value is another dictionary. As we discussed previously, this structure is called an Adjacency Map, and it is a highly optimized way to represent a graph that goes beyond the basic array-of-lists approach shown in the video sources.

Here is a simple breakdown of how it works:
*   **The Outer Dictionary Key:** Represents the starting **Vertex**.
*   **The Inner Dictionary:** Represents all connected **Neighbors** and the **Weight** of that connection.
*   **Structure:** `{ Source_Vertex: { Neighbor_Vertex: Edge_Weight } }`

### Example: One Single Undirected Edge
Let's take an example from the video: an undirected edge between vertex `0` and vertex `1` with a weight of `10`. 

Because the graph is **undirected**, the connection goes both ways (0 connects to 1, and 1 connects to 0). Here is exactly how it is represented in the dictionary of dictionaries:

```python
adj_map = {
    0: { 1: 10 },
    1: { 0: 10 }
}
```

### How to read this data structure:
1.  **`adj_map`** gives you the inner dictionary **`{ 1: 10 }`**. This translates to: "Vertex 0 is connected to Vertex 1, and the weight of this edge is 10."
2.  **`adj_map`** gives you the inner dictionary **`{ 0: 10 }`**. This translates to: "Vertex 1 is connected to Vertex 0, and the weight of this edge is 10."

### Why did we use this?
If you want to check if an edge exists between `0` and `1`, or if you want to find the weight of that edge, you simply execute `adj_map`. Because dictionaries in Python use hashing, jumping straight to key `0` and then straight to inner key `1` takes **$O(1)$ constant time**. 

*(Note: As established in our conversation history, the video specifically teaches the Array of Lists approach, so this dictionary-of-dictionaries approach is an independent optimization to meet the strict dynamic performance requirements you asked for.)*
"""
