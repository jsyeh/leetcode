class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int target = *max_element(nums.begin(), nums.end());
        int combo = 0, ans = 0;
        for(int num : nums){
            if(num==target) combo++;
            else combo = 0;
            ans = max(ans, combo);
        }
        return ans;
    }
};
