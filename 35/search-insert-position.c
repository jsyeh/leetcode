int searchInsert(int* nums, int numsSize, int target){
    return binarySearch(nums, target, 0, numsSize);
}
int binarySearch(int* nums, int target, int left, int right){
    int mid = (left+right)/2;
    if(left>=right) return left;

    if(nums[mid]==target) return mid;
    else if(nums[mid]<target){
        return binarySearch(nums, target, mid+1, right);
    }else{
        return binarySearch(nums, target, left, mid);
    }
}
