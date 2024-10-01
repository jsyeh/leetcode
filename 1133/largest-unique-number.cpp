// LeetCode 1133. Largest Unique Number
// 最大的「單獨」的數。可以 sort 後，從大到小，找單獨的數
class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());  // 先「小到大」排好」
        int N = nums.size();  // 為簡化下面程式，用 N 對應 nums 數量
        if(N==1) return nums[0]; // 如果只有1個數，那它一定是 unique 的
        if(nums[N-1]!=nums[N-2]) return nums[N-1]; // 最大的數，與次大的不同，就找到答案
        for(int i=nums.size()-2; i>=1; i--){ // 倒過來的迴圈，避開最大、最小2數
            if(nums[i]!=nums[i+1] && nums[i]!=nums[i-1]) return nums[i];
        } // 與左右不同，就是 unique
        if(nums[0]!=nums[1]) return nums[0]; // 最小的數，與旁邊不同，也是 unique
        return -1; // 找不到答案，傳 -1
    }
};
