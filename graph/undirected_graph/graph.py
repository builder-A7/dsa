# Undirected and Unweighted graphs:


class Graph:
    """
    Highly Optimized Graph Representation using an Adjacency Map (Dict of Dicts).
    - Context: UNDIRECTED by default.
    - Context: UNWEIGHTED by default (weight defaults to None).

    Time Complexities (Average):
    - Add Vertex: O(1)
    - LookUp Vertex: O(1)
    - Add/Update Edge: O(1)
    - LookUp Edge: O(1)
    - Remove Edge: O(1)
    - Remove Vertex: O(V)
    """

    def __init__(self):
        # Dictionary to map vertex -> {neighbor: weight}
        self.adj_map = dict()

    def add_vertex(self, v: str) -> None:
        """Adds a vertex to the graph in O(1) time."""

        """ We don't need to preserve order of insertion w.r.t. edges. Also, no parallel edges. So, we can use set - to avoid duplicates. LookUp is O(1). Set is internally implemented using a HashMap. It is a HashSet."""
        if v not in self.adj_map:
            self.adj_map[v] = set()

    def lookup_vertex(self, v: str) -> bool:
        """Checks if a vertex exists in O(1) time."""
        return v in self.adj_map

    def add_edge(self, u: str, v: str, is_directed: bool = False) -> None:
        """
        Adds or updates an edge in O(1) time.
        Defaults to UNDIRECTED and UNWEIGHTED.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_map[u].add(v)
        if not is_directed:
            self.adj_map[v].add(u)

    def lookup_edge(self, u: str, v: str) -> bool:
        """Checks if an edge exists in O(1) time."""
        return u in self.adj_map and v in self.adj_map[u]

    def remove_edge(self, u: str, v: str, is_directed: bool = False) -> None:
        """
        Removes an edge in O(1) time.
        Defaults to UNDIRECTED removal.
        """
        if self.lookup_edge(u, v):
            self.adj_map[u].remove(v)

        if not is_directed and self.lookup_edge(v, u):
            self.adj_map[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Removes a vertex and all its connected edges.
        Time Complexity: O(V) because we must remove references from neighbors.
        """
        if v not in self.adj_map:
            return

        # 1. Remove references to `v` from all its neighbors
        for neighbor in self.adj_map[v]:
            if v in self.adj_map[neighbor]:
                self.adj_map[neighbor].remove(v)

        # 2. Completely delete the vertex `v`
        del self.adj_map[v]

    def display(self):
        """Utility to visualize the Adjacency Map with or without weights."""
        for src, dest in self.adj_map.items():
            curr_line_to_print = ""
            for neighbor in dest:
                curr_line_to_print += f"{src} -> {neighbor}" + ", "
            print(curr_line_to_print[:-2])


# ==========================================
# Interview Usage Example
# ==========================================
if __name__ == "__main__":
    graph = Graph()

    # Adding edges based on the video's vertices (0 to 6),
    # but strictly UNWEIGHTED and UNDIRECTED as per your constraints.
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    print("--- Unweighted Undirected Graph ---")
    graph.display()
