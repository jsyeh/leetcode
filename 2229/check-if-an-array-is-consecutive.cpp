// LeetCode 2229. Check if an Array Is Consecutive
// 檢測 nums 是否是「一串連續的整數」
class Solution {
public:
    bool isConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i=1; i<nums.size(); i++) {
            if(nums[i-1] + 1 != nums[i]) return false;
        }
        return true;
    }
};
