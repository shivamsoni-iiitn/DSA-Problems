void swap(int *a, int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void selectionSort(int arr[], int n) {
    // Code here
    
    for(int i=0;i<n;i++){
        int mini=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[mini]){
                mini=j;
            }
        }
        swap(&arr[i],&arr[mini]);
    }
    return;
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna