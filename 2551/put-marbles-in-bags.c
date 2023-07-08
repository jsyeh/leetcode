//參考 lee215 的解法，他說問題其實很簡單，就是要找切割點的左右加起來
//所以只要把相鄰的事先加起來，變成新的陣列。排序後，找到最的的前k項，減掉最小的前k項，答案就出來了
int comp(const void * p1, const void * p2){
    return *(int*)p1 - *(int*)p2;
}
long long putMarbles(int* weights, int weightsSize, int k){
    int N = weightsSize;
    int b[N];
    for(int i=0; i<N-1; i++){ //會少1筆哦！
        b[i] = weights[i] + weights[i+1]; //相鄰相加 的新的陣列
    }
    qsort(b, N-1, sizeof(int), comp);

    long long int small = 0, large = 0;
    for(int i=0; i<k-1 ;i++){ //不能算前k筆，而是前k-1筆，因為切 k-1 刀，才會分成 k 段
        small += b[i];
        large += b[N-2-i];
    }
    return large - small;
}
