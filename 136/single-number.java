class Solution {
    public int singleNumber(int[] nums) {
        int N = nums.length;
        int [] H = new int[60001];
        for(int i=0; i<N; i++){
            H[nums[i]+30000]++;
        }
        for(int i=0; i<60001; i++){
            if(H[i]%2==1) return i-30000;
        }
        return 0;
    }
}
