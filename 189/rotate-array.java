class Solution {
    public void rotate(int[] nums, int k) {
        int N = nums.length;
        int [] ans = new int[N];
        for(int i=0; i<N; i++){
            //ans[i] = nums[(i+N-k)%N];
            int i2 = ((i-k)%N+N)%N;
            ans[i] = nums[i2];
        }
        for(int i=0; i<N; i++){
            nums[i] = ans[i];
        }

    }
}
