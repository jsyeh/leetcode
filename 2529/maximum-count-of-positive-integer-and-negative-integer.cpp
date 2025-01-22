// LeetCode 2529. Maximum Count of Positive Integer and Negative Integer
// 找出「有幾個正數」「有幾個負數」，大的那個數量回傳
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int pos = 0, neg = 0;
        for(int num : nums) {
            if(num<0) neg++;
            if(num>0) pos++;
        }
        return max(neg, pos);
    }
};
