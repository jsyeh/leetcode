// LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
// 將 nums 切成 3 段 subarray，希望3段的「第1個」加起來最小。
int minimumCost(int* nums, int numsSize) {
    int min1 = nums[1], min2 = nums[2];
    if(min1>min2) {
        int temp = min1;
        min1 = min2;
        min2 = temp;
    }
    for(int i=3; i<numsSize; i++) {
        if(nums[i]<min1) {
            min2 = min1;
            min1 = nums[i];
        } else if(nums[i]<min2) {
            min2 = nums[i];
        }
    }
    return nums[0] + min1 + min2;
}
