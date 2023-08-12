public class Solution {
    public int UniquePathsWithObstacles(int[][] grid) {
        if(grid[0][0]==1) return 0; //最左上角出發點卡住，就沒辦法走

        //C# 用 .Length 而 Java 用 .length 而 C++ 用 ArrayList size()
        int M = grid.Length, N = grid[0].Length;
        int [,]table = new int[M,N];
        //C# 的規則陣列，是用 int[,] table = new int[3,4];
        //不規則陣列，是 int[][] table = new int[3][]; 再逐一new
        // table[0] = new int[4]; 
        // table[1] = new int[4]; 
        // table[2] = new int[4]
        //https://ithelp.ithome.com.tw/articles/10213228


        table[0,0] = 1; //出發點有1個可能
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if(grid[i][j]==1) table[i,j] = 0;
                else{
                    if(i!=0) table[i,j] = table[i-1,j];
                    if(j!=0) table[i,j] += table[i,j-1];
                }
            }
        }
        return table[M-1,N-1];
    }
}
