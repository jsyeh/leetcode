class Solution {
    LinkedList <Pos> queue;
    int I, J;
    boolean border;
    boolean [][] visited;
    public int closedIsland(int[][] grid) {
        //0:55 start
        I = grid.length;
        J = grid[0].length;
        visited = new boolean[I][J];
        int ans=0;
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
//05:00累了,暫停 遇到邊界的island不能計算
                if(!visited[i][j] && grid[i][j]==0){
                    queue = new LinkedList<Pos>();
                    border=false;
                    testAndVisitPush(grid, i, j);
                    while(queue.size()>0){
//System.out.print(".");
                        Pos now = queue.pop();
//System.out.print(now.i + " " + now.j);
                        visited[now.i][now.j]=true;
                        testAndVisitPush(grid, now.i-1, now.j);
                        testAndVisitPush(grid, now.i+1, now.j);
                        testAndVisitPush(grid, now.i, now.j-1);
                        testAndVisitPush(grid, now.i, now.j+1);
                    }
                    if(border==false) ans++;
//System.out.println(ans);
                }
            }
        }
        return ans;
    }
    void testAndVisitPush(int[][] grid, int i, int j) {
        if(i<0 || i>=I || j<0 || j>=J) return;
        if(visited[i][j]) return;
        if(grid[i][j]==0) {
            if(i==0 || j==0 || i==I-1 || j==J-1) border=true;
            queue.push(new Pos(i,j));
        }
    }
}
class Pos{
    public int i, j;
    Pos(int _i, int _j){
        i = _i;
        j = _j;
    }
}
