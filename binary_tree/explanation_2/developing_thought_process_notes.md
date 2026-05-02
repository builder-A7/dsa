# Q1
What is the difference between Expectation-Faith and Top-Down recursion?

# Ans:
The core difference between Expectation-Faith and Top-Down recursion lies in the direction of information flow between parent and child nodes during the recursive calls.
Expectation-Faith (Bottom-Up Information Flow) In the Expectation-Faith framework, information flows from the bottom of the tree up to the root.
The Concept: A parent node delegates a task to its subtrees, having "faith" that its left and right children will correctly solve the problem for their respective branches and return the sub-answers. 
The parent waits for these returns, and then processes those sub-answers alongside its own data to meet the overall "expectation".

When to use it: When a node relies on the completed results of its subtrees to figure out its own localized answer.
Example: Calculating the size or sum of a tree. To find the total sum, a parent node blindly trusts its left child to return the sum of the entire left branch, and its right child to return the sum of the entire right branch. Once both return, the parent calculates the total by executing left_sum + right_sum + node.data.

Top-Down Recursion (State Passing) In Top-Down recursion, information flows from the root of the tree down to the leaves.
The Concept: A child node cannot determine the answer by itself or by asking its own children; it fundamentally requires context from its ancestors. Therefore, the parent accumulates a running "state" and explicitly passes it down as arguments to its recursive child calls.

When to use it: When a problem requires historical context, continuous path tracking, or knowledge of the nodes that came before it.
Example 1 (Path Accumulation): In the "Path to Leaf from Root" problem, a node cannot know the path that leads to it. Instead, the parent adds its own value to a running sum and path array before making the recursive call, handing this updated context down to the children so they are aware of the accumulated state up to that point.

Example 2 (Parent Reference): In the "Print Single Child Nodes" problem, a child cannot independently determine if it is an only child. The parent must pass a reference to itself down to its children, allowing the child to evaluate its own condition by checking the parent's left and right pointers


# Q2
We have made use of the stateMachine and Expectation-Faith strategies to solve different Questions. We have solved different questions using these 2 strategies?
How to know: which strategy to apply in which problem?
I was able to observe that for stateMachine - it had something to do with pre, in and post order traversals - Where are we in the recursive code, where are we in the stack?

But there were so many other problems - many used the expectation - faith. What is that hint in the question which an observer can catch so that his brain immediately starts thinking: Yes, Expectation-Faith strategy is the one to be used here?

Were there any more strategies?

# Ans:
Your observation about the State Machine strategy is spot on. It is explicitly used to simulate the Euler tour and the recursion stack execution states (1 for Pre-order, 2 for In-order, 3 for Post-order) when you need to perform traversals iteratively without using the system's call stack.

Here is how you can train your brain to immediately identify when to use Expectation-Faith, followed by the other distinct problem-solving strategies we have utilized.

The Hint for Expectation-Faith: The "Helpless Parent"
The dead giveaway for the Expectation-Faith strategy (which is a Bottom-Up approach) is when a parent node is completely helpless to calculate its own answer until it receives the fully computed answers from its subtrees.
If you look at a problem and ask yourself, "Can a node solve this just by looking at its own data and its immediate children?" and the answer is No, you likely need Expectation-Faith. You must trust the children to do the heavy lifting for their entire branches, return the sub-answers, and then the parent links those sub-answers together.
Examples of the Hint in Action:
Is BST: A node cannot know if it is a valid Binary Search Tree just by checking if it is greater than its immediate left child; it must be greater than the maximum of the entire left subtree. 
Therefore, the parent is helpless until the left child returns its max and the right child returns its min.

Diameter: The longest path might not pass through the root at all. 
The parent is helpless until it asks its children, "What is your maximum height, and what is your internal diameter?" It uses those returned values to calculate its own maximums.

Tilt / Sum / Size / Max: A parent node cannot know the total sum of the tree without first waiting for the left child to return the sum of the entire left branch and the right child to return the sum of the entire right branch.

Were there any more strategies?
Yes! Across the binary tree problems we have solved, there are four other distinct strategies you should keep in your mental toolkit:
1. Top-Down State Passing (Accumulation)
The Hint: The child node is helpless because it needs historical context or information about its ancestors to evaluate itself.
How it works: Information flows from the Root down to the Leaves. The parent accumulates a running state and passes it down as function arguments.

When we used it:
Path to Leaf in Range: A leaf node doesn't know the path that led to it. The parent adds its own data to the running path and sum arrays, and passes them down.

Print Single Child Nodes: A child doesn't know if it has a sibling. The parent passes a reference to itself down to the child so the child can check parent.left and parent.right.

2. Boolean DFS Backtracking ("Find and Report")
The Hint: You are searching for a specific target node or path, and you need to construct the path backwards once it is found.

How it works: The recursive function returns a True/False boolean. If a child returns True, the parent knows the target is in that branch, appends its own data to the path, and returns True upwards.

When we used it: Node to Root Path. The root delegates the search to the left. If it gets a False, it tries the right.

3. Level Order / Breadth-First Search (BFS)
The Hint: The problem specifically asks you to process the tree horizontally (level by level) rather than diving deep into branches.
How it works: You abandon recursion entirely and use a Queue data structure. 
You follow the strict mantra: Remove, Print, Add Children.
When we used it: Printing the tree level-by-level line-by-line.

4. Relative Depth & Blockers
The Hint: The problem asks you to find nodes that are a specific distance (k) away from a target.
How it works: You pass a counter k downwards, decrementing it by 1 at each step. When k==0, you print the node. If you are searching upwards through ancestors, you must pass a "blocker" node to prevent the recursion from traveling back down the same path it just came from.

When we used it: Print K Levels Down and Print Nodes K Level Far.