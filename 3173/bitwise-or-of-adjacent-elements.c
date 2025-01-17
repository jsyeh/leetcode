// LeetCode 3173. Bitwise OR of Adjacent Elements
// 請找出 ans[i] = nums[i] | nums[i+1] 的陣列
int* orArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*) malloc(sizeof(int)*(numsSize-1));
    for(int i=0; i<numsSize-1; i++) {
        ans[i] = nums[i] | nums[i+1];
    }
    *returnSize = numsSize - 1;
    return ans;    
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

