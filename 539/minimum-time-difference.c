// LeetCode 539. Minimum Time Difference
// 給一堆字串，內含 24小時制的時間，問「它們間最小的時間差多少?」
int cmp(const void*p1, const void*p2){ // 給 qsort() 用的 compare比大小函式
    return *(int*)p1 - *(int*)p2;
}
int findMinDifference(char** timePoints, int timePointsSize) {
    int a[timePointsSize]; // LeetCode 用 gcc 13 可這樣宣告陣列
    int hh, mm; // 需要的變數
    for(int i=0; i<timePointsSize; i++){ // 用簡單的迴圈
        sscanf(timePoints[i], "%d:%d", &hh, &mm); //用 sscanf()斷字
        a[i] = hh*60+mm; // 算出「00:00到hh:mm差幾分鐘」
    }
    qsort(a, timePointsSize, sizeof(int), cmp); // 再排序就好了
    int ans = a[0] + 24*60 - a[timePointsSize-1]; // 頭尾跨午夜 24:00 當初始值
    for(int i=0; i<timePointsSize-1; i++){ //兩兩比較
        if(a[i+1]-a[i]<ans) ans = a[i+1] - a[i]; // 找最小值
    }
    return ans;
}
