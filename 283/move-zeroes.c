void moveZeroes(int* nums, int numsSize){
    int N=0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]!=0) nums[N++] = nums[i];
    }
    for(int i=N; i<numsSize; i++) nums[i] = 0;
}
