from collections import deque

class Solution:
    # def dfs(self, node, visited,adj,st):
    #     visited[node]=1
    #     for i in adj[node]:
    #         if not visited[i]:
    #             self.dfs(i, visited,adj,st)
    #     st.append(node)
            
    # def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
    #     # Code here
    #     adj = [[] for _ in range(V)]
    #     visited=[0]*V
    #     for i, j in edges:
    #         adj[i].append(j)
    #     st=[]
            
    #     for i in range(V):
    #         if not visited[i]:
    #             self. dfs(i,visited,adj,st)
    #     res=[]
    #     while st:
    #         res.append(st.pop())
    #     return res
    
    #Kahn algo
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Code here
        adj = [[] for _ in range(V)]
        visited=[0]*V
        indegree=[0]*V
        for i, j in edges:
            adj[i].append(j)
            indegree[j]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna