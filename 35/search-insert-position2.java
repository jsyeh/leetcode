class Solution {
    public int searchInsert(int[] nums, int target) {
        return searchInsert(nums, 0, nums.length, target);
    }
    int searchInsert(int[] nums, int i, int j, int target) {
        if(i>=j) return i;
        int mid = (i+j)/2;
        if(nums[mid]==target) return mid;
        if(target <= nums[mid]) return searchInsert(nums, i, mid, target);
        else return searchInsert(nums, mid+1, j, target);
    }
}

