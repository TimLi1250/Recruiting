# Trees: Two things we need to memorize would be BFS and DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
# The most important thing we need to remember here is that a BFS uses a queue (FIFO)
from collections import deque

class BinaryTreeBFS:
    def __init__(self, root=None):
        self.root = root

    def bfs(root):

        bfs_queue = deque()
        # After initializing our queue, we want to immediately put the first root node in it so that
        # it is not empty
        bfs_queue.append(root)

        # Now the first thing we want to do is pop the root node from the queue and add
        # its neighbors to the queue

        while len(bfs_queue) > 0:

            print_list = []
            # We want to find the length of the queue
            length = len(bfs_queue)
            # And then pop out everything from the queue
            for i in range(length):
                node = bfs_queue.popleft()
                # After we pop out everything from the queue, we want to make sure to add the
                # neighbors of all the nodes we popped out
                # In this case, the neighbors are the left and right children of the node
                if node is not None:
                    print_list.append(node.val)
                    bfs_queue.append(node.left)
                    bfs_queue.append(node.right)
                else:
                    print_list.append(None)
        print(print_list)

'''
Now for a DFS, we will usually just use recursion
For example, here is a problem where we just want to check that each node in the tree
is balanced i.e. the hight of the left subtree and the right subtree differ by at most 1
'''
class balancedBinaryTree:
    def isBalanced(self, root) -> bool:

        self.result = True
        # In most dfs cases, we will usually have a base case where we check if the current node is None
        # Usually here we can either return -1, 0 or nothing.
        def dfs(curr):
            if curr is None:
                return -1

            # This is our recursive DFS, we will recurse into the left and right children
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                self.result = False
            # Then we will return something that is based on the result of the left and right children
            return 1 + max(left, right)
        # We finally just need to make sure to call this function on the root node
        dfs(root)
        return self.result
'''
For a DFS, if we are doing it recursively, it is important for us to decide where the recursion is happening.
For example, if the current node depends on the children, you would put the "checking statements" after the recursion.
However, if the current node rather depends on what you had encountered already in the search (i.e. the parents),
you would want to put the "checking" statements before the recursion.

In the example above, we are checking conditions after the recursion.
I have attached an example below where we are checking conditions before the recursion.
The following problem is to find the number of "good" nodes in a binary tree.
A "good" node is a node where the path to that node has no nodes with a value greater than to the value of that node.
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        # maximum = root.val
        def dfs(curr, maxi):
            if curr is None:
                return
            if curr.val >= maxi:
                self.result += 1
                print(curr.val, maxi)
                maxi = curr.val

            left = dfs(curr.left, maxi)
            right = dfs(curr.right, maxi)

            return maxi
        dfs(root, root.val)
        return self.result

'''
After reading the book, the order of the methods depends on what kind of traversals you are doing.
Preorder traversal: 1. process node 2. dfs(node.left) 3. dfs(node.right)
Inorder traversal: 1. dfs(node.left), 2. process(node), 3. dfs(node.right)
Postorder traversal: 1. dfs(node.left) 2. dfs(node.right) 3. process(node)

Furthermore, if we want to do a question iteratively instead of recursively, we can implement a stack
'''

'''
Here are some common NeetCode questions and their approach to each one.

1. Widest Binary Tree Level: return the width of the widest level in a binary tree where the width is defined as the distance
between its leftmost and rightmost nodes.
Here we can just assign each node a index and then do a level-order traversal (BFS)

2. Binary Search Tree Validation: We just want to verify whether or not a binary search tree is valid or not
Here we can do a DFS, but while we are running the DFS, we need to pass in lower and upper bounds e.g. valid(node, left, right)

3. Lowest Common Ancestor: return the lowest common ancestor of two nodes (p, q) in a binary tree
There are two variations to this question:
a) if the binary tree is actually a binary search tree, this question becomes slightly easier.
In that case, we just need to check a couple of cases. Basically at any root node, it could be the ancestor so we check the following cases
* p < root and q < root -> recurse in root.left
* p > root and q > root -> recurse in root.right
* p < root and q > root -> found common ancestor

b)
Now the second variation to this question is for any binary tree.
Let's assume a node 3 is the LCA, then where can p and q be?
* one at 3's left subtree and one at 3's right subtree
* one at node 3 and one at 3's left subtree
* one at node 3 and one at 3's right subtree

If at least two of these three boolean values are True, then the current node is the lowest common ancestor.

4. Building a binary tree from Preorder and Inorder traversals
Here we want to first create the current node pointed at preorder_index, increment our preorder_index so it points to the next
node that needs to be created and finally
Make a recusrive call to build the current node's left and right subtrees.
* pass in the subarray [0, inorder_index - 1] for left subtree
* pass in the subarray [inorder_index + 1, n-1] for right subtree

5. Maximum Sum of a Continuous Path in a Binary Tree
The first thing we need to understand is that all paths have a root.
i.e. the maximum path sum from node 5 is 5 + (max path sum from left) + (max path sum from right)
However, when we return the maximum sum, the result has to be a continuous path so we return
node.val + max(left_sum, right_sum)
'''
