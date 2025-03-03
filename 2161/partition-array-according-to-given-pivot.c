// LeetCode 2161. Partition Array According to Given Pivot
// 給 pivot，小的放左邊、大的放右邊、相同的放中間，順序要保持。
// 在 C 語言裡，準備 memory 很麻煩。用「浪費memory」的方法，大的另外放，最後再放回 nums。
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int right[numsSize]; // 準備額外的 memory 放「右邊大的」
    int leftN = 0, rightN = 0; // 對應左邊、右邊的數量
    for(int i=0; i<numsSize; i++){
        if(nums[i]<pivot) nums[leftN++] = nums[i]; // 小的放「原本陣列 nums」
        else if(nums[i]>pivot) right[rightN++] = nums[i]; // 大的放 right 陣列
    }
    for(int i=leftN; i<numsSize-rightN; i++) {
        nums[i] = pivot; // 複製相同的，放中間
    }
    for(int i=numsSize-rightN; i<numsSize; i++) {
        nums[i] = right[i-numsSize+rightN]; // 右邊大的，再挪回 nums 裡
    } 
    *returnSize = numsSize; // C 要記得註明「陣列有多大」
    return nums; // 重覆使用原本的陣列，就不用再用 malloc() 宣告陣列的 memory 了
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
