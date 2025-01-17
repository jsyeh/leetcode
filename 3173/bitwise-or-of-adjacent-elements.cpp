// LeetCode 3173. Bitwise OR of Adjacent Elements
// 請找出 ans[i] = nums[i] | nums[i+1] 的陣列
class Solution {
public:
    vector<int> orArray(vector<int>& nums) {
        int N = nums.size();
        vector<int> ans(N-1);
        for(int i=0; i<N-1; i++) {
            ans[i] = nums[i] | nums[i+1];
        }
        return ans;
    }
};
