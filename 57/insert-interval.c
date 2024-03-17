//這題無法回收再利用 intervals, 因為有可能要「增加1格」，
//又為了想快一點、不要每次都 malloc()要記憶體 所以程式碼變得很雜亂
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    int N1=0, N2=0, N3=0;
    int s2 = newInterval[0], e2 = newInterval[1];
    for(int i=0; i<intervalsSize; i++){
        if(intervals[i][1]<s2) N1++; //放左邊國
        else if(e2<intervals[i][0]) N3++; //放右邊國
        else{ //交錯的部分
            if(intervals[i][0]<s2) s2=intervals[i][0]; //更新s2
            if(intervals[i][1]>e2) e2=intervals[i][1]; //更新e2
            N2++; //這些是要減損的，因為最後只能留下一筆 (s2,e2)
        }
    }
    if(N2==1){ //筆數剛好，不用再準備 memory
        //把s2,e2 放進去
        intervals[N1][0] = s2;
        intervals[N1][1] = e2;
        //把右邊國 依序放進來
        *returnColumnSizes = intervalsColSize;
        *returnSize = intervalsSize;
        return intervals;
    }else if(N2>1){ //要減少筆數，可以使用原本 memory
        intervals[N1][0] = s2;
        intervals[N1][1] = e2;
        for(int i=0; i<N3; i++){ //把右邊國，往左稍移
            intervals[N1+1+i][0] = intervals[N1+N2+i][0];
            intervals[N1+1+i][1] = intervals[N1+N2+i][1];
        }
        *returnColumnSizes = intervalsColSize; //回收再利用
        *returnSize = N1+1+N3; //筆數由 N1+N2+N3 變成 N1+1+N3
        return intervals; //回收再利用
    }else{ //沒有任何重疊、合併發生。所以要新增 memory
        *returnColumnSizes = (int*)malloc(sizeof(int)*(N1+1+N3));
        int* returnAll = (int*)malloc(sizeof(int)*(N1+1+N3)*2);
        int** ans = (int**)malloc(sizeof(int*)*(N1+1+N3));
        for(int i=0; i<N1; i++){
            ans[i] = &returnAll[i*2];
            ans[i][0]=intervals[i][0];
            ans[i][1]=intervals[i][1];
            (*returnColumnSizes)[i] = 2;
        }
        ans[N1] = &returnAll[N1*2];
        ans[N1][0] = s2;
        ans[N1][1] = e2;
        (*returnColumnSizes)[N1] = 2;
        for(int i=N1; i<N1+N3; i++){
            ans[1+i] = &returnAll[(1+i)*2];
            ans[1+i][0] = intervals[i][0];
            ans[1+i][1] = intervals[i][1];
            (*returnColumnSizes)[i+1] = 2;
        }
        for(int i=0; i<N1+1+N3; i++){
            printf("size: %d\n", (*returnColumnSizes)[i]);
        }
        *returnSize = N1+1+N3; //筆數由 N1+N2+N3 變成 N1+1+N3
        return ans; //回收再利用
    }
}
//case 2/156: intervals = [], newInterval = [5,7]
