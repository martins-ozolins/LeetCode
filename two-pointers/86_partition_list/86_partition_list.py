# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads for two separate lists:
        # smaller: nodes with val < x
        # larger: nodes with val >= x
        small_head = small_tail = ListNode(0)
        large_head = large_tail = ListNode(0)

        current = head

        # Traverse the original list and partition nodes
        while current:
            if current.val < x:
                # Append to the 'smaller' list
                small_tail.next = current
                small_tail = small_tail.next
            else:
                # Append to the 'larger' list
                large_tail.next = current
                large_tail = large_tail.next

            current = current.next

        # End the 'larger' list
        large_tail.next = None

        # Connect smaller list to larger list
        small_tail.next = large_head.next

        # The real head is the next of small_head dummy
        return small_head.next
