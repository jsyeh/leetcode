// LeetCode 1389. Create Target Array in the Given Order
// 將 nums[i] 照著 index[i] 的位置，插入 target 陣列裡
class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> ans;
        for(int i=0; i<index.size(); i++) {
            int ii = index[i]; // 要插入的 index 位置
            ans.insert(ans.begin() + ii, nums[i]);
        }      
        return ans;  
    }
};
