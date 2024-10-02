// LeetCode 283. Move Zeroes 把陣列裡的0移到右邊（不可以開新陣列）
// 簡單作法：先「數一數」有幾個0/有幾個不是0、邊數邊把「不是0」收集/移到左邊，最後再補0即可
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonZero=0; // 用1個變數，統計有幾個「不是0」的數
        for(int i=0; i<nums.size(); i++) {
            if(nums[i]!=0){ // 如果「不是0」，就手動「移到左邊」
                nums[nonZero++] = nums[i];
            } // 利用上週教過 nums[N++] 的技巧，邊移、邊改「變數」
        }
        for(int i=nonZero; i<nums.size(); i++) {
            nums[i] = 0; // 最後「用迴圈」把剩下右邊的數，都放0
        }
    }
};
