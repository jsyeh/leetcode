int peakIndexInMountainArray(int* arr, int arrSize){
    return binarySearch(arr, 0, arrSize-1);
}
int binarySearch(int* arr, int left, int right){
    printf("%d - %d\n", left, right);
    /*if(right-left==3){
        if(arr[left]>arr[left+1]) return left;
        if(arr[right]>arr[right-1]) return right;
        return left+1;
    }*/
    int mid = (left+right)/2;
    if(arr[mid-1]>arr[mid]) return binarySearch(arr, left, mid);
    else if(arr[mid+1]>arr[mid]) return binarySearch(arr, mid, right);
    else return mid;
}
