class Solution {
    public void moveZeroes(int[] nums) {
        //3:36 搞錯題目，原來不用排序
        int k=0, zero=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]==0) zero++;
            else {
                nums[k] = nums[i];
                k++;
            }
        }
        for(int i=k; i<nums.length; i++) {
            nums[i] = 0;
        }
    }
}
