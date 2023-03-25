class Pos {
    int i, j;
    Pos(int _i, int _j) {
        i = _i;
        j = _j;
    }
}
class Solution {
    int M, N;
    boolean [][] visited;
    public int numIslands(char[][] grid) {
        M = grid.length;
        N = grid[0].length;
        visited = new boolean[M][N];

        int ans = 0;
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(visited[i][j] || grid[i][j]=='0') continue;

                LinkedList<Pos> queue = new LinkedList<Pos>();
                queue.push(new Pos(i,j));
                visited[i][j] = true;
                ans++;

                while(queue.size()>0){
                    Pos now = queue.pop();
                    testAndAdd(grid, now.i-1, now.j, queue);
                    testAndAdd(grid, now.i+1, now.j, queue);
                    testAndAdd(grid, now.i, now.j-1, queue);
                    testAndAdd(grid, now.i, now.j+1, queue);
                }
            }
        }

        return ans;
    }

    void testAndAdd(char[][] grid, int i, int j, LinkedList<Pos> queue) {
        if(i<0) return;
        if(j<0) return;
        if(i>=M) return;
        if(j>=N) return;
        if(visited[i][j]) return;
        if(grid[i][j]=='0') return;

        queue.push(new Pos(i,j));
        visited[i][j]=true;
    }
}
