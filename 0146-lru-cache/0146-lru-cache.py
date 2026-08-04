class LRUCache:
    class Node:
        def __init__(self, _key, _val):
            self.key=_key
            self.val=_val
            self.next=None
            self.prev=None

    def __init__(self, capacity: int):
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity
        self.mpp={}

    def addNode(self, node):
        currnext=self.head.next
        node.next=currnext
        node.prev=self.head
        self.head.next=node
        currnext.prev=node

    def delNode(self, node):
        prevnode=node.prev
        nextnode=node.next
        prevnode.next=nextnode
        nextnode.prev=prevnode

    def get(self, key: int) -> int:
        if key in self.mpp:
            node=self.mpp[key]
            self.delNode(node)
            self.addNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node=self.mpp[key]
            self.delNode(node)
            del self.mpp[key]


        if len(self.mpp)==self.cap:
            lru=self.tail.prev
            self.delNode(lru)
            del self.mpp[lru.key]
        
        self.addNode(self.Node(key, value))
        self.mpp[key]=self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna