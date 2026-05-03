class Edge:
    """
    Represents a directed or undirected edge between two vertices.
    Optimized with __slots__ to reduce memory overhead in Python.
    """

    __slots__ = ["src", "nbr", "wt"]

    def __init__(self, src: int, nbr: int, wt: int):
        self.src = src  # Source vertex
        self.nbr = nbr  # Neighbor (Destination) vertex
        self.wt = wt  # Weight of the edge

    def __repr__(self):
        return f"({self.src} -> {self.nbr} @ {self.wt})"


class Graph:
    """
    Represents a graph using an Adjacency List.
    Space Complexity: O(V + E)
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Initialize an array of empty lists to hold the edges for each vertex
        self.adj_list: list[list[Edge]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, wt: int, is_directed: bool = False):
        """
        Adds an edge to the graph. The video uses an undirected graph setup.
        Time Complexity: O(1)
        """
        self.adj_list[u].append(Edge(u, v, wt))
        if not is_directed:
            self.adj_list[v].append(Edge(v, u, wt))

    def display(self):
        """
        Utility to visualize the adjacency list representation.
        """
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # The video sets up a graph with 7 vertices (0 to 6) [1, 5]
    vertices = 7
    graph = Graph(vertices)

    # Adding edges as described in the video examples (Source, Neighbor, Weight) [4, 5]
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 3, 40)
    graph.add_edge(1, 2, 10)
    graph.add_edge(2, 3, 10)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 5, 3)
    graph.add_edge(5, 6, 3)
    graph.add_edge(4, 6, 8)

    # Display the constructed graph
    graph.display()


"""
Here are the key problem-solving scenarios and edge cases discussed in the sources, followed by the optimized Python implementation.

Key Scenarios & Problem-Solving Applications
The video outlines several classic graph scenarios that you should be prepared to solve in an interview:

Pathfinding: Finding all possible paths between a source and destination, or finding the shortest path based either on the minimum number of edges (using Breadth-First Search) or the minimum total weight/distance.

Minimum Spanning Tree (MST): Connecting all nodes (e.g., computers) using the minimum possible cost or "wire" so that every node is reachable.

Dependency Resolution (Directed Graphs): Handling prerequisites where certain tasks must be completed before others, such as file compilation sequences. This is a classic use case for Topological Sorting.

Corner Cases & Edge Cases

Space Complexity Limitations for Large Graphs: When representing a graph, using an Adjacency Matrix (a 2D array) is a massive memory risk. If a graph has more than 10,000 vertices, an Adjacency Matrix becomes unviable because it requires O(V ^ 2 ) space, mostly filled with zeroes where no edges exist.

Optimal Representation: To handle the aforementioned memory issue, an Adjacency List (an array of lists containing edges) is strictly recommended as the "proper implementation" for optimal space and time complexity.

(Special Note: The provided video transcript does not discuss the "Expectation-Faith" recursive thought process. Therefore, there is no video-specific example to explain for this concept.)

--------------------------------------------------------------------------------
Python Code: Graph Foundation (Adjacency List)
To maintain continuity and interview standards, we will build a robust Object-Oriented foundation for the graph. The Java code in the video uses an Array of ArrayLists storing an Edge object.

Below is the highly optimized Python equivalent using a List of Lists.
"""
