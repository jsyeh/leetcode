double new21Game(int n, int k, int maxPts){
    if(k==0) return 1; //k竟然是0, 就表示"隨隨便便都可以結束", 機會是1, 一定會成功
    if(n>=k+maxPts) return 1; //n點超級大的話, 可接受的範圍就超級大, 就一定不會爆, 一定會成功
    //(其實以上是偷看 lee215的答案, 才知道的)
    double table[n+1];
    table[0] = 1; //table[i] 表示：（到達i的）機率
    //一開始一定會到達0點, 所以 table[0] 的機率是1
    
    //因為maxPts 的範圍內, 每一個點的可能性都一樣, 所以我們要計算"到達table[i]" 的機率時, 就是
    //把前面 table[i-1]...table[i-maxPts] 都加起來, 當分子, 再除以 maxPts 分母, 得到 table[i]機率
    //所以, 我們的 WindowSum 就一直是"之前 maxPts" 數量的和。 

    double WindowSum = table[0];
    double ans = 0;
    for(int i=1; i<=n; i++){
        table[i] = WindowSum / maxPts;//前面幾項比較委曲, 沒辦法加到太多項, 但還是要除上全部可能的點數
        //後面要進行 WindowSum 的更新, 以便下一輪計算 table[i] 機率
        //WindowSum += table[i];
        if(i<k) WindowSum += table[i]; //因為遊戲在得到K點後就結束, 所以之後不要再加了!
        else ans += table[i];//遊戲結束後, 這些機率都要加起來。真巧, 剛好和上面這行if()一起搞定

        if(i>=maxPts) WindowSum -= table[i-maxPts]; //因前面幾項比較委曲, 就不用扣掉。後面才扣掉前面項
        //這個程式的精華, 其實是在 WindowSum 來知道 table[i] 之前很多項加起來的機率可能性(有再除maxPts)
    }
    return ans;
}//case 127/151: 0 0 1 天啊,好短的case 這是特殊狀況, 原本程式的迴圈沒有處理到, 所以例外處理
