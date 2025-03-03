// LeetCode 2161. Partition Array According to Given Pivot
// 給 pivot，小的放左邊、大的放右邊、相同的放中間，順序要保持。
// 這次用 3 個迴圈，先取出「小的」，再取出「相同」，最後取出「大的」
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> ans(nums.size()); // 先開新的 memory
        int ansN = 0;
        for(int num : nums) {
            if(num<pivot) ans[ansN++] = num; // 小的放左邊
        }
        for(int num : nums) {
            if(num==pivot) ans[ansN++] = num; // 相同的放中間
        }
        for(int num : nums) {
            if(num>pivot) ans[ansN++] = num; // 大的放右邊
        }
        return ans;
    }
};
