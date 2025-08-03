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


# Now for a DFS, we will usually just use recursion
# For example, here is a problem where we just want to check that each node in the tree
# is balanced i.e. the hight of the left subtree and the right subtree differ by at most 1

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

# For a DFS, if we are doing it recursively, it is important for us to decide where the recursion is happening.
# For example, if the current node depends on the children, you would put the "checking statements" after the recursion.
# However, if the current node rather depends on what you had encountered already in the search (i.e. the parents),
# you would want to put the "checking" statements before the recursion.

# In the example above, we are checking conditions after the recursion.
# I have attached an example below where we are checking conditions before the recursion.
# The following problem is to find the number of "good" nodes in a binary tree.
# A "good" node is a node where the path to that node has no nodes with a value greater than to the value of that node.

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