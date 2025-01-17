// LeetCode 1708. Largest Subarray Length K
// 將 nums 做出一堆「長度為k」的子陣列，（逐位比較）找出最大的子陣列
// 因「每個數都不同」，只要比「每個」子陣列的「第一個數」找最大即可
class Solution {
public:
    vector<int> largestSubarray(vector<int>& nums, int k) {
        int ansI = 0;
        for(int i=0; i<nums.size()-k+1; i++) { // 逐一比「每個」子陣列
            if(nums[i] > nums[ansI]) ansI = i; // 的第1個數
        }
        vector<int> ans(nums.begin()+ansI, nums.begin()+ansI+k);
        return ans;
    }
};
