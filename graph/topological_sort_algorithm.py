class Graph:
    """
    Graph Representation and Utilities Toolkit.
    - Context: UNDIRECTED and UNWEIGHTED by default.
    - EXPLICIT OVERRIDE: Topological Sort requires DIRECTED edges.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def add_directed_edge(self, u: int, v: int) -> None:
        """
        EXPLICITLY specified Directed Edge (u -> v).
        Means 'u' has a directed path to 'v' (e.g., u must happen before v).
        """
        self.adj_list[u].append(v)

    # ... (Previous methods: bfs, dijkstra, is_cyclic, etc. remain here) ...

    def topological_sort(self) -> list[int]:
        """
        Executes a Topological Sort using DFS and a Stack.
        Only valid on Directed Acyclic Graphs (DAGs).

        Time Complexity: O(V + E) - Every vertex and edge is processed once.
        Space Complexity: O(V) - For the Visited set, Stack, and Recursion call stack.
        """
        visited = set()
        stack = []

        def _dfs_topo(current: int):
            # Pre-order: Mark as visited so we don't process it again
            visited.add(current)

            # Expectation-Faith: Resolve all downstream dependencies first
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    _dfs_topo(neighbor)

            # Post-order / Corner Case 1: All dependencies are resolved.
            # It is now safe to push the current node to the stack.
            stack.append(current)

        # Corner Case 2: Outer loop to handle disconnected components
        for v in range(self.num_vertices):
            if v not in visited:
                _dfs_topo(v)

        # The stack currently holds elements with the most-dependent at the bottom.
        # We must pop from the top to get the correct execution order.
        # In Python, returning the reversed list perfectly simulates popping all items.
        return stack[::-1]

    def display(self):
        """Utility to visualize the Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # Setup 7 vertices (0 to 6) representing tasks/files
    graph = Graph(7)

    # Adding EXPLICITLY DIRECTED edges to form a DAG (Directed Acyclic Graph)
    # Edge u -> v means Task u must appear before Task v.
    graph.add_directed_edge(0, 1)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(2, 3)
    graph.add_directed_edge(0, 3)
    graph.add_directed_edge(4, 3)
    graph.add_directed_edge(4, 5)
    graph.add_directed_edge(5, 6)
    graph.add_directed_edge(4, 6)

    print("--- Graph Structure (Directed Acyclic Graph) ---")
    graph.display()

    print("\n--- Topological Sort (Valid Execution Order) ---")

    # The video demonstrates that the Stack popping yields a valid order
    # where prerequisites strictly appear before their dependents.
    valid_order = graph.topological_sort()

    print(f"Topological Order: {valid_order}")
    # Expected valid topological order could be: [9-14]
    # Note: Multiple valid topological sorts can exist depending on the outer loop start order.


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for Topological Sort.

CRITICAL GRAPH CONSTRAINT OVERRIDE: You established that all graphs are strictly UNDIRECTED unless explicitly specified. I must explicitly specify that Topological Sort mathematically requires a Directed Acyclic Graph (DAG). 

An undirected graph implies a two-way dependency (a cycle), which makes dependency resolution impossible. To maintain your constraints while solving this, I have added an add_directed_edge method to our class specifically for this algorithm.

The "Expectation-Faith" Recursive Thought Process -

The video frames Topological Sort as a classic dependency resolution problem (e.g., compiling software files where File 0 depends on File 1). 

It uses Depth First Search (DFS) with a Stack.

Expectation: When you call DFS on a task (e.g., 0), you expect it to deeply explore all of task 0's prerequisites and push them into a Stack in the correct order.

Faith: You have faith that if you recursively call DFS on all of 0's unvisited dependencies, they will perfectly resolve their own sub-dependencies and push themselves to the Stack before returning control to 0.

Resolution (Post-Order): Once all recursive calls for 0's dependencies return, 0 itself is finally safe to execute, so you push 0 to the Stack.

Corner Cases & Scenarios to Handle -
The Pre-order vs. Post-order Trap (Interview Favorite): A common interview mistake is trying to add elements to a list the moment you visit them (Pre-order). 

In a disconnected graph, a node evaluated later in the outer loop might actually be a prerequisite for a node evaluated earlier, but Pre-order would place it at the bottom.

You must only push to the Stack in Post-order (after the DFS neighbor loop finishes). This guarantees a node is added only when all its downstream paths are fully resolved.

Disconnected Components: Just like finding connected components, a software build might have separate, isolated project trees. 

You must wrap your DFS in an outer loop from 0 to V-1. If a node is unvisited, trigger the DFS. This ensures no floating dependencies are missed.

--------------------------------------------------------------------------------
Python Code: topological_sort (Adjacency List)
Here is the Mid-Senior level implementation. We are integrating this into our ongoing Graph toolkit. I am using a standard Python list to represent the Stack, which we will reverse at the end to simulate popping from the top.
"""
