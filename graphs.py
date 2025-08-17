'''
Let's take a look at graphs, a graph will consist of nodes and edges

We can define a graph node as follows
'''

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

'''
There are a couple types of graphs we can define:
* Directed v.s. Undirected
* Weighted v.s. Unweighted
* Cyclic v.s. Acyclic

Graphs are usually stored as either an adjacency list or an adjacency matrix
An adjacency list is usually stored as a hashmap like {node: neighbors}
An adjacency matrix is usually stored as a 2D matrix where matrix[i][j] indicates an edge between nodes i and j
'''

# Just like trees, we can use DFS and BFS to traverse a graph.

def dfs(node, visited):
    visited.add(node)
    ## process(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)

from collections import deque

def bfs(node):
    visited = {}
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            ## process(node)
            for neighbor in node.neighbors:
                queue.append(neighbor)


# Now let's say for example you are given the edges as a list or something
# i.e. [[2,3],[3,1],[1,5],[5,6],[6,2]]
# we can make a graph from this like so
graph = {}

def add_edges(u, v):
    if u not in graph:
        graph[u] = v
    if v not in graph:
        graph[v] = u

    graph[u].append(v)
    graph[v].append(u)

'''
Now let's look at a couple examples.
We can start with the example: Graph Deep Copy
'''

# This problem is relatively straight forward. At each step in the DFS process, we want to create the node and then run the process
# on the neighbors of the node
def graph_deep_copy(node):
    if not node:
        return None

    def dfs(node, clone_map):
        # check if the node had already been cloned in the past
        # if so, we just want to return that clone instead of making a new one
        if node in clone_map:
            return clone_map[node]

        # make a new cloned node
        cloned_node = GraphNode(node.val)
        # add the new cloned node to the clone map
        clone_map[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_neighbor = dfs(neighbor, clone_map)
            cloned_node.neighbors.append(cloned_neighbor)
        return cloned_node

    return dfs(node)

'''

Now let's look at the question counting islands. The jist of this question is that given a 2D array of 1s and 0s where 1s represents
land and 0 represents water. Count how many islands there are in total.

The approach to this question is that once we find a land cell, we can just perform a DFS or BFS to find every land cell that is part of that island.
Therefore the algorithm for this question is:
1. Search through the matrix until we find a land cell
2. Upon encountering a land cell, we can explore the island using DFS but once we visit each land cell, we need to mark it as visited
i.e. we can just mark it as "-1"
3. Increment the number of islands by 1
4. When we land on the last element in the matrix, we are done.
'''

def count_islands(matrix) -> int:
    if not matrix:
        return 0

    num_islands = 0

    # iterate through the entire matrix and run dfs on any land cells
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                dfs(r, c, matrix)
                num_islands += 1

    return num_islands

def dfs(r, c, matrix):
    # once we visit the cell, we want to mark it as visited
    matrix[r][c] = -1
    # there are four directions to go from a cell, we want to run a DFS on all 4 directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in directions:
        next_r, next_c = r + d[0], c + d[1]
        if (matrix[r][c] == 1):
            dfs(next_r, next_c, matrix)


'''
Now let's look at a couple questions and their approaches:

1. Matrix Infection where you are given a matrix where 0: Empty, 1: Uninfected, 2: Infected.
Every second, an infected cell infects its uninfected neighbors.

My approach to this question: we know that if there is an infected cell, every uninfected cell in the same graph will end up being
infected. Furthermore, we know that infected cells are related to the distance from the the original infected cell. Therefore, we
can use something related to a BFS i.e. a multi-source BFS. We keep track of how many levels we need to get through until the
queue is empty.

2. Given an undirected graph, determine if it is bipartite. A graph is bipartite if the nodes
can be colored in one of two colors such that no two adjacent nodes are the same color.

Here we can use the Graph coloring approach. This approach involves for each node we color blue, we color its neighbors orange
and vice versa. Therefore, we just need to check if at any point in the DFS, the color of a node is equal to the color of its neighbor.

3. Longest Increasing Path: find the longest strictly increasing path in a matrix of positive integers

We want to see that we can only move to a neighboring cell if its value is higher than the current one -> DAG. Therefore, the problem
becomes finding the longest path in a DAG. To do this we can just call a dfs on every cell in the matrix and find the maximum based on that.

Therefore the psuedocode looks something like this:
def dfs(cell):
    max_path = 1
    for each neighbor of the current cell:
        if value of neighbor > value of cell
            max_path = max(max_path, dfs(neighbor) + 1)
    return max_path

For further optimization, we can store the DFS result of each cell -> memoization.

4. Given two words, start and end and a dictionary containing an array of words, return the length of the shortest
transformation sequence to transform start to end.

To approach this question, we should obviously start by creating a graph where start is the starting node and end is the ending node.
Then to return the length of the shortest transformation sequence, we just need to find the shortest path which we can do using a level-order
traversal.

Now how can we build this graph? For each word, we need to generate all possible words by changing each letter in the word.
* An optimization we can do here is that instead of just running the level-order traversal from the start node we can run it
* from both the start and the end node -> bidirectional traversal

5. Merging Communities: n people numbered 0 to n-1, each person intially belonging to a separate community. We want to
write two functions, connect and get_community_size
'''

##################################################################################################################################
'''
Here we need to use the Union-Find datastructure.
In the Union-Find datastructure, we have two operations
* Union: takes two elements from different sets and make them part of the same set
* Find: determine what set an element belongs to

Union: Let's say we have two communities 1 -> 2 and 5 -> 3 <- 4. We want to merge 1 and 5 together.
We have parents and representatives.
* parents are what a node is currently pointing to
* representatives are what every node is pointing to (representative of the entire community)

Let's say we have the graph 0 -> 1 -> 2, then the parent of 0 is 1 while the representative of 0 is 2.

Now to merge these communities, we want to first pick the representative from the larger community to be the new
representative of the entire community.
Then all we need to do is have the parent of the smaller representative to be the bigger representative.

Find: the find function should return the representative of the community the person is in
To find this, we can just traverse the parent chain until we reach the representative ->
we can see this through checking if the parent of the current node is itself -> this can only happen to the representative
'''
# Here is the Union-Find data structure:
class UnionFind:

    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        # size[i] is the size of the community of person i
        self.size = [1] * size

    def union(self, x: int, y: int) -> None:
        # first we should find the representatives of each community
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        # Here we can perform a optimization called path compression but this is not completely necessary
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]

##################################################################################################################################
'''
6. Prerequisites:
Given an integer n representing the number of courses labeled from 0 to n-1, and an array of prerequisite parirs,
we want to determine if it is possible to enroll in all courses.

We notice that in order for complete enrollment to be possible, there must not be a cycle in the graph.
Furthermore, the first courses that can be completed are those without any arrows pointing to them -> in-degree is 0.
Therefore, we can just remove them from the graph and update the remaining degrees of the graph.

Here we can use Kahn's algorithm:
* the first step is to determine the in-degree of each course
* then add the courses with an in-degree of 0 to a queue
* pop the course from the queue and then for each course that has course 0 as a prerequisite, reduce their in-degree by 1
* then add the new courses who have an in-degree of 0 to the queue
'''