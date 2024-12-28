// LeetCode 689. Maximum Sum of 3 Non-Overlapping Subarrays
// 將 nums 分成 3 段「長度為k」且「不重疊」，加來要最大。本題目用了 3 次 Dynamic Programming 的技巧（先左邊、再右邊，最後查中間）
class Solution {
public:
    int sumK(int i, int k, vector<int>& prefixSum) {
        return prefixSum[i+k] - prefixSum[i];
    }
    int sumKKK(int iLeft, int iMiddle, int iRight, int k , vector<int>& prefixSum) {
        return sumK(iLeft, k, prefixSum) + sumK(iMiddle, k, prefixSum) + sumK(iRight, k, prefixSum);
    }
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int N = nums.size();
        vector<int> prefixSum(N+1), posLeft(N), posRight(N);
        prefixSum[0] = 0;
        for(int i=0; i<N; i++) {
            prefixSum[i+1] = prefixSum[i] + nums[i];
        }
        posLeft[0] = 0;
        for(int i=1; i<=N-k; i++) {
            int i2 = posLeft[i-1];
            if(sumK(i, k, prefixSum) > sumK(i2, k, prefixSum)) posLeft[i] = i;
            else posLeft[i] = i2;
        }
        posRight[N-k] = N-k;
        for(int i=N-k-1; i>=0; i--) {
            int i2 = posRight[i+1];
            if(sumK(i, k, prefixSum) >= sumK(i2, k, prefixSum)) posRight[i] = i;
            else posRight[i] = i2;
        }
        vector<int> ans({0,k,k*2});
        for(int i=k; i<=N-k*2; i++) {
            int iLeft = posLeft[i-k], iRight = posRight[i+k];
            if(sumKKK(iLeft, i, iRight, k, prefixSum) > sumKKK(ans[0], ans[1], ans[2], k, prefixSum)) {
                ans[0] = iLeft;
                ans[1] = i;
                ans[2] = iRight;
            }
        }
        return ans;
    }
};
