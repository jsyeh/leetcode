class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        //題目看不太懂。重點是: 前一次選 M 堆, 下一次要選 1<=X<=2M 且更新 M 為"之前選最多的堆數"
        //感覺上 Dynamic Programming 可以解
        //不過，lee215 參考答案是算 postsum[i] = piles[i]...piles[N-1]
        vector<int> postSum(piles.size()); //也就是第i個pile之後的全部石頭數
        postSum[piles.size()-1] = piles[piles.size()-1];
        for(int i=piles.size()-2; i>=0; i--) postSum[i] = postSum[i+1] + piles[i];

for(int i=0; i<piles.size(); i++) printf("%d ", postSum[i]);
        vector<vector<int>> table(piles.size()); //設定二維陣列的長寬
        for(int i=0; i<piles.size(); i++) table[i].resize(piles.size());

        return dfs(postSum, 1, 0, table);
    }


    int dfs(vector<int> & postSum, int M, int pile, vector<vector<int>>&table) {
        if(pile + 2 * M >= postSum.size()) return postSum[pile];//可把後面全拿
        
        if(table[pile][M]>0) return table[pile][M];//有計算過的狀況
        int ans = 0;
        for(int i=1; i<=2*M; i++) { //這次取幾堆的石頭啊？
            int temp = postSum[pile] - postSum[pile + i];//你現在取的石頭數，就是照著堆數，減
            int nextM = (M>i)? M: i; 
            temp += postSum[pile + i] - dfs(postSum, nextM, pile+i, table);
            if(temp>ans) ans = temp;
            //找所有可能性中，最大的答案
        }
        table[pile][M] = ans;
        return ans;
    }
};
