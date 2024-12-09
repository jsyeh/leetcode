// LeetCode 3152. Special Array II
// 希望 nums[query開始...query結束] 的 subarray 裡，相鄰的數「奇偶數」相交錯。
// 可記錄「到nums[i]為止，「奇偶數交錯」最長（往前回溯）到哪裡，便能快速找到答案
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int N = nums.size();
        vector<int> prevSpecial(N);
        prevSpecial[0] = 0;
        for(int i=1; i<N; i++) {
            // 若是交錯的，可繼承前一項的位置
            if(nums[i-1]%2 != nums[i]%2) prevSpecial[i] = prevSpecial[i-1];
            else prevSpecial[i] = i; // 若不是交錯，只好歸零，從現在這裡「重新累積」交錯的部分
        }
        // 建好後，便可照著 queries 逐項找答案
        int Q = queries.size();
        vector<bool> ans(Q);
        for(int i=0; i<Q; i++) {
            int start = queries[i][0], end = queries[i][1];
            if(prevSpecial[end] <= start) { // 交錯範圍夠長，範圍能包含 start...end
                ans[i] = true; // 可以成功
            } else { // 交錯範圍不足
                ans[i] = false; // 就失敗了
            }
        }
        return ans;
    }
};
