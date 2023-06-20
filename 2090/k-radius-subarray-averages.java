class Solution {
    public int[] getAverages(int[] nums, int k) {
        int width = k*2+1;
        int[] ans = new int[nums.length];

        long sum=0;
        for(int i=0; i<width-1 && i<nums.length; i++) {
            sum += nums[i];
        }
        for(int i=0; i<nums.length; i++){
            if(i<k) {
                ans[i] = -1;
            } else if(i>=nums.length-k) {
                ans[i] = -1;
            } else {
                sum += nums[i+k];
                ans[i] = (int)(sum / width);
                sum -= nums[i-k];
            }
        }
        return ans;
    }
}
//case 38/39: 一堆 100000, 加起來超過int
