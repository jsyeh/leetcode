// LeetCode 1295. Find Numbers with Even Number of Digits
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans = 0; // 迴圈前面 ans 是 0
        for(int i=0; i<nums.size(); i++){
            int now = nums[i]; // 現在要處理 nums[i]
            // Q: 如何知道 nums[i] 是幾位數?
            int digits = 0; //有幾位數啊?
            while(now>0){ // 用上週教過、今天又寫2-3次的剝皮法
                digits++; // 一邊數一下「你剝了幾次」
                now = now / 10; // 數字越剝越小
            }
            if(digits%2==0) ans++;// 迴圈裡, 偶數的位數時, ans++
        }
        return ans; // 迴圈後面 ans 拿來用
    }
};
