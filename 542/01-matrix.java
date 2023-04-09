class Pos {
    int i, j, dist;
    Pos(int _i, int _j, int _dist) {
        i = _i;
        j = _j;
        dist = _dist;
    }
}
class Solution {
    int I, J;
    boolean[][] visited;
    int[][] ans;
    LinkedList<Pos> queue = new LinkedList<Pos>();
    public int[][] updateMatrix(int[][] mat) {
        //00:52 start
        I = mat.length;
        J = mat[0].length;
        ans = new int[I][J];
        visited = new boolean[I][J];
        
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
                if(mat[i][j]==0){
                    visit(mat, i, j, 0);
                    //queue.push(new Pos(i, j, 0));
                }
            }
        }
        while(queue.size()>0) {
            Pos now = queue.pop();
            visit(mat, now.i-1, now.j, now.dist+1);
            visit(mat, now.i+1, now.j, now.dist+1);
            visit(mat, now.i, now.j-1, now.dist+1);
            visit(mat, now.i, now.j+1, now.dist+1);
        }
        return ans;
    }
    //不能使用DFS，因為會算錯。應用BFS
    void visit(int[][] mat, int i, int j, int dist){
        if(i<0 || j<0 || i>=I || j>=J) return;
        if(visited[i][j]) return;
        visited[i][j]=true;
        if(mat[i][j]==0) dist=0;
        if(mat[i][j]==1) ans[i][j]=dist;
        queue.add(new Pos(i, j, dist));
        //if(mat[i][j]==0) dist=0;
        //if(mat[i][j]==1) ans[i][j]=dist;
/*        visit(mat, i-1, j, dist+1);
        visit(mat, i+1, j, dist+1);
        visit(mat, i, j-1, dist+1);
        visit(mat, i, j+1, dist+1);*/
    }
}
