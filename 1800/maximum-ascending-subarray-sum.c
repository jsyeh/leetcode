// LeetCode 1800. Maximum Ascending Subarray Sum
// nums 陣列裡，某一段「漸增」加起來希望最多。
int maxAscendingSum(int* nums, int numsSize) {
    int ans = nums[0], now = nums[0]; // 一開始，先放「第1筆」
    for(int i=1; i<numsSize; i++) { // 逐筆「與前項比較」
        // 若「漸增」，這段「漸增」數列變大
        if(nums[i-1] < nums[i]) now += nums[i]; 
        else now = nums[i]; // 若沒「漸增」，就是「新的一段」的開始
        
        if(now>ans) ans = now; // 隨時更新「答案」
    }
    return ans;   
}
