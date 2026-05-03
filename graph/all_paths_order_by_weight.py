import math
import heapq


class Graph:
    """
    Graph Representation using Adjacency List (Array of Lists).
    - Context: UNDIRECTED and UNWEIGHTED by default.
    """

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: list[list[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected, unweighted edge."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def multisolver(self, src: int, dest: int, criteria: int, k: int) -> dict:
        """
        Explores all paths to solve 5 queries in a single DFS traversal.
        Metrics are based on Path Length (number of edges).
        """
        # 1. Initialize trackers with Identity Values
        smallest_len = math.inf
        smallest_path = []

        largest_len = -math.inf
        largest_path = []

        ceil_len = math.inf  # Smallest among those > criteria
        ceil_path = []

        floor_len = -math.inf  # Largest among those < criteria
        floor_path = []

        # Min-Heap for Kth largest.
        # Stores tuples: (path_length, insertion_counter, path_list)
        # The counter prevents TypeError if path_lengths are equal.
        kth_largest_pq = []
        pq_counter = 0

        visited = set()

        def _dfs(current: int, path_so_far: list[int]):
            nonlocal smallest_len, smallest_path, largest_len, largest_path
            nonlocal ceil_len, ceil_path, floor_len, floor_path, pq_counter

            # Base Case / Multisolver Evaluation
            if current == dest:
                path_len = len(path_so_far) - 1  # Number of edges

                # Update Smallest
                if path_len < smallest_len:
                    smallest_len = path_len
                    smallest_path = list(path_so_far)

                # Update Largest
                if path_len > largest_len:
                    largest_len = path_len
                    largest_path = list(path_so_far)

                # Update Ceil (Just Larger than Criteria)
                if path_len > criteria and path_len < ceil_len:
                    ceil_len = path_len
                    ceil_path = list(path_so_far)

                # Update Floor (Just Smaller than Criteria)
                if path_len < criteria and path_len > floor_len:
                    floor_len = path_len
                    floor_path = list(path_so_far)

                # Update Kth Largest via Min-Heap
                heapq.heappush(
                    kth_largest_pq, (path_len, pq_counter, list(path_so_far))
                )
                pq_counter += 1
                if len(kth_largest_pq) > k:
                    heapq.heappop(kth_largest_pq)  # Drop the smallest of the K elements

                return

            # Expectation-Faith & Backtracking
            visited.add(current)
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    path_so_far.append(neighbor)
                    _dfs(neighbor, path_so_far)
                    path_so_far.pop()  # Backtrack path
            visited.remove(current)  # Backtrack visited

        # Trigger the recursive DFS
        _dfs(src, [src])

        # Package results. The Kth largest is the root of our Min-Heap (index 0).
        kth_path = kth_largest_pq[1] if len(kth_largest_pq) == k else None

        return {
            "Smallest Path": smallest_path,
            "Largest Path": largest_path,
            f"Ceil (Just > {criteria})": ceil_path if ceil_len != math.inf else None,
            f"Floor (Just < {criteria})": (
                floor_path if floor_len != -math.inf else None
            ),
            f"{k}th Largest Path": kth_path,
        }


# ==========================================
# Interview Usage Example
# ==========================================
if __name__ == "__main__":
    graph = Graph(7)

    # Adding unweighted, undirected edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 6)

    # Multisolver execution
    # Looking for paths from 0 to 6.
    # Criteria: length 4.
    # K: 3rd largest path.
    results = graph.multisolver(src=0, dest=6, criteria=4, k=3)

    print("--- Multisolver Results ---")
    for key, value in results.items():
        print(f"{key}: {value}")


"""
Here are the problem-solving strategies, edge cases, and the "Expectation-Faith" recursive thought process for solving multiple graph queries (Smallest, Largest, Ceil, Floor, and Kth Largest paths) in a single DFS traversal.

Adaptation for Unweighted Graphs
Because we are strictly using unweighted graphs based on your constraints, the concept of "Path Weight" discussed in the video translates directly to Path Length (the total number of edges in the path).

The Recursive Thought Process & The "Expectation-Faith" Model
The video evolves the "Expectation-Faith" framework from finding all paths to a Multisolver pattern:

Expectation: You expect to traverse every possible route to the destination.
Faith: You have faith that the backtracking DFS will eventually guide every valid route to hit the base case (src == dest).

Resolution (The Multisolver): Instead of just printing the path at the base case, you evaluate the newly discovered path against global/external trackers (Smallest, Largest, Ceil, Floor, Kth Largest). Because you check every path at the base case, by the time the DFS fully terminates, your trackers will hold the correct optimal answers.

Corner Cases & Scenarios to Handle
Identity Values for Initialization: 
A classic interview pitfall is poor initialization.
To find the Smallest path, initialize your tracker with +Infinity.
To find the Largest path, initialize with -Infinity (minus inf.). This ensures the very first path discovered automatically replaces the initial value.

Ceil (Just Larger) & Floor (Just Smaller):
Ceil: Represents the smallest path among all paths that are strictly larger than a given criteria.

Floor: Represents the largest path among all paths that are strictly smaller than a given criteria.

Kth Largest Path via Priority Queue: 
Do not store all paths and sort them at the end (O(NlogN) space/time waste). Instead, maintain a Min-Heap (Priority Queue) of exact size K. If the heap exceeds size K, pop the smallest element. At the end, the root of the Min-Heap is exactly the Kth largest path.

--------------------------------------------------------------------------------
Python Code: DFS Multisolver (Adjacency List)
Here is the Mid-Senior level implementation. To maintain continuity, we continue building upon the Graph class using the Adjacency List structure. We use Python's nonlocal keyword and heapq to efficiently manage the state across the recursive call stack.
"""
