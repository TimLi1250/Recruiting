# Sorting Algorithms: We want to implement the following sorting algorithms:

# Bubble Sort
# Selection Sort
# Insertion Sort

# Merge Sort
# Quicksort

# Counting Sort
# Radix Sort
# Bucket Sort
# Heap Sort

class SortingAlgorithms:

    '''
    Let's start with Bubble Sort:
    We want to compare adjacent elements and swap them if they are in the wrong order.
    We notice that every pass will lock some element in the correct position. For example, in the first pass, the largest element will be moved to the end of the array.
    In the second pass, the second largest element will be moved to the second last position, and so on.
    '''
    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                # So first pass i = 0, we compare all consecutive elements.
                # In the second pass i = 1, we compare everthing except the last element.
                if arr[j] > arr[j + 1]:
                    temp = arr[j+1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp
        return arr
    '''
    Next, let's implement Selection Sort. It is a little similar to Bubble Sort, but instead of swapping adjacent elements, we find the minimum element
    in the unsorted part of the array and swap it with the first unsorted element.
    '''
    @staticmethod

    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i # We basically want to swap the minimum of the unsorted part with this index at the end of the loop
            # Therefore, in the first pass, we will find the minimum element in the entire array, and do two things:
            for j in range(i+1, len(arr)):

                # 1. If this minimum element is not the first element, we will swap it with the first element
                # 2. If it is the first element, we will just continue to the next
                # In this case, we know the minimum element of the ENTIRE array is at the first index and then we just continue with the rest of the array.
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    '''
    Now let's implement Insertion Sort. Assume the first element is already sorted, we take the second element and insert it either in front of the first element
    or after it. Now we know the first two elements are sorted, we can now take the third element and either insert it in front, between, or after the first two elements.
    We can continue this process until we have sorted the entire array.
    '''
    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            sort_index = i
            # We want to look at the previous sorted part of the array and see where we want to insert the current element
            for i in range(0, i):
                if arr[sort_index] < arr[i]:
                    # We want to insert the current element at the index i-1, but if i is 0, we just want to insert it at the beginning.
                    if i == 0:
                        arr.insert(0, arr[sort_index])
                        arr.pop(sort_index + 1)  # Remove the element that was moved to the end
                    else:
                        arr.insert(i, arr[sort_index])
                        arr.pop(sort_index + 1)
                    break
        return arr

    # This is the better way to implement insertion sort:
    @staticmethod
    def insertion_sort_2(arr):

        # Start from the second element (index 1)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Start from i-1 and keep on shifting elements i-2, i-3, etc. that are > key to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            # Insert the key into its correct position
            arr[j + 1] = key

        return arr

    '''
    Now let's implement Merge sort. This is a divide and conquer algorithm.
    We will divide the array into two halves, sort each half recursively, and then merge the two sorted halves.
    '''
    @staticmethod
    def merge_sort(arr):
        # So if the length of the array is greater than 1, we will first divide the array into two halves
        if len(arr) > 1:

            r = len(arr) // 2
            L = arr[:r]
            M = arr[r:]

            # Sort the two halves, basically we want to start this algorithm with two sorted arrays
            SortingAlgorithms.merge_sort(L)
            SortingAlgorithms.merge_sort(M)

            i = 0
            j = 0
            k = 0
            # Basically we iterate through both halves and compare the elements, if one is smaller than the other, we add it to the new array.
            # If an element is just added from one array, we will go to the next element in that array and then continue comparing.
            while i < len(L) and j < len(M):
                # k is the index of the new array that we are building
                if L[i] < M[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = M[j]
                    j += 1
                k += 1
            # Now, we need to consider the case where one of the halves has more elements than the other so we will add the remaining elements to the new array
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(M):
                arr[k] = M[j]
                j += 1
                k += 1
        return arr
    '''
    Time for Quick Sort. This is also a divide and conquer algorithm but instead of dividing the array into two halves, we will choose a pivot
    element and partition the array into two parts: elements less than the pivot and elements greater than the pivot.
    '''
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low  # Index of smaller element
        for j in range(low, high):
            # If the current element is smaller than or equal to the pivot, we will swap it with the element at index i
            if arr[j] <= pivot:

                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # Finally, we will swap the pivot element with the element at index i
        arr[i], arr[high] = arr[high], arr[i]
        return i


    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:
            # Partition the array and get the index of the pivot element
            pi = SortingAlgorithms.partition(arr, low, high)

            # Recursively sort the elements before and after partition
            SortingAlgorithms.quick_sort(arr, low, pi - 1)
            SortingAlgorithms.quick_sort(arr, pi + 1, high)
        return arr

    def kth_smallest(arr, low, high, k):
        if (k > 0 and k <= high - low + 1):

            index = SortingAlgorithms.partition(arr, low, high)
            # If the index is equal to k-1, we have found the kth smallest element
            if (index - low == k - 1):
                return arr[index]
            # If the index is greater than k-1, we need to search in the left part of the array
            if (index - low > k - 1):
                return SortingAlgorithms.kth_smallest(arr, low, index - 1, k)
            # If the index is less than k-1, we need to search in the right part of the array
            return SortingAlgorithms.kth_smallest(arr, index + 1, high, k - index + low - 1)

# Example usage of the sorting algorithms
data = [-2, 45, 0, 11, -9, 8, 23, 74, 18, -90, -67, 55, 34]
bubble_sorted_data = SortingAlgorithms.bubble_sort(data)
print("Bubble Sorted Data:", bubble_sorted_data)
selection_sorted_data = SortingAlgorithms.selection_sort(data)
print("Selection Sorted Data:", selection_sorted_data)
insertion_sorted_data = SortingAlgorithms.insertion_sort(data)
print("Insertion Sorted Data:", insertion_sorted_data)
merge_sorted_data = SortingAlgorithms.merge_sort(data)
print("Merge Sorted Data:", merge_sorted_data)
quick_sorted_data = SortingAlgorithms.quick_sort(data, 0, len(data) - 1)
print("Quick Sorted Data:", quick_sorted_data)
kth_smallest_element = SortingAlgorithms.kth_smallest(data, 0, len(data) - 1, 5)
print("5th Smallest Element:", kth_smallest_element)
