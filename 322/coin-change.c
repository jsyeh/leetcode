int min(int a, int b){
    if(b==INT_MIN) return a; //因為 INT_MAX+1會overflow,所以要保護一下,不要用它
    if(a==INT_MIN) return b;
    if(a<b) return a;
    else return b;
}
int coinChange(int* coins, int coinsSize, int amount){
    double table[coinsSize+1][amount+1];
    for(int a=0; a<=amount; a++) table[0][a] = INT_MAX;

    for(int c=1; c<=coinsSize; c++){
        table[c][0] = 0; //0元需要0個coin
        int coin = coins[c-1];//現在使用的 coin 幣值

        for(int a=1; a<=amount; a++){
            if(a-coin<0) table[c][a] = table[c-1][a];
            else table[c][a] = min(table[c-1][a], table[c][a-coin]+1);
        }
    }

    if(table[coinsSize][amount]==INT_MAX) return -1;
    else return (int)table[coinsSize][amount];
}
