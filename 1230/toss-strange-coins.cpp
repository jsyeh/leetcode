class Solution {
public:
    double probabilityOfHeads(vector<double>& prob, int target) {
        int N = prob.size();
        double table[N+1][N+1];//table[i][target]: 使用前i個coins,要投出target個正面

        table[0][0]=1;//0個coin,0個正面的機率很高
        table[0][1]=0;
        for(int coin = 0; coin<N; coin++){
            for(int t=0; t<=target; t++){
                table[coin+1][t] = table[coin][t]*(1-prob[coin]);
                if(t>0) table[coin+1][t] += table[coin][t-1]*prob[coin];
            }
        }
        return table[N][target];
    }
};
