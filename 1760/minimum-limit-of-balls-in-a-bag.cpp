// LeetCode 1760. Minimum Limit of Balls in a Bag
// 每個袋子裡有 nums[i] 個球，每次可「挑1袋」分成「2袋」, 希望做完 maxOperations 次後，每袋的球的上限「最少」是多少？ 
class Solution {
public:
    int helper(int maxVal, vector<int>&nums) { // 這個函式，供 binary search 使用
        int ans = 0;
        for(int num : nums) { // 算出要「再多幾袋」才能不超過 maxVal
            ans += num / maxVal - 1 + (num % maxVal > 0);
        }
        return ans;
    }
    int minimumSize(vector<int>& nums, int maxOperations) {
        int largest = *max_element(nums.begin(), nums.end()); // 最大那袋，當成 右邊界
        int left = 1, right = largest; // 設很大，但怕 overflow 先設成 long long int
        while(left<right) { // binary search 的寫法
            int mid = (left+right) / 2; // 之後數字會變正常，用 int 即可
            int operations = helper(mid, nums);
            if(operations>maxOperations) left = mid + 1; // 不成立，調高 1 格
            else right = mid; // 成立，往下再探索
        } // 用「猜數字」常用的 binary search。直接「預測最大值」再檢查「能不能做到」
        return left;
    }
};
