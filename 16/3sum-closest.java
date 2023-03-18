class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int N = nums.length;
        int bestSum = nums[0]+nums[1]+nums[2];
        int minDist = bestSum-target;
        if(minDist<0) minDist = -minDist;
        for(int i=0; i<N-2; i++){
            for(int j=i+1; j<N-1; j++){
                for(int k=j+1; k<N; k++){
                    int now = nums[i]+nums[j]+nums[k];
                    int diff = target-now;
                    if(diff<0) diff = -diff;
                    if(diff<minDist){
                        minDist=diff;
                        bestSum=now;
                    }
                }
            }
        }
        return bestSum;
    }
}
