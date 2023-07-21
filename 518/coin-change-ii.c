int change(int amount, int* coins, int coinsSize){
    int table[amount+1];
    for(int i=0; i<=amount; i++){ //第0種幣 coins[0] 
        if(i%coins[0]==0) table[i]=1; //是倍數時，便能用此幣支付
        else table[i]=0; //不是的話，就沒有用此幣的可能
    }//先建出基礎的表格
    //接著測試其他的幣
    for(int c=1; c<coinsSize; c++){
        int c2 = coins[c];
        for(int i=c2; i<=amount; i++){
        //i不夠大時，沒辦法使用 c2 這種幣
            table[i] += table[i-c2]; //夠大時，能逐一使用此幣，增加支付的可能性
        }
    }
    return table[amount];
}
