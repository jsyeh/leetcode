class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int ans=0;

        int sum=0, left=0, right=0;//右界包含
        for( ; right<nums.length; right++){
            sum += nums[right];
            while(sum>=target){
                int nowLen = right-left+1;
                if(ans==0) ans = nowLen;
                else if(nowLen<ans) ans = nowLen;

                sum -= nums[left];
                left++;
            }
            if(sum>=target){
            }
        }
        return ans;
    }
}//case 12: 11 [1,2,3,4,5]
