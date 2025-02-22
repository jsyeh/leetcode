// LeetCode 487. Max Consecutive Ones II
// nums 裡，若能把「1個0變1」，最多能「連續幾個1」
// 可用「毛毛蟲」的方法，容忍「最多1個0」來爬行即可
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int zero = 0, left = 0, ans = 0;
        for(int right = 0; right < nums.size(); right++) { // 右邊的頭往右爬
            if(nums[right]==0) { // 遇到0，就要處理 
                zero++; // 多了1個0
                while(zero>1) { // 0太多，就一直縮左邊的尾巴
                    if(nums[left]==0) zero--; // 太好了，吐出1個0
                    left++; // 左邊的尾巴往右縮
                }
            } 
            ans = max(ans, right-left+1); // 最長的長度在這裡
        }
        return ans;
    }
};
