'''
Let's take a look at binary search.

We need to always follow these steps:
1. Define the search space.
2. Define the behavior inside the loop narrowing the search space.
3. Choose an exit condition for the while-loop
4. Return the correct value.

When we are narrowing the search space, we can either move the right pointer to the middle index or the left pointer to the middle index,
depending on whether we are looking for a value that is less than or greater than the middle value.

mid is usually defined as : (left + right) // 2

'''

'''
Let's start by looking at an example: Finding the insertion index of a target value in a sorted array.
If the array contains the target value, we return its index.
If the target value is not present, we return the index where it would be inserted.

'''

def search_insert(nums, target):

    # start by setting left and right pointers
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        # If the midpoint element is less than the target, move the left pointer to the right
        #  because we need to look for elements that are greater than or equal to the target
        elif nums[mid] < target:
            left = mid + 1
        # If the midpoint element is greater than OR EQUAL to the target, move the right pointer to the middle
        # because we need to look for elements that are less than the target
        else:
            right = mid

    return left

'''
Now let's look at the question: Find the first and last occurences of a number in a sorted array.
For example if we have an array [5, 7, 7, 8, 8, 8, 9, 10] and we want to find the first and last occurences of the number 8

For our binary search, we can perform two separate searches:
1. One to find the first occurrence of the target value.
2. Another to find the last occurrence of the target value.


'''

def search_range(nums, target):

    def find_first(nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # if the middle is less than the target, we need to move the left pointer to the right

            if nums[mid] < target:
                left = mid + 1
            else:
            # on the other hand, if the middle is greater than or equal to the target,
            # we need to move the right pointer to the middle
                right = mid
        return left if left < len(nums) and nums[left] == target else -1

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1 # Note the +1 to bias towards the right
            # so now we do the opposite, if the middle is greater than the target, we move the right pointer to the left
            if nums[mid] > target:
                right = mid - 1
            else:
            # else we move the left pointer to the middle
                left = mid
        return left if left < len(nums) and nums[left] == target else -1

    first = find_first(nums, target)
    last = find_last(nums, target)

    return [first, last]

'''

REMEMBER the search space for binary search may not be very obvious at first glance. Sometimes, it can be tricky to define the search space correctly.
For example, let's look at the cutting wood question where we need to find the maximum length of wood that can be cut from a set of logs such that the total number of pieces is at least a given number k.

Here we want to perform binary search on the length of the wood pieces, not on the indices of the logs.
We can define the search space as the range from 1 to the maximum length of the logs.

There are many other questions like these such as Koko eating bananas, or the minimum time to finish all tasks, where we need to define the search space carefully.

In another example, to find a target in a rotated sorted array,
We KNOW whether to search in the left or right half of the array by seeing whether or not the left or right half is sorted.

'''