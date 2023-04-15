class Solution {
    public int[] searchRange(int[] nums, int target) {
        int index = Arrays.binarySearch(nums, target);
        if(index<0) return new int[]{-1,-1};

        int left = myBinarySearchLeft(nums, target, 0, nums.length);
        int right = myBinarySearchRight(nums, target, 0, nums.length);

        return new int[]{left, right};
    }
    int myBinarySearchLeft(int[] nums, int target, int left, int right) {
        int mid = (left+right)/2;
        if(nums[mid]==target) {
            if(mid-1<left) return mid;
            return myBinarySearchLeft(nums, target, left, mid);
        }else if(nums[mid]>target) {
            return myBinarySearchLeft(nums, target, left, mid);
        }else {
            return myBinarySearchLeft(nums, target, mid+1, right);
        }
    }
    int myBinarySearchRight(int[] nums, int target, int left, int right) {
        int mid = (left+right)/2;
        if(nums[mid]==target) {
            if(mid+1>=right) return mid;
            return myBinarySearchRight(nums, target, mid, right);
        }else if(nums[mid]>target) {
            return myBinarySearchRight(nums, target, left, mid);
        }else {
            return myBinarySearchRight(nums, target, mid+1, right);
        }
    }
}
