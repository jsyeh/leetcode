//如果有負的，那交給之後的可能更好。
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int * table = new int[nums.size()];
        // table[i] 表示包含 nums[i] 結尾的最大maxSubArray和
        table[0] = nums[0];
        int ans = table[0]; //因為迴圈沒有考慮到最前面的 table[0]
        for(int i=1; i<nums.size(); i++){
            table[i] = table[i-1] + nums[i];
            if(nums[i]>table[i]) table[i] = nums[i];
            if(table[i]>ans) ans = table[i];
        }
        return ans;
    }
};
