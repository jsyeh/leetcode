// LeetCode 2563. Count the Number of Fair Pairs
// 若 lower <= nums[i] + nums[j] <= upper 叫 fair pair，總共有多少組？
// 直覺用2層for迴圈，但 nums 有 10^5 太大，不能用2層迴圈。
class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());// Hint 1 建議 sort() 因 sort 後的結果一樣多組
        // 再來就簡單了，用 for 迴圈，決定右邊界，再binary search看左邊的範圍
        long long int ans = 0; // 小心，要用 long long int 才夠裝答案，因為答案會很大很大
        for(int i=1; i<nums.size(); i++) {
            auto j_left = lower_bound(nums.begin(), nums.begin()+i, lower - nums[i]);
            auto j_right = upper_bound(nums.begin(), nums.begin()+i, upper - nums[i]);
            ans += j_right - j_left;
        }
        return ans;
    }
};

