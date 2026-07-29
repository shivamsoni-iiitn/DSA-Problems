int findMaxConsecutiveOnes(int* nums, int n) {
    int len=0;
    int maxi=0;
    for(int i=0;i<n;i++){
        if(nums[i]==1){
            len++;
        }
        else{
            len=0;
        }
        maxi=fmax(maxi, len);
    }
    return maxi;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna