// LeetCode 2161. Partition Array According to Given Pivot
// 給 pivot，小的放左邊、大的放右邊、相同的放中間，順序要保持。
// 這次用 3 個迴圈，先取出「小的」，再取出「相同」，最後取出「大的」
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int * ans = (int*) malloc(sizeof(int)*numsSize); // 手動準備 memory
    int ansN = 0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]<pivot) ans[ansN++] = nums[i]; // 小的放左邊
    }
    for(int i=0; i<numsSize; i++){
        if(nums[i]==pivot) ans[ansN++] = nums[i]; // 相同放中間
    }
    for(int i=0; i<numsSize; i++){
        if(nums[i]>pivot) ans[ansN++] = nums[i]; // 小的放左邊
    }
    *returnSize = numsSize; // C 要記得註明「陣列有多大」
    return ans;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
