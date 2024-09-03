// LeetCode 2553. Separate the Digits in an Array
// 把把數字的每一位數，分開後，再塞進答案裡
class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;
        for(int num : nums){
            for(char d : std::to_string(num)){
                ans.push_back(d - '0');
            }
        }
        return ans;
    }
};
