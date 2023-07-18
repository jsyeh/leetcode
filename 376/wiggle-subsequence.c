int wiggleMaxLength(int* nums, int numsSize){
    int up[numsSize+1], down[numsSize+1];
    up[0]=0; //up[i] 表示第i 為止(包含nums[i])，往上最多的數目
    down[0]=0;
    int ans = 0;
    for(int i=1; i<numsSize; i++){
        int now = nums[i];
        int maxdown=0, maxup=0;
        for(int k=0; k<i; k++){
            if(nums[k]<nums[i]){ //合理的up
                if(down[k]+1>maxup) maxup = down[k]+1;
            }
            if(nums[k]>nums[i]){
                if(up[k]+1>maxdown) maxdown = up[k]+1;
            }
        }
        up[i] = maxup;
        down[i] = maxdown;
        if(maxdown>ans) ans = maxdown;
        if(maxup>ans) ans = maxup;
        //printf("nums[i]: %d maxup: %d maxdown: %d\n", nums[i], maxup, maxdown);
    }
    return ans+1;
}
