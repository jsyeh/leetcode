// 你只有2個籃子，即「只能採集」2種水果。
// 從 fruits[i] 開始往右採集，只能採集2種水果，可採集多少水果。
// 可使用 sliding window 來處理。我模仿之前寫的 Python 程式, 改用 C 實作
int totalFruit(int* fruits, int fruitsSize) {
    int a = 0, b = 0, bN = 0; //a是前一籃的水果編號, b是後一籃的水果編號, bN是b水果連續累積幾個
    int ans = 0, cur = 0; //ans最後的答案, cur目前這個的答案
    for(int i=0; i<fruitsSize; i++){
        if(fruits[i]==b){ //與最後一籃的b水果相同
            cur ++; //現在的答案變長
            bN ++; // b水果+1
        }else if(fruits[i]==a){ //與前一籃的a水果相同
            cur ++; //現在的答案變長
            int temp = a;
            a = b;
            b = temp; //將兩籃交換
            bN = 1; //重新從1開始, 目前 b 連續 1個
        }else{ //不幸fruits[i]與a,b都不相同, 要捨棄a了
            cur = bN + 1; //之前的b變a,長度+現在新水果1個
            a = b; //b變成前一籃的a
            b = fruits[i]; //新的b
            bN = 1; ////重新從1開始, 目前 b 連續 1個
        }
        if(cur>ans) ans = cur;
    }
    return ans;
}
