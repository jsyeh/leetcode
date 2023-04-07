/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    int * ans = (int*) malloc(numsSize*sizeof(int));///有點難懂,要自己 malloc
    *returnSize = numsSize;
    ans[0] = nums[0];
    for(int i=1; i<numsSize; i++){
        ans[i] = ans[i-1] + nums[i];
    }

    return ans;
}
