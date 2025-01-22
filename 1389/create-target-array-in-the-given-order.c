// LeetCode 1389. Create Target Array in the Given Order
// 將 nums[i] 照著 index[i] 的位置，插入 target 陣列裡
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    int* ans = (int*) malloc(sizeof(int)*numsSize);
    for(int i=0; i<numsSize; i++) {
        int ii = index[i]; // 要插入的位置
        for(int k=i; k>ii; k--) { // 把那個位置「右邊」的數，都往右挪
            ans[k] = ans[k-1];
        }
        ans[ii] = nums[i]; // 有空位後，插入現在的數 nums[i]
    }
    *returnSize = numsSize;
    return ans;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
