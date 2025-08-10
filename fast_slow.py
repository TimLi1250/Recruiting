'''
We can briefly discuss fast and slow pointers. These are often used to do linked list problems.

Usually the slow pointer moves one step at a time, while the fast pointer moves two steps at a time.

One really common problem is to determine if a linked list has a cycle.
If there is a cycle, the fast pointer will eventually meet the slow pointer.
If there is no cycle, the fast pointer will reach the end of the list.
'''

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def FloydsCycle(head):
    if not head:
        return False

    slow = head
    fast = head

    # Move slow pointer one step and fast pointer two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False