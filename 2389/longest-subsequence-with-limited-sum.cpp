// LeetCode 2389. Longest Subsequence With Limited Sum
// queries[i] 給個數字，問 nums 能挑出的「最長」有多長。
class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        vector<int> ans(queries.size());
        sort(nums.begin(), nums.end()); // 先「小到大」排好，之後「小到大」挑數字即可
        // 因僅 1000 個數，暴力加起來即可。若數字大，可用 prefixSum 配 binary search
        for(int i=0; i<queries.size(); i++) { // 「小到大」逐項加加看
            int nowSum = 0, nowN = 0, query = queries[i];
            for(int i=0; i<nums.size(); i++) {
                if(nowSum + nums[i] <= query) {
                    nowSum += nums[i]; // 就加起來吧
                    nowN++; // 喜，又多了1個數
                } else break;
            }
            ans[i] = nowN;
        }
        return ans;
    }
};
