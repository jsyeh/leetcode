//把陣列中，全部的數字（除了自己本身）都乘起來
// 不能先暴力乘起來，因為數字會太大。所以拆成「左半」乘「右半」
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int prefix[numsSize]; //prefix[i] 對應 nums[0]...nums[i]的乘積
    int suffix[numsSize]; //suffix[i] 對應 nums[i]...最後項 的乘積
    int p = 1; //用來放 prefix乘積
    for(int i=0; i<numsSize; i++){
        p *= nums[i];
        prefix[i] = p;
    }
    int s = 1; //用來放 suffix 乘積
    for(int i=numsSize-1; i>=0; i--){
        s *= nums[i];
        suffix[i] = s;
    }
    //前面處理好 prefix 及 suffix 乘積後，便能每項算出來
    for(int i=0; i<numsSize; i++){
        nums[i] = 1; // 先放基礎的1，方便下面乘法
        if(i>0) nums[i] *= prefix[i-1]; //乘左邊
        if(i<numsSize-1) nums[i] *= suffix[i+1]; //乘右邊
    }
    *returnSize = numsSize; //回傳陣列的大小
    return nums; //回收再利用 nums 陣列
}
