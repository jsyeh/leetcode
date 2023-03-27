class Solution {
    public int uniquePaths(int m, int n) {
        int [][] table = new int[m+1][n+1];
        for(int i=0; i<=m; i++){
            table[i][0] = 0;//Integer.MAX_VALUE;
        }
        for(int j=0; j<=n; j++){
            table[0][j] = 0;//Integer.MAX_VALUE;
        }

        table[0][1] = 1;
        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                table[i][j] = table[i-1][j] + table[i][j-1];
            }
        }
        return table[m][n];
    }
}
