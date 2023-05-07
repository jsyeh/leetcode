class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        int N = nums.length;
        for(int i=N-1; i>=2; i--){
            if(nums[i]<nums[i-1]+nums[i-2]){
                return nums[i]+nums[i-1]+nums[i-2];
            }
        }
        return 0;
    }
}
