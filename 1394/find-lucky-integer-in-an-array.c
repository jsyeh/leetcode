int findLucky(int* arr, int arrSize) {
    int ans = -1;
    int H[501] = {}; // 統計出現的次數，上限是500
    for(int i=0; i<arrSize; i++){ // 逐一處理
        H[arr[i]]++; // 多找到1個
    }
    for(int i=500; i>0; i--){ // 倒著數，500...1
        if(H[i]==i) return i; // 最大的 lucky integer 
    }
    return -1; // 沒找到答案
}
