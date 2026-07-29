int removeDuplicates(int* nums, int n) {
    int idx=0;
    for(int i=1;i<n;i++){
        if(nums[idx]!=nums[i]){
            idx++;
            nums[idx]=nums[i];
        }
    }
    return idx+1;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna