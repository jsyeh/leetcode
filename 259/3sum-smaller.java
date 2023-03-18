class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int N = nums.length;
        int ans=0;
        for(int i=0; i<N-2; i++){
            for(int j=i+1; j<N-1; j++){
                for(int k=j+1; k<N; k++){
                    if(nums[i]+nums[j]+nums[k]<target) ans++;
                    else break;
                }
            }
        }
        return ans;
    }
}
