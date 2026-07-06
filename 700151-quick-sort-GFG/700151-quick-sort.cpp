class Solution {
  public:
    void quickSort(vector<int>& arr, int low, int high) {
        // code here
        if(low<high){
            int index=partition(arr,low,high);
            quickSort(arr, low, index-1);
            quickSort(arr, index+1, high);
        }
    }

    int partition(vector<int>& arr, int low, int high) {
        // code here
        int pivot=arr[low];
        int l=low, r=high;
        while(l<r){
            while(l<=high && pivot>=arr[l]) l++;
            while(r>=low && pivot<arr[r]) r--;
            if(l<r) swap(arr[l], arr[r]);
        }
        swap(arr[r],arr[low]);
        return r;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna