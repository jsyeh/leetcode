// LeetCode 3392. Count Subarrays of Length Three With a Condition
// 數一數「有多少subarray」長度為3、且前後加起來==中間/2
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int ans = 0; // 迴圈前面 ans 是 0
        for(int i=0; i<nums.size()-2; i++) { // 逐一處理
            if( nums[i]*2 + nums[i+2]*2 == nums[i+1] ) ans++;
        } // 迴圈裡，符合條件的「答案]  +1
        return ans; // 迴圈後，把答案送出去
    }
};
