class Solution {
    public int shortestBridge(int[][] grid) {
        //先用 connected components ，把兩個island找出來。
        //再利用Dilate看長多久後，island 2 可找到 island 3

        int ID=2; //第1個島是2, 第2個島是3
        int N = grid.length;
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]==1) { //找到陸地，馬上用DFS染色成ID
                    dfs(grid, i, j, ID);
                    ID++;
                }
            }
        }
        int[][] grid2 = new int[N][N];
        //print("grid", grid);
        //print("grid2", grid2);
        copy(grid2,grid);//grid2[i][j] = grid[i][j]
        for(int k=0; k<N;k++) {        
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++){
                    if(grid[i][j]==2){
                        test(grid, grid2, i-1, j);
                        test(grid, grid2, i+1, j);
                        test(grid, grid2, i, j-1);
                        test(grid, grid2, i, j+1);
                        if(touched) return k;
                    }
                }
            }
            int[][] temp = grid;
            grid = grid2;
            grid2 = temp; //把兩個grid交換，下一輪再繼續成長
        //print("grid", grid);
        //print("grid2", grid2);
        }
        //print("grid", grid);
        //print("grid2", grid2);
        return 0;
    }

    boolean touched = false;

    void copy(int[][] grid2, int[][] grid) {
        int N = grid.length;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                grid2[i][j] = grid[i][j];
            }
        }
    }
    /*void print(String name, int[][] grid) {
        System.out.println(name);
        int N = grid.length;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                System.out.print(grid[i][j]+" ");
            }
            System.out.println();
        }

    }*/

    void test(int[][] grid, int[][] grid2, int i, int j) {
        //會呼叫test()便表示它是2的鄰居
        int N = grid.length;
        if(i<0 || j<0 || i>=N || j>=N) return;

        grid2[i][j] = 2;
        if(grid[i][j]==3) touched = true;
    }

    void dfs(int[][] grid, int i, int j, int ID) {
        int N = grid.length;
        if(i<0 || j<0 || i>=N || j>=N) return;

        if(grid[i][j]!=1) return;

        grid[i][j] = ID;
        dfs(grid, i+1, j, ID);
        dfs(grid, i-1, j, ID);
        dfs(grid, i, j+1, ID);
        dfs(grid, i, j-1, ID);
    }
}
