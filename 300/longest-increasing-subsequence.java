class Solution {
    public int lengthOfLIS(int[] nums) {
        int N = nums.length;
        int [] table = new int[N];
        // table[i] : 包含 nums[i] 的 LIS 的長度
        table[0] = 1;
        int ans = 1;
        for(int i=1; i<N; i++){
            table[i] = 1;
            for(int k=i-1;k>=0; k--){
                if(nums[i]>nums[k] && table[k]+1>table[i]){
                    table[i] = table[k]+1;
                }
            }
            if(table[i]>ans) ans = table[i];
        }
        return ans;
    }
}
