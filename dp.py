'''
Perhaps one of the most important topics: Dynamic Programming

Dynamic Programming is similar to recursion in the aspect where we are trying to break a big problem into numerous little subproblems
However, it stores the solutions to each subproblem so that they can be reused when they're needed again.

It usually has these characteristics:
1. The optimal solution to a problem can be constructed from the optimal solution to its subproblems
2. The same subproblems are solved repeatedly during the problem solving process.
3. There is a recurrence relation i.e. a formula that expresses the solution to the problem in terms of the solutions to its subproblems
4. Base Cases
'''


'''
Let's look at some common questions.
1. Climbing stairs: Number of distinct ways to climb n steps by taking either 1 or 2 at a time

To approach this question, we want to notice that to get to step i, we need to either get to step i-1 or i-2.
Then we want to identify the base cases where there are 1 way to get to step 1 and 2 ways to get to step 2.
Furthermore, here we notice that there are several subproblems that are solved repeatedly. We can get around this by
using memoization -> we can store this information in a hash map
'''
memo = {}
def climbing_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo.get(n) # or memo[n]

    memo[n] = climbing_stairs(n-1) + climbing_stairs(n-2)
    return memo[n]

'''
Here we need to consider two approaches to dynamic programming.

1. The approach above is called the Top-Down approach which is also known as Memoization.
In this approach, we write your solution recursively (divide and conquer). When you compute a subproblem, you store the result
If that subproblem is needed again, you look it up instead of recomputing.

Start with the original problem -> recursively break into subproblems -> cache results.

2. The second approach which we will depict with the solution below is called the Bottom-Up appraoch which also known as Tabulation.
In this approach, we explicitly build a table of subproblem answers. We start with the simplest base cases and iteratively fill up the table
until the final answer.

Start with base cases -> iteratively compute larger subproblems -> reach the final solution.
'''

def climbing_stairs_2(n: int) -> int:

    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    if n <= 2:
        return dp[n]
    else:
        for i in range (3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# We can actually optimize this because we don't need to store an entire array of previous subproblems. We just need to know what the
# value of dp[i-1] and dp[i-2] are so we can just use two variables and constantly replace them.

def climbing_stairs_2_optimized(n: int) -> int:
    one_before, two_before = 2, 1
    if n <= 2:
        return n
    for i in range(3, n+1):
        current = one_before + two_before
        two_before = one_before
        one_before = current
    return one_before

'''
2. Minimum Coin Combination: given an array of coin values and a target amount of money, return the minimum amount needed to reach the target

To approach this question, let's say we have the array [1, 2, 3] and a target amount 5. Then we have 3 cases:
* if we use a 1, we have 1 + coin_combination(5-1)
* if we use a 2, we have 1 + coin_combination(5-2)
* if we use a 3, we have 1 + coin_combination(5-3)

Therefore if we want the overall minimum, we just take 1 + min (coin_combination(4), coin_combination(3), coin_combination(2))
'''

# Let's first look at the Top-Down approach:
memo = {}

def min_coin_combination(coins, target):
    res = dp(coins, target, {})
    return -1 if res == float('inf') else res

def dp(coins, target, memo):
    # Base case
    if target == 0:
        return 0
    # Memoization
    if target in memo:
        return memo.get(target)
    min_coins = float('inf')

    # calculate minimum number of coins if we use current coin
    for coin in coins:
        if coin <= target:
            min_coins = min(min_coins, 1 + dp(coins, target - coin, memo))

    memo[target] = min_coins
    return memo[target]

# Now let's look at the Bottom-Up approach:
def min_coin_combination_2(coins, target):
    # minimum amount of coins needed for each amount
    dp = [float('inf')] * (target+1)
    dp[0] = 0
    for t in range(1, target+1):
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], 1 + dp[t-coin])
    return dp[target] if dp[target] != float('inf') else -1

'''
3. Matrix Pathways: top left of a mxn matrix and we want to find the number of unique pathways to reach the bottom-right corner of a matrix

To approach this question, we need to see that in order to be at the position [i][j], we must've been before at [i-1][j] or [i][j-1].
Therefore, our dp solution is dp[r][c] = dp[r-1][c] + dp[r][c-1].
Furthermore we have the base cases dp[0][x] = dp[x][0] = 1
'''

def matrix_pathways(m, n):
    # set the base case
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
# again we can perform optimizations by only storing the current row and the previous row

'''
4. Neighborhood Burglary: Rob the maximum amount of cash from an array of houses but can't rob adjacent houses.

To approach this question, we should look at what happens at house i.
* If we rob house i, we now have total_stolen(i-2) + house[i].
* If we DON'T rob house i, we now have total_stolen(i-1)

Therefore our dp solution is: dp[i] = max(dp[i-1], houses[i] + dp[i-2])
Furthermore, we have the base cases: dp[0] = houses[0] and dp[1] = max(houses[0], houses[1])
'''

