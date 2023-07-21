int coinChange(int* coins, int coinsSize, int amount){
    int table[amount+1]; //table[i] 表示 i元 要用的最少硬幣數
    for(int i=0; i<=amount; i++) table[i] = -1; //還沒辦法做出來
    table[0] = 0; //0元，0個硬幣，沒問題

    for(int c=0; c<coinsSize; c++){
        int c2 = coins[c];
        for(int i=1; i<=amount; i++){
            if(i-c2>=0){
                if(table[i-c2]==-1) continue; //沒有意義，不要用它
                if(table[i]==-1) table[i] = table[i-c2]+1;
                if(table[i-c2]+1<table[i]) table[i] = table[i-c2]+1;
            }
        }
    }
    return table[amount];
}
