class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        //這題再次偷看 lee215 的解法, 它寫得很清楚, 比昨天的挑戰還簡單
        int N = stoneValue.size();
        int table[N]; //如果你從後面往前後 table[i] 表示輪到拿stone[i] 的人最多可以得幾分
        //因為有3種可能拿法, 所以3種拿法都計算, 下一個人會拿再後面的分數

        //最後答案是看 table[0] 的值, 也就是一開始Alice開始拿時, 最終會得到的最多分數是多少

        //想法是倒過來更新。如果你拿了最後幾筆, 從最後的分數進前想。只考後從後往前的分數部分
        table[N-1] = stoneValue[N-1];//最後一個人最拿最後顆石頭,只有一個可能分數
        for(int i=N-2; i>=0; i--) { //要考慮輪到拿 stone[i] 的人的狀況
            table[i] = stoneValue[i] - table[i+1]; //先考慮拿1顆的狀況, 你拿1顆,別人拿stone[i+1]之後
            int temp = stoneValue[i];
            for(int k=1; k<3 && i+k<N; k++) { //可拿1顆(前一行有處理)、2顆、3顆, 得到的分數, 與下一個人的分數有關
                temp += stoneValue[i+k];//多拿一顆的值
                if(i+k+1<N){ //下一個人 table[i+k+1] 沒超過陣列, 就要考慮下一個人 -table[i+k+1]
                    if(temp - table[i+k+1]>table[i]) table[i] = temp - table[i+k+1];
                }else{
                    if(temp > table[i]) table[i] = temp;//沒有後一個的機會, 就不要 - table[i+k+1];
                }
                //如果再多拿一顆,讓你得到更多分、更有優勢, 那換多拿一顆的數
            }
            //迴圈從後往前, 表示有 "後見之明", 思考的方式, 是如果後面的結果已知, 那現在要挑幾顆最有優勢
        }

        if(table[0]>0)return "Alice";
        else if(table[0]<0)return "Bob";
        else return "Tie";
    }
};
