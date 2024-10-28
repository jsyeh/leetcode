// LeetCode 2644. Find the Maximum Divisibility Score
// 問 nums[i] 能被 divisors[d] 整除最多的那個 divisors[d] 是哪個
class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int ans = divisors[0], score = 0;
        for(int d : divisors) {
            int score2 = 0;
            for(int num : nums) {
                if(num % d == 0){
                    score2++;
                }
            }
            if(score2>score || (score2==score && d<ans)) {
                ans = d;
                score = score2;
            }
        }
        return ans;
    }
};
