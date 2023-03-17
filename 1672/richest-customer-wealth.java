class Solution {
    public int maximumWealth(int[][] accounts) {
        
        int max_wealth = 0;
        for(int i=0; i<accounts.length; i++){
            int now = 0;
            for(int j=0; j<accounts[i].length; j++){
                now += accounts[i][j];
            }
            if(now>max_wealth) max_wealth = now;
        }
        return max_wealth;
    }
}
