//因為乘到負數時，要倒過來比較，所以準備兩個陣列
//max_so_far[i] 表示 subarray 到 nums[i] 的（乘法）最大值
//min_so_far[i] 表示 subarray 到 nums[i] 的（乘法）最小值
class Solution {
public:
    int max(int a, int b, int c) {
        return std::max(a, std::max(b,c));
    }
    int min(int a, int b, int c) {
        return std::min(a, std::min(b,c));
    }
    int maxProduct(vector<int>& nums) {
        int max_so_far[nums.size()], min_so_far[nums.size()];
        max_so_far[0] = nums[0];
        min_so_far[0] = nums[0];
        int ans = nums[0];
        for(int i=1; i<nums.size(); i++) {
            max_so_far[i] = max(max_so_far[i-1]*nums[i], min_so_far[i-1]*nums[i], nums[i]);
            min_so_far[i] = min(max_so_far[i-1]*nums[i], min_so_far[i-1]*nums[i], nums[i]);
            if(max_so_far[i]>ans) ans = max_so_far[i];
        }
        return ans;
    }
};
