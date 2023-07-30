int missingElement(int* nums, int numsSize, int k){
    for(int i=1; i<numsSize; i++){
        int diff = nums[i] - nums[i-1];
//printf("k:%d diff:%d\n", k, diff);
        if(diff>1){
            if(k>diff-1) k -= diff - 1;
            else return nums[i-1] + k;
        }
    }//離開迴圈，表示k-th 在最後數字的再後面
    return nums[numsSize-1] + k;
}
