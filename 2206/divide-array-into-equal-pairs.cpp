// LeetCode 2206. Divide Array Into Equal Pairs
// 將 nums 裡的數，相同的數「兩兩一組」分好，全部分完。
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        int counter[501] = {}; // 用來統計「有幾個數」
        int odd = 0; // 統計目前「數量」有幾個是奇數個
        for(int i=0; i<nums.size(); i++) {
            counter[nums[i]]++;
            if(counter[nums[i]]%2==1) odd++; // 現在多1個奇數數量
            else odd--; // 現大土中少1個奇數數量
        }
        return odd == 0; // 確定「沒有任何落單」的數
    }
};
