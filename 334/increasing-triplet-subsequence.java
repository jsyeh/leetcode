class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums.length<3) return false;

        int lowest = Integer.MAX_VALUE, middle = Integer.MAX_VALUE;
        for(int i=0; i<nums.length; i++){
            if(nums[i]<lowest) lowest = nums[i];
            else if(lowest < nums[i] && nums[i] <middle) middle = nums[i];
            else if(nums[i]>middle) return true;
        }
        return false;
    }
}
