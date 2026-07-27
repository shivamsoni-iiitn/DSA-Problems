class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n=len(val)
        items=[]
        for i in range(n):
            items.append((val[i]/wt[i], val[i], wt[i]))
        
        items.sort(reverse=True)
        count=0
        for i in range(n):
            if capacity==0:
                break
            if items[i][2]<=capacity:
                capacity-=items[i][2]
                count+=items[i][1]
            else:
                count+=items[i][1]*(capacity/items[i][2])
                capacity=0
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna