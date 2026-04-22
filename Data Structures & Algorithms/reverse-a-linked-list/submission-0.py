# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # main idea: reverse the pointers to point backwards
    # traverse through the loop until you reach a null
    # Keep track of 3 things: 1) curr mode 2) next node 3) previous node
    # steps:
        # Traverse the list while cur is not None
        # Save the connection to the next node
        # Reverse the curr node to point to prev node
        # Move forward
        
        curr = head
        prev = None

        while curr is not None:
            # save link to next node
            nextNode = curr.next

            # reverse the pointer   
            curr.next = prev 

            # move forward
            prev = curr 
            curr = nextNode 

        head = prev
        return head

       
