// LeetCode 1822. Sign of the Product of an Array
class Solution {
public:
    int arraySign(vector<int>& nums) {
        int ans = 1; // 1乘上任何數,就突然變成「任何數」
        // 不能寫 int ans=0; 因為 0 乘上任何數,會變成0
        for(int i=0; i<nums.size(); i++) {
            if(nums[i]>0) ans *= +1;
            if(nums[i]<0) ans *= -1;
            if(nums[i]==0) ans *= 0;
        } // 數字越乘越大, 就爆炸了!!! 只能乘 +1, -1, 0 
        if(ans>0) return 1;
        if(ans<0) return -1;
        return 0;
    }
};
