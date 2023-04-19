class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int ans=0, product=1;
        int left=0, right=0;//右包含
        for( ; right<nums.length; right++){
            product *= nums[right];
            while(left<nums.length && product>=k){
                product/=nums[left];
                left++;//縮左邊界，直到合格為止
            }
            if(product<k) ans+=(right-left+1);//以右界為準，距離全下
            System.out.println(ans);
        }
        return ans;
    }
}
//10 5 2 6
//10
//10 5
//   5 2
//   5 2 6 
