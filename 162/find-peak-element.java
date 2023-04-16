class Solution {
    public int findPeakElement(int[] nums) {
        //微積分的極值，一次微分為0
        return findPeakElement(nums, 0, nums.length-1);
    }
    int findPeakElement(int[] nums, int left, int right) {
        if(left==right) return left;//夾擊
        //如果剩2格，就回傳大的那格
        if(right-left==1){
            if(nums[left]>nums[right]) return left;
            else return right;
        }

        int mid = (left+right)/2;
        if(nums[mid+1]-nums[mid]>0){ //上漲，看右半邊
            return findPeakElement(nums, mid, right);
        }else return findPeakElement(nums, left, mid);
    }
}
