class Pos {
    int i, j;
    Pos(int _i, int _j) {
        i = _i;
        j = _j;
    }
}
class Solution {
    int I, J;
    LinkedList<Pos> queue = new LinkedList<Pos>();
    public int maxAreaOfIsland(int[][] grid) {
        int ans=0;
        I = grid.length;
        J = grid[0].length;
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
                int area = 0;
                if(grid[i][j]==1){
                    testAndPush(grid, i, j);
                    while(queue.size()>0){
                        Pos now = queue.pop();
                        area++;
                        testAndPush(grid, now.i+1,now.j);
                        testAndPush(grid, now.i-1,now.j);
                        testAndPush(grid, now.i,now.j+1);
                        testAndPush(grid, now.i,now.j-1);
                    }
                    System.out.println(area);
                    if(area>ans) ans = area;
                }
            }
        }
        return ans;
    }

    void testAndPush(int [][] grid, int i, int j) {
        if(i<0 || j<0 || i>=I || j>=J) return;
        if(grid[i][j]==0) return;

        grid[i][j]=0;
        queue.push(new Pos(i,j));
    }
}
