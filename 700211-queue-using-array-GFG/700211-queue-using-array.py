class myQueue:
    def __init__(self, n):
        self.q = [0] * n
        self.size = n
        self.start = -1
        self.end = -1

    def isEmpty(self):
        return self.start == -1

    def isFull(self):
        return (self.end + 1) % self.size == self.start

    def enqueue(self, x):
        if self.isFull():
            return

        if self.isEmpty():
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.size

        self.q[self.end] = x

    def dequeue(self):
        if self.isEmpty():
            return -1

        x = self.q[self.start]

        # Last element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.size

        return x

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.start]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[self.end]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna