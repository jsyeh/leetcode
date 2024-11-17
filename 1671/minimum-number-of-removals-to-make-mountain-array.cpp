// LeetCode 1671. Minimum Number of Removals to Make Mountain Array
// 「像山一樣」的山形陣列，會「先上升、再下降」。nums裡「最少刪幾個」會變成「像山一樣」的山形陣列。
// Hint 1: 想找「最長」的「像山一樣」的山形subseqnece
// Hint 2: 用 LIS 問題的解法（的變形），來解類似的問題
// 所以就「左到右的LIS」和「右到左的LIS」都準備好，再巡一次，就知道答案了
class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int N = nums.size();
        int LIS1[1000] = {}, LIS2[1000];
        for(int i=0; i<N; i++) {
            LIS1[i] = 1; // 左到右的 LIS，LIS1[i] 對應「以nums[i]結尾的LIS長度」
            for(int k=0; k<i; k++) { // 只要左小右大，就更新
                if(nums[k]<nums[i]) LIS1[i] = max(LIS1[i], LIS1[k]+1);
            }
        }
        for(int i=N-1; i>=0; i--) {
            LIS2[i] = 1; // 右到左的 LIS，LIS2[i] 對應「以nums[i]結尾的LIS長度」
            for(int k=i+1; k<N; k++) { // 只要左大右小，就更新
                if(nums[i]>nums[k]) LIS2[i] = max(LIS2[i], LIS2[k]+1);
            }
        }
        int ans = 0; // 想找「山形」的「最長」
        for(int i=1; i<N-1; i++) { // 因為要山形，山峰不能在最左、最右邊
            if(LIS1[i]!=1 && LIS2[i]!=1) { // 如果有任一個是1，就不是山形
                ans = max(ans, LIS1[i] + LIS2[i] - 1);
            }
        }
        return N - ans; // 反過來，就是「要刪最少、要刪幾個
    }
};
