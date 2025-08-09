'''
Two pointer

There are three main strategies for the two-pointer technique:

1. Inward traversal: This method involves starting from both ends and moving towards the middle.

2. Unidirectional traversal: This approach uses one pointer to traverse the array while the other pointer is used to track a condition or state.
(An example of this would be using a slow and fast pointer)

3. Staged traversal: Traverse one pointer and after a certain condition is met, we can move the second pointer.

We should use this when we have
1. a linear data structure
2. a PREDICTABLE data structure i.e. sorted or palindrome

'''

# Let's take a look at the triplet sum problem. We want to find all unique triplets in an array that sum to zero.
# For example, we can have an triplet [-1, 1, 0] or [-1, 4, -3]

def find_triplet_sum(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        # This is because we are looking for triplets, if the current number is greater than 0, we can break out of the loop

        if arr[i] > 0:
            break
        # We need to avoid duplicates so let's say we have our "a" value be -4. We want to keep iterating past
        # that number until we find a new number to use as "a" in our triplet.
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        pairs = find_pairs(arr, i + 1, -arr[i])
        for pair in pairs:
            triplets.append([arr[i], pair[0], pair[1]])
    return triplets

def find_pairs(arr, starts, target):

    pairs = []
    start, end = starts, len(arr) - 1
    while start < end:
        current_sum = arr[start] + arr[end]
        if current_sum == target:
            pairs.append([arr[start], arr[end]])
            start += 1
            # Same thing here, we want to avoid duplicates so
            # we keep moving the start pointer until we find a new number
            while start < end and arr[start] == arr[start - 1]:
                start += 1

        elif current_sum < target:
            start += 1
        else:
            end -= 1

    return pairs

'''
Now let's look at the dreaded problem: LARGEST CONTAINER
The problem is as below:
You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
Find two lines which, together with the x-axis, form a container that holds the most water.

I think the hard part to recognize about this question is that we just need to save the maximum area we can find
instead of trying to update the maximum area every time we find a new pair of lines.

'''
def largest_container(arr):
    start, end = 0, len(arr) - 1
    max_area = 0

    while start < end:
        width = end - start
        height = min(arr[start], arr[end])
        area = width * height
        max_area = max(max_area, area)

        # And now we have three cases to update our two pointer technique:
        if arr[start] == arr[end]:
            start += 1
            end -= 1
        elif arr[start] < arr[end]:
            start += 1
        else:
            end -= 1

    return max_area