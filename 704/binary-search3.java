class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(nums, 0, nums.length, target);
    }
    int binarySearch(int[] nums, int i, int j, int target) {
        if(i>=j) return -1; //error
        int mid = (i+j)/2;
        if(nums[mid]==target) return mid;
        if(target<nums[mid]) {
            return binarySearch(nums, i, mid, target);
        }else {
            return binarySearch(nums, mid+1, j, target);
        }
    }
}
