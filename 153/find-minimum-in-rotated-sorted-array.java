class Solution {
    public int findMin(int[] nums) {
        //return nums[findMin(nums, 0, nums.length-1)];
        int left=0, right=nums.length-1;

        while(left<right){
            int mid = (left+right)/2;
            if(nums[left]<=nums[right]) return nums[left];
            if(nums[left] <= nums[mid]){
                left = mid+1;
            }else {
                right = mid;
            }
        }
        return nums[left];
    }

 /*   int findMin(int[] nums, int left, int right) {

System.out.println("left:" + left + " - " + nums[left] + " right:" + right + " - " + nums[right]);

        if(nums[left]<=nums[right]) return left;//左右排好，太棒了
        if(left==right) return right;//太接近了，夾擊成功

        int mid = (left+right)/2;
        if(nums[mid]>nums[mid+1]) return mid+1;
        if(nums[mid-1])
        if(nums[mid]>nums[left]) {//正常的順序,表示最小值在另一邊 or 0
            return findMin(nums, mid, right);
        }else{
            return findMin(nums, left, mid);
        }
    }*/

    //Q：若本來的nums[] 完全沒有 rotate 那方法還是對的嗎？
}
