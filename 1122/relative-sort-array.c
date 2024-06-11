/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    int* ans = (int*) malloc(sizeof(int)*arr1Size); // 先準備好答案要放的 memory
    int H[1001] = {}; // 因數字介於 0...1000範圍, 就開陣列來裝數字
    for(int i=0; i<arr1Size; i++) {  // 先巡一次, 將字統計分類
        H[arr1[i]]++;
    }
    int N = 0; //逐一放數字到 ans[]裡
    for(int i=0; i<arr2Size; i++) { // 照著 arr2[i] 的順序放入
        for(int k=0; k<H[arr2[i]]; k++) {  // 照著「出現的次數」重覆塞入答案裡
            ans[N++] = arr2[i]; 
        }
        H[arr2[i]] = 0; //用完 arr2[i] 了
    }
    // 最後一輪: 把剩下的數字, 依序放上來
    for(int i=0; i<=1000; i++) {
        for(int k=0; k<H[i]; k++) {
            ans[N++] = i;
        }
    }
    *returnSize = arr1Size;
    return ans;
}
