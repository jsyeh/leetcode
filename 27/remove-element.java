class Solution {
    public int removeElement(int[] nums, int val) {
        int N = nums.length;
        for(int i=0; i<N; i++){
            if(nums[i]==val) {
                nums[i] = nums[N-1];
                N--;
                i--;
            }
        }
        return N;
    }
}
