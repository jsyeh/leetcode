class Solution {
    public int arraySign(int[] nums) {
        //數字很多，不能直接乘
        //但可數數：幾個0、幾個負數
        int zero=0, negative=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]==0) zero++;
            if(nums[i]<0) negative++;
        }
        if(zero>0) return 0;
        if(negative%2==0) return 1;
        else return -1;
    }
}
