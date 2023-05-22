class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean failedInc = false, failedDec = false;
        for(int i=1; i<nums.length; i++){
            if(nums[i-1] < nums[i]) failedDec = true;
            if(nums[i-1] > nums[i]) failedInc = true;
            if(failedInc && failedDec) return false;
        }
        return true;
    }
}
