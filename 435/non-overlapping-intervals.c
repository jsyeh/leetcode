int comp(const void*p1, const void*p2){
    return (*(int**)p1)[1]-(*(int**)p2)[1]; //照著end時間做排序
}
int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize){
    int N = intervalsSize;
    qsort(intervals, N, sizeof(int)*2, comp);

    //for(int i=0; i<N; i++){
    //    printf("%d %d\n", intervals[i][0], intervals[i][1]);
    //}

    int end = intervals[0][1];//第1筆，結束的時間
    int count = 1;//算1筆
    for(int i=1; i<N; i++){
        if(intervals[i][0] >= end){//有機會放進去
            end = intervals[i][1];
            count++;//就多一筆
        }
    }

    return N-count;
}
