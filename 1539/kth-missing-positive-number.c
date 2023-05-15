int findKthPositive(int* arr, int arrSize, int k){
    int N = 1;
    for(int i=0; i<arrSize; i++){
        //printf("arr[i]:%d N:%d k:%d\n", arr[i], N, k);
        if(arr[i]>N){
            if(arr[i]-N==k) return arr[i]-1;
            if(arr[i]-N>k) return N+k-1;
            else {
                k -= arr[i]-N;
                N = arr[i]+1;
            }
        }else N++;
    }
    return N+k-1;
    //return arr[arrSize-1]+k;
}
//cae 72/86: [2] 1
