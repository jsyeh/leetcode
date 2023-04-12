class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        int [] ans = new int[N+1];
        if(N>0) ans[0] = nums[0];
        if(N>1) ans[1] = nums[1];
        if(N>2) ans[2] = nums[2]+ans[0];
        for(int i=3; i<N; i++){
            ans[i] = nums[i] + max(ans[i-2], ans[i-3]);
        }//ans[i]表示第i個要用的最好結果
        if(N==1) return ans[0];
        else return max(ans[N-1],ans[N-2]);
    }
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
}
