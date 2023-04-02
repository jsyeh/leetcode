class Solution {
    public int[] sortedSquares(int[] nums) {
        //00:29看懂
        for(int i=0; i<nums.length; i++){
            nums[i] *= nums[i];
        }
        Arrays.sort(nums);
        return nums;
    }
}
