class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int N = costs.size(), K = costs[0].size();
        int table[N+1][K];
        //考慮n間房，如果最後1間挑此色k，最便宜的組合

        for(int k=0; k<K; k++) table[0][k]=0;//0間房，0元

        for(int n=1; n<=N; n++){ //1間房 算到 全部N間房
            for(int k=0; k<K; k++){ //如果最後1間想挑色彩K
                //前一間房不是k的，全部要考慮
                int min = INT_MAX;
                for(int prevK=0; prevK<K; prevK++){
                    if(k!=prevK && table[n-1][prevK]<min) min = table[n-1][prevK];
                    //前一間房不是色彩k, 且是最便宜的，記下來
                }
                table[n][k] = min + costs[n-1][k];
                //現在的花費，是最便宜的，加上此間用色彩k的花費
            }
        }
        
        int ans = INT_MAX;
        for(int k=0; k<K; k++){ //最後一間，各種色彩都去找
            if(table[N][k]<ans) ans = table[N][k];
        }
        return ans;
    }
};
