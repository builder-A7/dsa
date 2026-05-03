Are there any specific memory constraints?
When using dictionaries? For Graphs? Like we had 10K upper limit on n(vertices) for adj. matrix?

There is no strict 10,000 vertex limit when using the dictionary implementation.
The video explicitly states that the 10,000 vertex limit applies specifically to the Adjacency Matrix (2D Array). 
This is because an adjacency matrix allocates a V×V grid, meaning a graph with 10,000 vertices requires creating a matrix with 100 million slots. 
This wastes massive amounts of continuous memory, largely filled with zeros where no edges exist.
To solve this exact memory issue, the sources introduce the Adjacency List (an array of lists) as the "proper implementation".

(Please note: Because the dictionary-of-dictionaries approach is an optimisation we introduced to meet your strict O(1) time-complexity requirements, its specific memory behaviours are outside of the provided sources. You may want to independently verify the following information.)

Memory Constraints for the Dictionary Approach:
Space Complexity is O(V+E): Just like the array of lists taught in the video, the dictionary approach scales based only on the number of Vertices (V) and Edges (E) that actually exist. It does not allocate memory for empty connections.
The Upper Limit: Because it avoids the O(V ^ 2) memory trap of the matrix, it does not suffer from the 10K limit. You can easily represent graphs with hundreds of thousands or millions of vertices. The only true upper limit is the physical RAM available on your system.
The Mid-Senior Trade-off (Interview Insight): While a dictionary scales perfectly fine up to millions of vertices, it is important to mention in an interview that dictionaries carry a higher constant memory overhead under the hood compared to plain arrays. This is because hash tables need to allocate extra space to prevent hash collisions. However, this memory overhead is universally accepted as the necessary trade-off to achieve the O(1) time complexities for adding, removing, and looking up vertices and edges.