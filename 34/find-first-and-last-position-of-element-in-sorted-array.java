class Solution {
    public int[] searchRange(int[] nums, int target) {
        int mid = Arrays.binarySearch(nums, target);
        if(mid<0) {
            int [] ans = {-1, -1};
            return ans;
        }
        int a1 = mySearchLeft(nums, 0, nums.length, target);
        int a2 = mySearchRight(nums, 0, nums.length, target);
        int [] ans = {a1, a2};
        return ans;
    }
    int mySearchLeft(int[] nums, int from, int to, int target) {
        int mid = Arrays.binarySearch(nums, from, to, target);
        if(mid<0) return -1;
        int next = mySearchLeft(nums, from, mid, target);
        if(next==-1) return mid;
        else return next;
    }
    int mySearchRight(int[] nums, int from, int to , int target) {
        int mid = Arrays.binarySearch(nums, from, to, target);
        if(mid<0) return -1;
        int next = mySearchRight(nums, mid+1, to, target);
        if(next==-1) return mid;
        else return next;
    }
}
