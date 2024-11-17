// LeetCode 3095. Shortest Subarray With OR at Least K I
// 希望 subarray 裡的數 OR 起來後 >=k，問最小的subarray裡，有幾個數
// subarray 是連續的 nums[i]...nums[j]
class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int ans = INT_MAX;
        int N = nums.size();
        for(int i=0; i<N; i++){ // 計算 nums[i]...nums[j] 的 OR值
            int allOR = 0; // 計算 i 開始的subarray 結果>=k的長度
            for(int j=i; j<N; j++){
                allOR |= nums[j];
                if(allOR>=k){
                    ans = min(ans, j-i+1);
                    break;
                }
            }
        }
        if(ans==INT_MAX) return -1;
        return ans;
    }
};
