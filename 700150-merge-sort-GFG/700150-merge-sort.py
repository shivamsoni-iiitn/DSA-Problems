class Solution:
    def merge(self, arr, l, mid,r):
        a, b = l, mid + 1
        temp=[]
        while(a<=mid and b<=r):
            if arr[a]<arr[b]:
                temp.append(arr[a])
                a+=1
            else:
                temp.append(arr[b])
                b+=1
        
        while(a<=mid):
            temp.append(arr[a])
            a+=1
        while(b<=r):
            temp.append(arr[b])
            b+=1
        
        for i in range(l,r+1):
            arr[i]=temp[i-l]
    
    def mergeSort(self, arr, l, r):
        # code here
        if(l>=r):
            return
        mid=(l+r)//2
        self.mergeSort(arr,l, mid)
        self.mergeSort(arr,mid+1, r)
        self.merge(arr,l,mid,r)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna