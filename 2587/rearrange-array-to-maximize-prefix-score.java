class Solution {
    public int maxScore(int[] nums) {
        int N = nums.length;
        Arrays.sort(nums);
        long sum=0;
        int ans=0;
        if(sum>0) ans++;
        for(int i=N-1; i>=0; i--){
            sum += nums[i];
            if(sum>0) ans++;
        }
        return ans;
    }
}//TODO: maxize the number of positive integers in the array prefix.
//long 64bit
