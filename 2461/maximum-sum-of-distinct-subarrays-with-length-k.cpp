// LeetCode 2461. Maximum Sum of Distinct Subarrays With Length K
// 長度 k 的 subarrays （裡面每格都不同）加起來最大值。連續subarray適合「毛毛蟲」
// 策略：「只要吃到『重覆』」，就要一直吐，吐到「沒有重覆」腸子清空為止。
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long ans = 0, total = 0; // 最大的答案、目前的total值
        unordered_set<int> window; // 利用 Hash Set 來存 sliding window 裡，只出現1次的數
        int N = nums.size();
        int left = 0, right = 0; // 毛毛蟲的 sliding window
        for(right=0; right<N; right++) { // 右邊界，會遞增
            while(window.count(nums[right])>0 || window.size()>=k) { // 右邊有吃過 or 太長
                window.erase(nums[left]); // 吐掉左邊
                total -= nums[left]; // total減少
                left++; // 左邊界「右移」1格
            }
            window.insert(nums[right]); // 吃掉右邊
            total += nums[right]; // total增加
            if(window.size()==k) ans = max(ans, total); // 長度正確時，更新答案
        }
        return ans;
    }
};
