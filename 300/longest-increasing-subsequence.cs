public class Solution {
    public int LengthOfLIS(int[] nums) {
        int N = nums.Length;
        int [] dp = new int[N]; //dp[i]: 到nums[i]為止且包含它的 LIS 長度
        int ans = 1;
        for(int i=0; i<N; i++){ // 每個人都去查
            dp[i] = 1; // 最基礎的1
            for(int k=0; k<i; k++){
                if(nums[i]>nums[k] && dp[k]+1>dp[i]){
                    dp[i] = dp[k] + 1; // 如果更長的話，更新
                } //包含 nums[k]，最後一項是 nums[i] 的最長 LIS
            }
            if(dp[i]>ans) ans = dp[i]; // 如果更長的話，更新
        }
        return ans;
    }
}
