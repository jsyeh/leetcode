// LeetCode 2270. Number of Ways to Split Array
// 要將 nums 切成2段，左邊 i+1個加起來 >= 右邊剩下的。有幾種切法？
int waysToSplitArray(int* nums, int numsSize) {
    long long int preSum[numsSize+1];
    preSum[0] = 0;
    for(int i=0; i<numsSize; i++) {
        preSum[i+1] = preSum[i] + nums[i];
    }
    long long int total = preSum[numsSize];
    int ans = 0;
    for(int i=0; i<numsSize-1; i++) {
        if(preSum[i+1] >= total - preSum[i+1]) ans++;
    } // 因 preSum[i+1] 對應 nums[i] 項
    return ans;
}
