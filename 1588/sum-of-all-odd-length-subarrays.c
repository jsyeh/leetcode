int sumOddLengthSubarrays(int* arr, int arrSize){
    //利用 prefix技巧，先把 arr[i] 的內容，變成前i項的和
    for(int i=1; i<arrSize; i++){
        arr[i] += arr[i-1];
    }

    int ans=0;
    for(int i=0; i<arrSize; i++){
        for(int k=i; k<arrSize; k+=2){
            if(i==0) ans += arr[k];
            else ans += (arr[k]-arr[i-1]);
        }
    }
    return ans;
}
