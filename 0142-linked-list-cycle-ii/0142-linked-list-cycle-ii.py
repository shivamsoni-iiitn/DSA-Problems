# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        count=0
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                slow=head
                break
        if fast is None or fast.next is None:
            return None   
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
            count+=1
        return slow

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna