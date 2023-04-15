class Solution {
    public void sortColors(int[] nums) {
        int [] c = {0, 0, 0};
        for(int i=0; i<nums.length; i++){
            c[nums[i]]++;
        }
        for(int i=0; i<nums.length; i++){
            if(i<c[0]) nums[i] = 0;
            else if(i<c[0]+c[1]) nums[i] = 1;
            else nums[i] = 2;
        }
    }
}
