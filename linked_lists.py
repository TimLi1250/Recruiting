'''
Let's take a look at linked lists.

There are two types of linked list: singly linked lists and doubly linked lists.
(singly linked list O(1) for removing head, O(n) for removing tail and doubly linked list O(1) for removing both head and tail)

We can start with a simple example: reversing a singly linked list.

Let's say our linked list looks like this: 1 -> 2 -> 3 -> null
To reverse it, we want it to look like this: null <- 1 <- 2 <- 3 or easier to understand: 3 -> 2 -> 1 -> null

To do this we need to perform the following steps for every single node in the linked list:
1. Keep track of the NEXT node.
2. Set the NEXT node of the current node to the PREVIOUS node.
3. Move the PREVIOUS node to the current node.

So let's look at this in our example:
We know the previous node of the first node is None (null).

(prev) null -> (current) 1 -> (next) 2 -> 3

Now we first want to save our next node, which is 2.
Then we want to set the next node of the current node (1) to the previous node (null)

(prev) null <- (current) 1 -> (next) 2 -> 3

Now we want to move the previous node to the current node (1), and the current node to the next node (2).

null <- (prev) 1 -> (current) 2 -> 3

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next  # Step 1: Keep track of the NEXT node
        current.next = previous    # Step 2: Set the NEXT node of the current node to the PREVIOUS node
        previous = current         # Step 3: Move the PREVIOUS node to the current node
        current = next_node        # Move to the next node

    return previous  # The new head of the reversed linked list

'''
We can also do this problem with recursion.
Let's assume we have the linked list: 1 -> 2 -> 3 -> null.
We want to run the following recusive call: new_head = reverse_linked_list(head.next) i.e. we want to reverse the list: 2 -> 3 -> null.
Therefore, we should have something that looks like this: (head) 1 -> 2 <- 3 (new head).
Here, we just need to reverse the direction between 1 -> 2, and we can do this by setting head.next.next = head.
So now we have (head) 1 -> <- 2 <- 3 (new head).
Finally, we need to set head.next = None so that first node points to None

'''

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head  # Base case: if the list is empty or has one node, return head

    new_head = reverse_linked_list_recursive(head.next)  # Recursive call
    head.next.next = head  # Reverse the direction
    head.next = None  # Avoid cycle (more so the first node points to None)

    return new_head  # Return the new head of the reversed linked list

'''
One common strategy in linked list questions is to use the "slow and fast pointer" technique.
For example, for the problem remove the kth node from the end of the linked list, we can use two pointers:
1. Move the fast pointer k steps ahead.
2. Move both pointers until the fast pointer reaches the end of the list.
3. The slow pointer will now be at the node before the kth node from the end.
'''

'''
Now let's look at finding the intersection of two singly linked lists.
Here it is IMPORTANT to recognize that the tail ends of both linked lists must be the same if they intersect.
Therefore, our job is to basically be at a node such that the remaining length of both linked lists is the same.
We can do this by putting a pointer at the head of both linked lists, and when one pointer reaches the end of its linked list, we set it to the head of the other linked list.
i.e. pointer A first traverses A and then B, while pointer B first traverses B and then A.
When they meet, they will be at the intersection node.

'''
def linked_list_intersection(headA, headB):
    if headA is None or headB is None:
        return None

    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        # This basicallly means if pointerA reaches the end of its linked list, we set it to the head of the other linked list
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA  # Can be the intersection node or None if they don't intersect

# Finally we can also combine data structures with linked list. For example, to implement a LRU Cache,
# we want to combine a hash map with a doubly linked list.