def neighborhood_burglary(houses) -> int:
    # base cases
    if not houses:
        return 0

    if len(houses) == 1:
        return houses[0]

    dp = [0] * len(houses)
    dp[0], dp[1] = houses[0], max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i-1], houses[i] + dp[i-2])

    return dp[len(houses)-1]

'''
5. Longest Common Subsequence. Given two strings, find the length of the longest common subsequence.
Let's approach this question by looking at an example.
Let's say str1 = "acabac" and str2 = "aebab"

Now we can start by comparing the first letter of each string.
    1. Now if they are the same, we know we can include this letter in the LCS of the two strings that come after that letter. Therefore, we get a dp solution of
        if str1[i] == str2[j]:
            LCS(i, j) = 1 + LCS(i+1, j+1)
    2. Now if they are different, we know the LCS can not include both of the characters. Therefore, we need to look at what happens if we
    exclude one of them. Therefore, our dp solution for this case would be
        if str1[i] != str2[j]:
            LCS(i, j) = max(LCS(i+1, j), LCS(i, j+1))

Now let's look at the base case, we know that the longest common subsequence between any string and an empty string is 0. Therefore, we can
have the base cases dp[len(str1)][j] = 0 and dp[i][len(str2)] = 0.
Here we populate our 2D dp array in reverse order.
'''

'''
6. Longest Palindrome in a string. So we just want to return the longest palindromic substring that exists within a string.

To approach this question, we need to look at what makes a string a palindrome.
We can see that in order for a str[i:j] to be a palindrome, str[i] must equal str[j] and furthermore, str[i+1:j-1] must also be a palindrome

Therefore, we can set up a dp solution: dp[i][j] is True if s[i] == s[j] and also dp[i+1][j-1] is True

For base cases, we know a substring of length 1 is a palindrome and a substring of length 2 is a palindrome if both elements are the same.
'''

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n == 0 :
        return ""
    # sets the entire dp matrix to False for now
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start_index = 0
    # Base case 1 element
    for i in range(n):
        dp[i][i] = True
    # Base case 2 elements
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_len = 2
            start_index = i

    # loop through palindromic strings that are length 3 or higher
    for sub_str_len in range(3, n+1):
        for i in range(n-sub_str_len+1):
            j = i+sub_str_len-1

            # dp condition checks
            if s[i] == s[j] and dp[i+1][j-1] == True:
                dp[i][j] = True
                max_len = sub_str_len
                start_index = i
    return s[start_index: start_index + max_len]

# OPTIMIZATION: you can do for this problem is realize that the center to any palindrome will either be a single character like a
# or two characters like bb. Therefore we can set the left and right pointers at the center and expand outward. When we expand outward
# we can check if it is still a palindrome.

'''
7. Maximum Subarray Sum: Given an array of integers, return the sum of the subarray with the largest sum.

To approach this problem we need to realize that at every index in the array, we can choose to add the number to the ongoing subarray sum
or we can restart. Therefore, the dp solution is dp[i] = max(dp[i-1]+nums[i], nums[i]). dp[i] in this case will refer to the maximum
sum of any subarray that ENDS at i.

For our base case, we know that any subarray that ends at index 0 will just be the number itself so dp[0] = nums[0].
'''

def maximum_subarray(nums) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

'''
8. 0/1 Knapsack: You want to rob a store but has a knapsack that has a maximum capacity. All the items in the store have designated weights
and amount. Your job is to maximize the amount.

Let's approach this problem with an example. Suppose we had four items, let's say like shown:
* 0: ($70, w = 5)
* 1: ($50, w = 3)
* 2: ($40, w = 4)
* 3: ($30, w = 1)

Let the function knapsack(i, cap) represent the maximum amount with items starting from index i and a knapsack capacity of cap.
Then our job is to figure out what knapsack(0, 7) is. Now let's say in the problem above that we select item 0.
Then, knapsack(0, 7) will be equal to 70 + knapsack(1, 7-5).
Therefore, if we generalize, we can say that if we select the ith item, the most value we can get is value[i] + knapsack(i+1, c-weights[i])

If we EXCLUDE element i, then the most we can get is knapsack(i+1, c)

Now let's consider the base cases. When i = n, then we get dp[n][c]. This case means we are considering 0 elements to add to the knapsack,
so we can set that to 0. Furthermore, dp[i][0] = 0 because no items can fit into a knapsack of capacity 0.
'''

def knapsack(capacity, weights, values) -> int:
    n = len(values)
    # set our base cases
    dp = [[0] for x in range(capacity+1) for x in range(n+1)]

    for i in range(n-1, -1 , -1):
        for c in range(1, capacity+1):
            if weights[i] <= c:
                dp[i][c] = max(values[i] + dp[i+1][c-weights[i]], dp[i+1][c])
            # here we run into the case where we have no more room to fit the item in the knapsack
            else:
                dp[i][c] = dp[i+1][c]
    return dp[0][capacity]
