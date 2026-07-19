class Solution:
    def finddfs(self, adj, visited,idx, res):
        visited[idx]=True
        res.append(idx)
        for i in adj[idx]:
            if visited[i]==False:
                self.finddfs(adj, visited,i,res)
        
    def dfs(self, adj):
        # code here
        visited=[False]*len(adj)
        res=[]
        self.finddfs(adj, visited,0,res)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna