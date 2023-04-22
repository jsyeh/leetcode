class Pos {
    int i, j, len;
    Pos(int _i, int _j) {
        i = _i;
        j = _j;
    }
    Pos(int _i, int _j, int _len) {
        i = _i;
        j = _j;
        len = _len;
    }
}
class Solution {
    int M, N;
    boolean [][] visited;
    Queue<Pos> queue = new LinkedList<Pos>();    
    public int shortestPathBinaryMatrix(int[][] grid) {
        if(grid[0][0]==1) return -1; //無法走
        M = grid.length;
        N = grid[0].length;

        visited = new boolean[grid.length][grid[0].length];
        testAndAdd(grid, 0, 0, 1);
        queue.offer(new Pos(0,0,1));
        while(queue.size()>0){
            Pos now = queue.poll();
            if(now.i==M-1 && now.j==N-1) return now.len;
            for(int i=now.i-1; i<=now.i+1; i++){
                for(int j=now.j-1; j<=now.j+1; j++){
                    testAndAdd(grid, i, j, now.len+1);
                }
            }
        }
        return -1;
    }
    void testAndAdd(int[][] grid, int i, int j, int len) {
        if(i<0 || j<0 || i>=M || j>=N) return;
        if(visited[i][j]) return;
        visited[i][j] = true;
        if(grid[i][j]==1) return;
        queue.offer(new Pos(i, j, len));
    }
}//case 64/89: 很長的陣列
