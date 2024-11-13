// LeetCode 2563. Count the Number of Fair Pairs
// 同樣的演算法，用 C++ 就能順利做出來，不會超過時間！
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        long long int ans = 0; // 小心，要用 long long int 才夠裝答案，因為答案會很大很大
        for(int i=1; i<nums.size(); i++) {
            auto j_left = lower_bound(nums.begin(), nums.begin()+i, lower - nums[i]);
            auto j_right = upper_bound(nums.begin(), nums.begin()+i, upper - nums[i]);
            ans += j_right - j_left;
        }
        return ans;
    }
};
