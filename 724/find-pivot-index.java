class Solution {
    public int pivotIndex(int[] nums) {
        int leftSum=0, rightSum = 0, N = nums.length;
        for(int i=1; i<N; i++){
            rightSum += nums[i];
        }
        if(rightSum == 0) return 0;

        for(int i=1; i<N; i++){
            leftSum += nums[i-1];
            rightSum -= nums[i];
            if(leftSum == rightSum) return i;
        }
        return -1;
    }
}//Input: [-1,-1,0,1,1,0]
