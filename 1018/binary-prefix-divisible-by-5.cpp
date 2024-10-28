// LeetCode 1018. Binary Prefix Divisible By 5
// nums 裡有一堆 0 和 1，以它為 prefix 的數，是5的倍數嗎？
// 因 nums 有 10^5 個 bit，所以要取 %5 才不會爆掉
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> ans(nums.size());
        int now = 0;
        for(int i=0; i<nums.size(); i++) {
            now = (now * 2 + nums[i]) % 5;
            if(now==0) ans[i] = true;
            else ans[i] = false;
        }
        return ans;
    }
};
