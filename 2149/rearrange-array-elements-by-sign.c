// 題目保證 nums[i] 有一半正的、一半負的
// 回傳結果，要「正的、負的」相間隔，而且正數間的順序不能變，負數也是。
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int positive[numsSize/2], negative[numsSize/2], pi=0, ni=0; 
    for(int i=0; i<numsSize; i++){ // 先把 nums[i] 照正負來分類
        if(nums[i]<0){
            negative[ni] = nums[i]; // 負的放這裡
            ni++;
        }else{
            positive[pi] = nums[i]; // 正的放這裡
            pi++;
        }
    }
    for(int i=0; i<numsSize/2; i++){ // 再依序塞回去
        nums[i*2+0] = positive[i]; // 先塞正的
        nums[i*2+1] = negative[i]; // 再塞負的
    }
    *returnSize = numsSize; // C 比較麻煩，要再設定 array 的 returnSize
    return nums;
}
