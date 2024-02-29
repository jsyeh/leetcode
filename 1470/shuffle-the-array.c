// 原本是「先一堆x、再一堆y」, 要改成「x,y交錯」

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int N = numsSize / 2;
    int x[N]; //先開一堆x,把x的答案copy過來
    memcpy(x,nums,numsSize/2*sizeof(int));
    for(int i=0; i<N; i++){ //再逐一放回 x[2*i] 及 x[2*i+1]
        nums[2*i+0] = x[i]; //剛剛備份的x[i]
        nums[2*i+1] = nums[N+i]; //對應到 y[i] 的值, 交錯放回 nums[i]
    }
    *returnSize = numsSize;
    return nums;
}
