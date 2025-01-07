// LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
// 將 nums 切成 3 段 subarray，希望3段的「第1個」加起來最小。
class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int min1 = min(nums[1], nums[2]);
        int min2 = max(nums[1], nums[2]);
        for(int i=3; i<nums.size(); i++) {
            if(nums[i]<min1) {
                min2 = min1;
                min1 = nums[i];
            } else if(nums[i]<min2) {
                min2 = nums[i];
            }
        }
        return nums[0] + min1 + min2;
    }
};
