''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self, head):
        curr=head
        prev=None
        while curr:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev
            
        
    def addOne(self,head):
        # code here
        head=self.reverse(head)
        curr=head
        carry=1
        while curr:
            summ=curr.data+carry
            carry=summ//10
            curr.data=summ%10
            if curr.next==None and carry:
                curr.next=Node(carry)
                curr=curr.next
            curr=curr.next
            
            
        head=self.reverse(head)
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna