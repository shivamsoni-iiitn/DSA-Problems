class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if(low<high):
            index=self.partition(arr,low,high)
            self.quickSort(arr,low, index-1)
            self.quickSort(arr, index+1, high)
        
    def partition(self, arr, low, high):
        # code here
        pivot=arr[low]
        l,r=low, high
        while l<r:
            while(l<=high and arr[l]<=pivot):
                l+=1
            while(r>=low and arr[r]>pivot):
                r-=1
            if l<r: arr[l],arr[r]=arr[r],arr[l]
        
        arr[r],arr[low]=arr[low], arr[r]
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna