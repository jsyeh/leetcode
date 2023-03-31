class Solution {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length; //右邊界不包含
        return search(nums, i, j, target);
    }
    int search(int[] nums, int i, int j, int target) {
        int mid = (i+j)/2; //右邊界不包含
        if(j==mid) return -1;
        else if(nums[mid]==target) return mid;
        else if(target<nums[mid]) return search(nums, i, mid, target);
        else return search(nums, mid+1, j, target);
    }
}
