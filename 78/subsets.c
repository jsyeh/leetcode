// 使用相同的演算法，C 語言的版本雖然會快，但它的memory管理有夠麻煩的
// pointer指標超容易出錯的 -- 熟練的高手，腦中能想像一堆指標指來指去，才不易出錯
// 而且要自己用 malloc() 準備全部陣列的記憶體，難度比較高。建議同學參考就好。
int pow2[] = {1,2,4,8,16,32,64,128,256,512,1024}; //查表用
int ** ans = NULL, * colSize = NULL, * memory = NULL;  //準備好3顆指標
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int N = numsSize;  // input的陣列大小，用短一點的變數，下面比較好懂。
    if(ans==NULL) {  // 為了加速，第1次使用時，用global變數，配置全部memory
        ans = (int**)malloc(sizeof(int*)*pow2[10]);  // 答案所需的陣列大小
        colSize = (int*)malloc(sizeof(int)*pow2[10]);  // 放每個陣列的大小
        memory = (int*)malloc(sizeof(int)*5120);  // 答案指標將使用的memory
    } 
    int memoryUsed = 0;  // 記錄目前已使用多少的 memory
    *returnColumnSizes = colSize;
    for(int mask=0; mask<pow2[N]; mask++) {  // 利用 bit masking 暴力試出全部組合
        ans[mask] = &memory[memoryUsed];  // 先把這次的陣列使用的memory指好
        (*returnColumnSizes)[mask] = 0;  // 一開始此 subset 大小是0，要小心那個圓括號
        for(int i=0; i<N; i++){  // 逐個 bit 處理 
            if((mask & (1<<i)) != 0){  // 每個 bit 對應 nums[i]
                memory[memoryUsed++] = nums[i];  // 把對應的nums[i]值放入此subset
                (*returnColumnSizes)[mask] = (*returnColumnSizes)[mask] + 1;
            }  // 陣列多用一格，要小心那個圓括號
        }
    }
    // printf("memoryUsed: %d\n", memoryUsed); 印出最大使用量5120，以便準備memory
    *returnSize = pow2[N];  // 要回傳的subset全部可能的數量；
    return ans;
}
