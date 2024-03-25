//想找到重覆的數
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    int ansN = 0;
    int happened[100001] = {};
    for(int i=0; i<numsSize; i++){
        happened[nums[i]]++;
        if(happened[nums[i]]==2){
            nums[ansN++] = nums[i]; //記錄重覆的數字
        } //回數再利用 nums[]
    }
    *returnSize = ansN;
    return nums;
}
