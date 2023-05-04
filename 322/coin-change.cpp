class Solution {
public:
    int min(int a, int b) {
        if(a==INT_MIN) return b;
        if(b==INT_MIN) return a;
        if(a<b) return a;
        else return b;
    }
    int coinChange(vector<int>& coins, int amount) {
        int cN = coins.size();
        int table[cN+1][amount+1];//fewest number of coins

        for(int c=0; c<=cN; c++) table[c][0] = 0;
        for(int a=0; a<=amount; a++) table[0][a] = INT_MAX;
        
        for(int c=1; c<=cN; c++){
            int coin = coins[c-1];
            for(int a=1; a<=amount; a++){
                table[c][a] = table[c-1][a];
                if(a>=coin && table[c][a-coin]!=INT_MAX){
                    table[c][a] = min(table[c][a-coin]+1, table[c][a]);
                }
            }
        }
        if(table[cN][amount]==INT_MAX) return -1;
        else return table[cN][amount];
    }
};
