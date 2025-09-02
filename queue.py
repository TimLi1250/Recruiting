'''
Let's take a look at queues. This is a first in and first out data structure.

We can most commonly use a queue as defined below.
'''

from collections import deque

my_queue = deque()
my_queue.append(0)
my_queue.append(1)
my_queue.append(2)
# should be (0, 1, 2)
print(my_queue)
# adds a 1 in the front and then a 2 in the front
my_queue.appendleft(1)
my_queue.appendleft(2)
# should be (2, 1, 0, 1, 2)
print(my_queue)
# pops off the last two elements
my_queue.pop()
my_queue.pop()
# should be (2, 1, 0)
print(my_queue)
# pops off the first two elements
my_queue.popleft()
my_queue.popleft()
# should now be just (0)
print(my_queue)

'''
Let's look at the question, sliding window maximum. We have an array and an integer k that represents the length of the sliding window.
We want to return a list that contains the maximum element in the window at each step.

'''

def sliding_window_max(nums, k):
    my_queue = deque()
    res = []

    # we want to access the index and the value, i will be the index and n will be the value
    for i, n in enumerate(nums):
        while my_queue and nums[my_queue[-1]] < n:
            my_queue.pop()
        my_queue.append(i)
        if my_queue[0] == i - k:
            my_queue.popleft()
        if i >= k-1:
            res.append(nums[my_queue[0]])
    return res