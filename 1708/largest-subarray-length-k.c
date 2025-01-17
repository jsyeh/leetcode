// LeetCode 1708. Largest Subarray Length K
// 將 nums 做出一堆「長度為k」的子陣列，（逐位比較）找出最大的子陣列
// 因「每個數都不同」，只要比「每個」子陣列的「第一個數」找最大即可
int* largestSubarray(int* nums, int numsSize, int k, int* returnSize) {
    int ansI = 0;
    for(int i=0; i<numsSize-k+1; i++) { // 逐一比「每個」子陣列
        if(nums[i] > nums[ansI]) ansI = i; // 的第1個數
    }
    int* ans = (int*) malloc(sizeof(int)*k);
    for(int i=0; i<k; i++) {
        ans[i] = nums[ansI+i];
    }
    *returnSize = k;
    return ans;
    
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

