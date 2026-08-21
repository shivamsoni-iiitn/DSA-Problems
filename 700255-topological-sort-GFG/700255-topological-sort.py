class Solution:
    def dfs(self, node, visited,adj,st):
        visited[node]=1
        for i in adj[node]:
            if not visited[i]:
                self.dfs(i, visited,adj,st)
        st.append(node)
            
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Code here
        adj = [[] for _ in range(V)]
        visited=[0]*V
        for i, j in edges:
            adj[i].append(j)
        st=[]
            
        for i in range(V):
            if not visited[i]:
                self. dfs(i,visited,adj,st)
        res=[]
        while st:
            res.append(st.pop())
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna