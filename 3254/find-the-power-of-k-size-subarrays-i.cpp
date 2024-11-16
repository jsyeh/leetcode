// LeetCode 3254. Find the Power of K-Size Subarrays I
// 陣列power：如果「陣列小到大、間隔差1」就挑最大那個，不然就-1
// 請把長度為k的subarray的「陣列power」都算出來
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int N = nums.size();
        vector<int> ans(N-k+1); //直接開夠大的陣列
        int combo = 0; // 利用 combo 來累計「目前有幾項完成」
        for(int i=0; i<N; i++) {
            if(i==0 || nums[i-1]+1==nums[i]) combo++; //累加combo
            else combo=1; //新的開始，1個

            if(i<k-1) continue; //還不足k項，就不要記錄下來

            if(combo>=k) ans[i-k+1] = nums[i];
            else ans[i-k+1] = -1;
        }
        return ans;
    }
};
