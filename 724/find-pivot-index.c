int pivotIndex(int* nums, int numsSize){
    for(int i=1; i<numsSize; i++){
        nums[i] += nums[i-1];
    }
    for(int ans=0; ans<numsSize; ans++){
        if(ans==0){
            if(nums[numsSize-1]-nums[ans]==0) return 0;
        } else if(nums[ans-1]==nums[numsSize-1]-nums[ans]) return ans;
    }
    return -1;
}
