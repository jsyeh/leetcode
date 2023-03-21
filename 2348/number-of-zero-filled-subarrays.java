class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long ans = 0;
        int N = nums.length;
        int zeroN = 0;
        for(int i=0; i<N; i++){
            if(nums[i]==0) zeroN++;
            else if(nums[i]!=0){
                if(zeroN>0) ans += calc(zeroN);
                zeroN=0;
            }
            if(nums[i]==0 && i==N-1){
                ans += calc(zeroN);
            }
        }
        return ans;
    }
    long calc(long len) {
        return (0+len)*(len+1)/2;
    }
}
