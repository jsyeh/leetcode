class Solution {
    public int search(int[] nums, int target) {
        int ans = Arrays.binarySearch(nums, target);
        if(ans>=0) return ans;
        return -1;
    }
}
