/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// LeetCode 1310. XOR Queries of a Subarray
// queries[i] 有範圍left,right，把 arr[left]...arr[right] 算出 XOR 的結果
// 可仿效 preSum 的方法，把 preXor 算出來，再用「扣除」的概念，就可快速推算出答案
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int preXor[arrSize+1];
    preXor[0] = 0; //凡事從0開始
    for(int i=0; i<arrSize; i++){
        preXor[i+1] = preXor[i] ^ arr[i];
    } // 建出 Xor 表格，對應arr[0]... arr[i] 的 Xor 結果
    int * ans = (int*)malloc(sizeof(int)*queriesSize);
    for(int i=0; i<queriesSize; i++){ // query[0] 左界 ... query[1] 右界
        int left = queries[i][0], right = queries[i][1];
        ans[i] = preXor[right+1] ^ preXor[left];
        // 多了 preXor[0], 所以 [left...right] 對應到 [left+1...right+1]
        // 要扣除的時候，就 preXor[right+1] 扣除 preXor[left]
    }
    *returnSize = queriesSize;
    return ans;    
}
