// LeetCode 2460. Apply Operations to an Array
// 如果 nums[i] == nums[i+1] 就把 nums[i] *= 2 並把 nums[i+1] = 0
// 巡一輪後，再把 0 移到 nums 右邊，就完成了！ 
int* applyOperations(int* nums, int numsSize, int* returnSize) {
    for(int i=0; i<numsSize-1; i++) { // 照著巡一輪
        if(nums[i]==nums[i+1]) { // 左右相等
            nums[i] *= 2; // 照題目「乘2倍」
            nums[i+1] = 0; // 照題目「變成0」
        }
    }
    int k = 0; // 要搬家
    for(int i=0; i<numsSize; i++) {
        if(nums[i]!=0) nums[k++] = nums[i];
    } // 把「非0項」左移
    for(int i=k; i<numsSize; i++) nums[i] = 0; // 剩下的填0

    *returnSize = numsSize; // LeetCode 的 C 要給「陣列大小」
    return nums;
}
