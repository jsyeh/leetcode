// LeetCode 2535. Difference Between Element Sum and Digit Sum of an Array
// a = sum(nums), b = 每個位數加起來，想找 abs(a-b)
class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int a = std::accumulate(nums.begin(), nums.end(), 0);
        int b = 0;  // 要把「每個位數」加起來
        for(int num : nums) {
            while(num>0) {
                b += num % 10;  // 要把「每個位數」加起來
                num /= 10;  // 剝皮法
            }
        }
        return abs(a-b);
    }
};

