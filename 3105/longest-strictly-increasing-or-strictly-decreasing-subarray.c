// LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
// 持續增加 or 持續減少，最長的長度是多少？
int longestMonotonicSubarray(int* nums, int numsSize) {
    int ans = 1, inc = 1, dec = 1;
    for(int i=1; i<numsSize; i++) {
        if(nums[i-1]<nums[i]) { // 持續增加
            inc++;
            if(inc>ans) ans = inc;
        } else inc = 1; // 沒有持續增加，重來

        if(nums[i-1]>nums[i]) { // 持續減少
            dec++;
            if(dec>ans) ans = dec;
        } else dec = 1; // 沒有持續減少，重來
    }
    return ans;
}
