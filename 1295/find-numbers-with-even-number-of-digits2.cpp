// LeetCode 1295. Find Numbers with Even Number of Digits
// nums 裡,，有些的位數是偶數位數、有些位數是奇數位數。找到「偶數位數」有幾個
// 這題Easy題，有很多種寫法。這裡用大一熟悉的 for(迴圈) 配 if(判斷)，就完成了。
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans = 0;
        for(int i=0; i<nums.size(); i++) { // 利用迴圈，逐一測試
            int now = nums[i]; // 現在處理 nums[i] 這個數
            if(now>=10 && now<=99) ans++; // 如果是2位數，可以哦!
            if(now>=1000 && now<=9999) ans++; // 如果是4位數，也可以哦！
            if(now==100000) ans++; // 如果是最大的數 10^5 剛好也是6位數，也可以哦！
        }
        return ans;
    }
};
