// LeetCode 2270. Number of Ways to Split Array
// 要將 nums 切成2段，左邊 i+1個加起來 >= 右邊剩下的。有幾種切法？
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int N = nums.size();
        vector<int> preSum(N+1);
        for(int i=0; i<N; i++) {
            preSum[i+1] = preSum[i] + nums[i];
        }
        int total = preSum[N];
        int ans = 0;
        for(int i=0; i<N-1; i++) { 
        // 想要比較 nums[0]...nums[i] vs. nums[i+1]...nums[N-1] 右邊至少1項，所以迴圈 i<N-1
            if(preSum[i+1] >= total - preSum[i+1]) ans++; // 因 preSum[i+1] 對應 nums[i] 項
        }
        return ans;
    }
};
