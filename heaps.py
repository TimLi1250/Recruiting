'''
Let's take a look at heaps

There are two types of heaps:
1. Min heap (smallest element at top)
2. Max heap (greatest element at top)

(Heaps will normally all be created as a min heap. To make a max heap, we can just negate everything we insert and
then at the end make sure to reverse back to original)

'''

# Let's take a look at some common methods to run on heap
import heapq

class Heap:
    heap = [2, 5, 6, 1, 10, 29, 83]

    heapq.heapify(heap)
    # pops the min/max element out of the heap
    heapq.heappop(heap)
    # adds an element to the heap
    heapq.heappush(heap, 7)
    # pushes an element and then pops the max/min element
    heapq.heappushpop(heap, 7)

# however, let's say our heap is not just an array of integers but rather an dictionary
# for example:
    dictionary = {}
    dictionary["hello"] = 5
    dictionary["tim"] = 3
    dictionary["worlds"] = 6
    dictionary["I"] = 1

    # we can then make a heap from this by doing this:
    heap2 = [(v, k) for k, v in dictionary.items()] # remember .items() gives you the entire key value pair
    # then we can just run heapify on this heap
    heapq.heapify(heap2)
    # heapq will always sort by first element in the tuple first and then if that is tied, it will sort by the second element
    # so in this case it will sort by the integer first and then sort lexicographically

'''
Let's take a look at the problem, k most frequent strings. Given a list of strings i.e. ["go", "I", "hello", "I", "go"], we want to
return the k most frequent ones.

The easy way to do this question is just first make a hashmap that keeps (str, frequency) and then convert that into a maxheap and pop k elements.

Another way we can do this question is by actually using a minheap to reduce space.
In this solution, we restrict the size of the minheap such that if it is greater than k, we discard the lowest frequency string.

Here we just iterate through the hashmap and look at if the following steps are possible.
1. If the heap has less than k elements, add it to the heap
2. If the heap has more than k elements, pop off the min frequent element and then add the current element to the heap.

At the end, we can just pop everything out of the heap to return the k most frequent elements.
'''

'''
Now let's look at the question combine sorted linked lists.
For example, given the linked list 1 -> 6, 1 -> 4 -> 6, and 3 -> 7,
I want to make the list 1 -> 1 -> 3 -> 4 -> 6 -> 6 -> 7.

At first glance we can just add every single element into a minheap and pop every element out from that minheap.
However, this is waste of space because we don't take into account that the lists are already sorted themselves.

Instead we can just create a minheap based on the first element in each list. Then we pop out the minimum element from the minheap and
add the next element in that list to the minheap.

'''

def combine_sorted_linked_lists(lists):
    heap = []
    for heads in lists:
        if heads is not None:
            heapq.heappush(heap, heads)
    dummy = ListNode(-1)
    curr = dummy
    while heap:
        # pop the smallest node
        smallest_node = heapq.heappop(heap)
        # add this node to our list
        curr.next = smallest_node
        curr = curr.next
        # add the next node of the node we just popped into the heap
        if smallest_node.next is not None:
            heapq.heappush(heap, smallest_node.next)
    return dummy.next

'''
Now let's tackle the question: finding the median of an integer stream
So this would originally be easy to do in O(n), but we aim for a solution that takes O(log(n))

We observe that there are two cases when computing the median.
If the length of the integer stream is even, the two numbers we use to compute the median are
1. the largest of the left half (max heap)
2. the smallest of the right half (min heap)

If the length of the integer stream is odd, we only have one number to represent the median.
In this case we can just store this in the max heap.

Therefore, to implement this problem we just need to follow the rules below.
1. The maximum value in the max-heap (representing the left half) must be less than equal to the minimum
value of the min-heap (right half)
2. Heaps should either be EQUAL size or the max-heap has ONE more element than the min-heap
(Note this does not follow the other way, the min-heap can not have one more element than the max-heap)
'''