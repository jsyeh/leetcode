// LeetCode 1929. Concatenation of Array
// 把陣列複製2次
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int N = nums.size();
        vector<int> ans(N*2);
        for(int i=0; i<N; i++) {
            ans[i] = ans[N+i] = nums[i];
        }
        return ans;
    }
};
