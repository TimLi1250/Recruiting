'''
Let's take a look at prefix sums.

Usually we can define a prefix sum like this:
'''

def compute_prefix_sums(list):
    prefix_sums = []
    prefix_sums.append(list[0])

    for i in range (1, len(list)):
        prefix_sums.append(prefix_sums[i-1] + list[i])

# Prefix sums are usually used to determine the sum of subarrays

'''
Let's look at this simple question, Sum between range: Given an integer array, write a function which returns the sum of values between two indexes

We can do this question by calculating the prefix sum and then computing the difference at certain indexes in the prefix sum.
'''

'''
Now we can look at a slightly harder question, find the number of subarrays in the integer array that sum to k
We know that the sum of a subarray between two indexes, i and j can be calculated like so:
sum[i: j] = prefix_sum[j] - prefix_sum[i-1]

sum[0: j] = prefix_sum[j] (here we can't subtract prefix_sum[0-1] as that index is out of bounds). However we can do this by
adding a 0 as the first element of the prefix_sum

Then our solution could be to loop throguh every single (i, j) pair in the prefix_sum which would result in a time complexity of O(N^2)

However, we can do better by using a hash map. (This process is similar to the two-sum question)
1. Update curr_prefix_sum by adding the current value of the array to it
2. If curr_prefix_sum - k exists in the hash map, we can add its frequency to count
3. Add (curr_prefix_sum, freq) to the hash map

'''

def k_sum_subarrays(nums, k):
    count = 0
    # need to add the key-value pair (0: 1) to account for subararys that sum to k from the start of the array
    prefix_sum_map = {0: 1}
    curr_prefix_sum = 0
    for num in nums:
        curr_prefix_sum += num
        if curr_prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[curr_prefix_sum-k]

        freq = prefix_sum_map.get(curr_prefix_sum, 0)
        prefix_sum_map[curr_prefix_sum] = freq + 1
    return count

'''
There are also prefix products and in this case, instead of appending 0, we can just append 1.
'''