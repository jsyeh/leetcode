class Pos {
    int i, j;
    Pos(int _i, int _j) {
        i = _i;
        j = _j;
    }
}
class Solution {
    int I, J;
    boolean [][] visited;
    LinkedList<Pos> queue;
    public int numEnclaves(int[][] grid) {
        I = grid.length;
        J = grid[0].length;
        visited = new boolean[I][J];
        queue = new LinkedList<Pos>();
        for(int i=0; i<I; i++){
            doVisit(grid, i, 0);
            doVisit(grid, i, J-1);
        }
        for(int j=0; j<J; j++){
            doVisit(grid, 0, j);
            doVisit(grid, I-1, j);
        }
        while(queue.size()>0){
            Pos now = queue.pop();
            doVisit(grid, now.i+1, now.j);
            doVisit(grid, now.i-1, now.j);
            doVisit(grid, now.i, now.j+1);
            doVisit(grid, now.i, now.j-1);
        }
        int ans=0;
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
                System.out.print(grid[i][j] + " ");
                if(grid[i][j]==1) ans++;
            }
            System.out.println();
        }
        return ans;
    }
    void doVisit(int[][] grid, int i, int j) {
        if(i<0 || i>=I || j<0 || j>=J) return;
        if(visited[i][j]) return;
        visited[i][j]=true;
        if(grid[i][j]==1){
            queue.push(new Pos(i,j));
            grid[i][j]=-1;
        }
    }
}//case3: [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
//[[0,0,0,1,1,1,0,1,0,0],
// [1,1,0,0,0,1,0,1,1,1],
// [0,0,0,1,1,1,0,1,0,0],
// [0,1,1,0,0,0,1,0,1,0],
// [0,1,1,1,1,1,0,0,1,0],
// [0,0,1,0,1,1,1,1,0,1],
// [0,1,1,0,0,0,1,1,1,1],
// [0,0,1,0,0,1,0,1,0,1],
// [1,0,1,0,1,1,0,0,0,0],
// [0,0,0,0,1,1,0,0,0,1]]
