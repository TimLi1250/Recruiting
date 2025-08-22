'''
Let's take a look at backtracking

You can think of it as traversing all possible cases in a maze, if one end is a dead end, you will go back to the previous intersection
We can thus create a state space tree.
* edges represents a possible decision, move or action
* root node: represents the initial state before any decisions are made
* intermediate nodes: partially covered states or intermediate positions
* leaf nodes: complete or invalid solutions
* path: a path from the root to any leaf node represents a sequence of decisions that lead to a complete or invalid solution

For the backtracking algorithm, we can usually apply a recursive DFS
* need a termination condition, define the condition that specifies where a path should end
* iterate through decisions; for each decision
    1. make that decision and update the current state accordingly
    2. Recursively explore all paths that branch from this updated state by calling the DFS function on this state
    3. Backtrack by undoing the decision we made and reverting the state.


'''
####################################################################################################################################
'''
in psuedocode:
def dfs(state):
    if meet_termination_condition(state):
        process_solution(state)
        return

    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision)
'''
####################################################################################################################################
'''
Let's start by looking at an example problem:
Permutations: Return all possible permutations of a given array of unique integers

Consider the array [4, 5, 6]. We can create one permutation by picking one number, then a second and finally a third.
Now we have found one permutation we need to backtrack to find others. Let's go back to [4, 5]. Can we choose a different number for
the last number? No -> backtrack once more to be at [4].

Now at this point, we can add a different number to [4], we can add 6 to get [4, 6], and then we see we can add 5 to get [4, 6, 5].
We can perform this process to find all of the permutations.

To Traverse the state space tree,
1. We first pick an unused number and add it to the current permutation candidate. Mark this numbe as used by adding it to the used hash set
2. Make a recursive call with this updated permutation candidate to explore its branches
3. Backtrack: remove the last number we added to the current candidate array, and the used hash set
'''

def find_all_permutations(nums):
    res = []
    backtrack(nums, [], set(), res)
    return res

def backtrack(nums, candidate, used, res):
    # if the current candidate is a complete permutation -> add it to the result
    if len(candidate) == len(nums):
        res.append(candidate[:])
        return
    for num in nums:
        if num not in used:
            # add the num to the current candidate and also mark it as used
            candidate.append(num)
            used.add(num)

            # then we want to recursively explore all branches using the updated permutation candidate
            backtrack(nums, candidate, used, res)
            # backtrack by reversing the changes we made
            candidate.pop()
            used.remove(num)

'''
Now let's look at the question find all subsets where we return all possible subsets of a given set of unique integers.

To approach this question, we just need to realize that all possible subsets are made when we choose to include or exclude every
element in the original set.
'''

def find_all_subsets(nums):
    res = []
    backtrack(0, [], nums, res)
    return res
# here i is telling us which element we are currently considering
def backtrack(i, curr_subset, nums, res):
    if i == len(nums):
        res.append(curr_subset[:])
        return
    # include the current element and recursively explore all paths that branch from this subset

    curr_subset.append(nums[i])
    backtrack(i + 1, curr_subset, nums, res)
    # Exclude the current element and recursively explore all paths that branch from this subset.
    curr_subset.pop()
    backtrack(i + 1, curr_subset, nums, res)

'''
Now let's look at the question N queens where we try to fit n queens onto a nxn chessboard such that no two queens attack each other

The approach to this question is that let's say we place each queen on a new row (two queens can never be on the same row). Then, we
check if a queen can be placed anywhere on this new row, if it can't we just backtrack and resposition the previous row's queen

Another thing we need to consider is how we can detect opposing queens. We can do this by using hash sets, we need a column, diagonal
and anti-diagonal hash set.
'''


res = 0

def n_queens(n: int) -> int:
    dfs(0, set(), set(), set(), n)
    return res

def dfs(r, diagonals_set, anti_diagonals_set, cols_set, n):
    global res
    # on the last row means we have placed all n queens
    if r == n:
        res += 1
        return

    for c in range(n):
        curr_diagonal = r-c # this just is a way to keep track of what diagonal we are in
        curr_anti_diagonal = r+c # and same to keep track of what anti-diagonla we are in

        # if there are queens on the current column, diagonal or anti-diagonal skip this square
        # we do this by checking the column, diagonal and anti-diagonal sets
        if (c in cols_set or curr_diagonal in diagonals_set or curr_anti_diagonal in anti_diagonals_set):
            continue
        # else we can place the queen at this square
        cols_set.add(c)
        diagonals_set.add(curr_diagonal)
        anti_diagonals_set.add(curr_anti_diagonal)

        # recursively move to the next row to continue placing queens
        dfs(r+1, diagonals_set, anti_diagonals_set, cols_set, n)

        # backtrack by removing the queen from that square
        cols_set.remove(c)
        diagonals_set.remove(curr_diagonal)
        anti_diagonals_set.remove(curr_anti_diagonal)



# Example Questions that I am just adding on: Given array of letters, want to see if a word exists or not
class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        def dfs(i: int, j: int, k: int) -> bool:
            # matched all characters
            if k == L:
                return True
            # out of bounds or mismatch
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
                return False

            # mark visited
            tmp = board[i][j]
            board[i][j] = '#'

            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            # unmark visited
            board[i][j] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
