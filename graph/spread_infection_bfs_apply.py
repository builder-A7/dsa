from collections import deque


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

    # ... (Previous methods: bfs, is_cyclic, is_bipartite, etc. remain here) ...

    def spread_infection(self, src: int, t: int) -> int:
        """
        Calculates how many people will be infected by time 't'.
        Patient zero (src) is infected at time 1.

        Time Complexity: O(V + E) - Standard BFS traversal.
        Space Complexity: O(V) - For the Queue and the Visited set.
        """
        # Queue stores tuples of (current_vertex, time_infected)
        # Initialization Time Trap: Source starts at time 1
        queue = deque([(src, 1)])
        visited = set()
        infected_count = 0

        while queue:
            # Step 1: Remove
            current, time = queue.popleft()

            # Corner Case 1: Time Limit Exceeded
            # If the popped person was infected after time 't', stop processing.
            if time > t:
                break

            # Step 2: Mark & Handle Cycles (Corner Case 2)
            if current in visited:
                continue

            # Late marking: mark as visited only after popping
            visited.add(current)

            # Step 3: Work
            infected_count += 1

            # Step 4: Add unvisited neighbors
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    # Neighbors get infected 1 unit of time after the current vertex
                    queue.append((neighbor, time + 1))

        return infected_count

    def display(self):
        """Utility to visualize the unweighted Adjacency List."""
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> {self.adj_list[i]}")


# ==========================================
# Interview Usage Example (Based on Video)
# ==========================================
if __name__ == "__main__":
    # Setup 7 vertices (0 to 6) representing people
    graph = Graph(7)

    # Adding unweighted, undirected edges (representing contact between people)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    print("--- Graph Structure (Contact Network) ---")
    graph.display()

    # Scenario:
    # Patient zero is person 6.
    # We want to know how many people are infected by time 3.
    # Expected infection spread:
    # t=1: [4] (Count = 1)
    # t=2: [5, 6] (Count = 3)
    # t=3: [7] (Count = 4)
    patient_zero = 6
    time_limit = 3

    total_infected = graph.spread_infection(src=patient_zero, t=time_limit)

    print(f"\n--- Infection Spread ---")
    print(
        f"Total people infected starting from person {patient_zero} by time {time_limit}: {total_infected}"
    )


"""
Here are the problem-solving strategies, edge cases, and the specific algorithmic pattern for the "Spread Infection" problem, adhering strictly to your unweighted and undirected constraints.

The "Expectation-Faith" Note -
Because this problem asks how far an infection spreads within a specific time frame, it requires exploring the graph radius-wise (level-by-level). Therefore, the video explicitly uses Breadth-First Search (BFS). 

The recursive DFS "Expectation-Faith" thought process does not apply here.

The Problem-Solving Strategy: Level-Order BFS (Time Tracking) -
This problem is a direct application of the BFS "Remove, Mark, Work, Add" mantra. 

The only modification from a standard BFS is that your Queue must store both the vertex and the time at which that vertex gets infected.

The source (patient zero) starts at time 1.

Every time you add a neighbor to the Queue, its infection time is current_time + 1.

The "Work" step simply involves incrementing an infected_count.

Corner Cases & Scenarios to Handle
Time Limit Exceeded (The Break Condition): When you pop a vertex from the Queue, you must immediately check if its time is strictly greater than the given time limit t. 

If it is, you must break out of the loop entirely. Because BFS processes elements in monotonically increasing time, if the current element exceeds t, all subsequent elements in the Queue will also exceed t.

Already Infected (Cycle Prevention): Just like standard BFS, multiple infected people might try to infect the same shared neighbor. If the popped vertex is already in your visited set, you must continue (skip) to prevent recounting them in your total infected count.

Initialization Time Trap: A classic interview mistake is starting patient zero at time 0. The video specifically establishes that the initial infection is observed at time 1.

--------------------------------------------------------------------------------
Python Code: spread_infection (Adjacency List + BFS)
Here is the Mid-Senior level implementation. We are integrating this method into our ongoing Graph class. Using collections.deque ensures O(1) pop operations from the front of the queue.

"""
