class Solution {
    //啊，很亂，重寫啦！
    public int coinChange(int[] coins, int amount) {
        int [][] table = new int[coins.length+1][amount+1];
        for(int i=0; i<=coins.length; i++){
            for(int j=0; j<=amount; j++){
                table[i][j] = -1;
            }
        }
        for(int k=0; k<=coins.length; k++){
            table[k][0]=0;
        }
        Arrays.sort(coins);
        for(int i=1; i<=coins.length; i++){
            for(int k=1; k<=amount; k++){
                int prev = k - coins[i-1];
                if(prev<0){
                    table[i][k] = table[i-1][k];
                    continue;
                }
                int a = table[i-1][k];
                int b = table[i][prev];
                if(a==-1 && b==-1) continue;
                else if(a==-1) table[i][k] = b+1;
                else if(b==-1) table[i][k] = a;
                else table[i][k] = min(a, b+1);
            }
        }
        return table[coins.length][amount];
    }
    int min(int a, int b) { //which is smaller
        if(a<b) return a;
        else return b;
    }
}
