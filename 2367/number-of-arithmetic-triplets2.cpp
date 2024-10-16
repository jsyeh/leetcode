// LeetCode 2367. Number of Arithmetic Triplets
// 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
// 用暴力3層迴圈，太慢了。因為 nums[i] 是「嚴格遞增」越來越大
// 所以一定不會重覆，可利用 history 來記下「之前出現過的數」
class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int history[201] = {}; // 因數字 <= 200
        int ans = 0;
        for(int num : nums){
            if(num-diff*2>=0 && history[num-diff]==1 && history[num-diff*2]==1){
                ans++;
            }
            history[num] = 1; // 記錄 nums 出現過
        }
        return ans;
    }
};
