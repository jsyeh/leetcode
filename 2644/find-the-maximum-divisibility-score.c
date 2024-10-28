// LeetCode 2644. Find the Maximum Divisibility Score
// 問 nums[i] 能被 divisors[d] 整除最多的那個 divisors[d] 是哪個
int maxDivScore(int* nums, int numsSize, int* divisors, int divisorsSize) {
    int ans = divisors[0], score = 0;
    for(int d=0; d<divisorsSize; d++) {
        int score2 = 0;
        for(int i=0; i<numsSize; i++) {
            if(nums[i] % divisors[d]==0) {
                score2++;
            }
        }
        if(score2>score || (score2==score && divisors[d]<ans)) {
            ans = divisors[d];
            score = score2;
        }
    }
    return ans;
}
