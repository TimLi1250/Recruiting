# Each device belongs to a rooted hierarchy. A key for device "u" grants access to "u" and every device below it.
# Find the narrowest key covering requested devices.

# Implement this stateful interface
#
# class DeviceTree:
#     __init__(parent: list[int])
#     narrowest_key(targets: list[int]) -> int

# Requirements
# Part A - Two targets. Given a rooted tree as a parent array, return the lowest common ancestor of two
# target nodes. Node 0 is the root and parent[0] = -1
import math

class DeviceTree:
    def __init__(self, parent: list[int]):
        # `parent[device]` identifies that device's immediate parent.
        # Node 0 is the root, so parent[0] == -1.
        self.parent = parent

    def narrowest_key(self, targets: list[int]) -> int:
        # Part A assumes we only have two targets
        first, second = targets[0], targets[1]
        # We can just make two lists representing a path to the target node, and then reverse iterate through the lists
        first_list, second_list = [], []
        while first != 0:
            first_list.append(first)
            first = self.parent[first]
        while second != 0:
            second_list.append(second)
            second = self.parent[second]

        first_list.reverse()
        second_list.reverse()

        narrowest_key = 0
        for i in range(min(len(first_list), len(second_list))):
            if first_list[i] == second_list[i]:
                narrowest_key = first_list[i]

        return narrowest_key

    # Part B - Batch access. After one tree preprocessing pass, answer up to 200,000 independent two-node
    # queries efficiently. Return one answer per query.

    def depth(self, node) -> int:
        depth = 0
        while node != 0:
            node = self.parent[node]
            depth += 1
        return depth

    def narrowest_batches(self, targets: list[list[int]]) -> list[int]:
        # Now we have a huge list of targets like [[3, 4], [1, 5], [6, 7]] etc.
        # We want to return a list of LCA like [5, 6, 1, 9] etc.
        # We would like to just call the function above for every pair of targets
        # However, I believe our implementation above is too slow so we need to try a different way

        # 1. We can just compute the depth of every node once and put it into a table
        depth_table = []
        for i in range(len(self.parent)):
            depth_table.append(self.depth(i))

        # 2. Now we need to compute the ancestor table
        max_depth = max(1, int(math.log2(max(depth_table))) + 1)

        ancestor_table = [[0] * len(self.parent) for _ in max_depth]
        # First column is just the immediate parents
        ancestor_table[0] = self.parent[:]
        for i in range(1, max_depth):
            for node in range(len(self.parent)):
                middle = ancestor_table[i - 1][node]
                ancestor_table[i][node] = ancestor_table[i - 1][middle]
