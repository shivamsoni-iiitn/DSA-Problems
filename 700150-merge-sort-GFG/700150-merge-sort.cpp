class Solution {
  public:
    void merge(vector<int>& arr, int l, int mid, int r){
        int a=l, b=mid+1;
        vector<int>temp;
        while(a<=mid && b<=r){
            if(arr[a]<arr[b]){
                temp.push_back(arr[a]);
                a++;
            }
            else{
                temp.push_back(arr[b]);
                b++;
            }
        }
        while(a<=mid){
            temp.push_back(arr[a]);
            a++;
        }
        while(b<=r){
            temp.push_back(arr[b]);
            b++;
        }
        for(int i=l;i<=r;i++){
            arr[i]=temp[i-l];
        }
    }
    
    void mergeSort(vector<int>& arr, int l, int r) {
        // code here
        if(l>=r){
            return;
        }
        int mid=(l+r)/2;
        mergeSort(arr,l,mid);
        mergeSort(arr,mid+1,r);
        merge(arr,l,mid,r);
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna