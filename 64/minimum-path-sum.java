class Solution {
    public int minPathSum(int[][] grid) {
        int I = grid.length, J = grid[0].length;
        int [][] table = new int[I+1][J+1];
        // table[i][j] 表示如果要走到 grid[i][j] 最小的值是多少

        for(int i=0; i<=I; i++){
            table[i][0] = Integer.MAX_VALUE;
        }
        for(int j=0; j<=J; j++){
            table[0][j] = Integer.MAX_VALUE;
        }

        table[0][1] = 0;
        for(int i=1; i<=I; i++){
            for(int j=1; j<=J; j++){
                int prev = Math.min(table[i-1][j], table[i][j-1]);
                table[i][j] = prev + grid[i-1][j-1];
            }
        }
        return table[I][J];
    }
}
