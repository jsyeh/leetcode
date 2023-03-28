class Solution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int ans=0;
        int left=0, right=1; //右邊習慣不包含
        while(left<nums.length) {
            for(int i=0; left+i<nums.length ; i++) {
                if(nums[left+i]-nums[left]>k){
                    left=left+i;
                    ans++;
                    break;
                } else if(left+i==nums.length-1) {
                    left = nums.length;
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
}
