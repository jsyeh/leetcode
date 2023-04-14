class Solution {
    public int majorityElement(int[] nums) {
        //Easy感覺得簡單的題目,程式碼應不會太難
        //但要想到簡單的解法，需要一點靈感
        //偷看解答，有很多種作法
        Arrays.sort(nums);
        //找連續的次數
        int ans = nums[0], maxCount=1, count=1;
        for(int i=1; i<nums.length; i++){
            if(nums[i]==nums[i-1]) count++;
            else{
                if(count>maxCount){
                    maxCount = count;
                    ans = nums[i-1];
                }
                count = 1;
            }
        }
        if(count>maxCount) ans = nums[nums.length-1];
        return ans;
    }
}
