// LeetCode 1018. Binary Prefix Divisible By 5
// nums 裡有一堆 0 和 1，以它為 prefix 的數，是5的倍數嗎？
// 因 nums 有 10^5 個 bit，所以要取 %5 才不會爆掉
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    bool* ans = (bool*)malloc(sizeof(bool)*numsSize);
    int now = 0;
    for(int i=0; i<numsSize; i++) {
        now = (now * 2 + nums[i]) % 5;
        if(now==0) ans[i] = true;
        else ans[i] = false;
    }
    *returnSize = numsSize;
    return ans;
}
