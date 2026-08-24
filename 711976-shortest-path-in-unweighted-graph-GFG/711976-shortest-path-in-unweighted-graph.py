from collections import deque, defaultdict

class Solution:
    def shortestPath(self, V, edges, src, dest):
        # code here
        dis=[float('inf')]*V
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        q=deque()
        dis[src]=0
        q.append(src)
        while q:
            node=q.popleft()
            for i in adj[node]:
                if dis[i]>dis[node]+1:
                    dis[i]=dis[node]+1
                    q.append(i)
        
        for i in range(V):
            if dis[i]==float('inf'):
                dis[i]=-1
        
        return dis[dest]
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna