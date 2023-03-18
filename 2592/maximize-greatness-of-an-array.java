class Solution {
    public int maximizeGreatness(int[] nums) {
        Arrays.sort(nums);
        int N = nums.length;
        int i=0, j=0, ans=0;
        while(i<N && j<N){
            while(nums[i]==nums[j]){
                j++;
                if(j>=N)return ans;
            }
            if(nums[i]<nums[j]) ans++;
            i++;
            j++;
        }
        return ans;
    }
}//[1,3,5,2,1,3,1]
//  1 1 1 2 3 3 5
//    2 3 3 5
//Case 
