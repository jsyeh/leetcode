/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int* ans = (int*) malloc(sizeof(int)*2);

    int left = 0, right = numsSize;
    while(left<right) {
        int mid = (left+right)/2;
        if(nums[mid]==target){
            left = mid;
            break;
        }
        if(nums[mid]<target) left = mid+1;
        else right = mid;
    }
    if(left>=right) {
        ans[0] = -1;
        ans[1] = -1;
        return ans;
    }
    for(right = left; right<numsSize; right++){
        if(nums[left]!=nums[right]) {
            right = right - 1;
            break;
        }
    }
    if(right>=numsSize) right--; //超過邊界，要拉回來

    for( ; left>=0; left--){
        if(nums[left]!=nums[right]) {
            left = left + 1;
            break;
        }
    }
    if(left<0) left++; //超過邊界，要拉回來

    ans[0] = left;
    ans[1] = right;
    *returnSize = 2;
    return ans;
}//case 4/88: [1] 1
