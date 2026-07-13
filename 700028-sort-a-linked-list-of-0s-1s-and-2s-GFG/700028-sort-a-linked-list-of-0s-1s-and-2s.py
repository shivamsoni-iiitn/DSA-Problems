'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        zero=Node(-1)
        zerotail=zero
        ones=Node(-1)
        onestail=ones
        twos=Node(-1)
        twostail=twos
        curr=head
        
        while curr:
            if curr.data==0:
                zerotail.next=curr
                zerotail=curr
            elif curr.data==1:
                onestail.next=curr
                onestail=curr
            else:
                twostail.next=curr
                twostail=curr
            curr=curr.next
        
        twostail.next=None
        
        zerotail.next=ones.next if ones.next else twos.next
        onestail.next=twos.next
        twos.next=None
        head=zero.next
        
        return head
                    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna