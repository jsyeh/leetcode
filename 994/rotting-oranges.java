class Pos {
    int i, j, minute;
    Pos(int _i, int _j, int _minute) {
        i = _i;
        j = _j;
        minute = _minute;
    }
}
class Solution {
    int I, J;
    LinkedList<Pos> rotten = new LinkedList<Pos>();
    boolean [][] visited;
    public int orangesRotting(int[][] grid) {
        I = grid.length;
        J = grid[0].length;
        visited = new boolean[I][J];
for(int i=0; i<I; i++){
    for(int j=0; j<J; j++){
        System.out.print(grid[i][j]);
    }
    System.out.println();
}
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
                if(grid[i][j]==2) visit(grid, i,j,0);
            }
        }
        int ans = 0;
        while(rotten.size()>0){
            //Pos now = rotten.pop();
            Pos now = rotten.poll();
            if(now.minute>ans) ans = now.minute;
System.out.println(now.i + " " + now.j + " " + now.minute);
            visit(grid, now.i+1, now.j, now.minute+1);
            visit(grid, now.i-1, now.j, now.minute+1);
            visit(grid, now.i, now.j+1, now.minute+1);
            visit(grid, now.i, now.j-1, now.minute+1);
        }
        for(int i=0; i<I; i++){
            for(int j=0; j<J; j++){
System.out.print(grid[i][j]);
                if(grid[i][j]==1) ans = -1;
            }
System.out.println();
        }
        return ans;
    }
    void visit(int[][] grid, int i, int j, int minute) {
        if(i<0 || j<0 || i>=I || j>=J) return;
        if(visited[i][j]) return;
System.out.println("visiting " + i + j + minute);
        visited[i][j]=true;

        if(grid[i][j]==0) return;
        if(grid[i][j]==1 || grid[i][j]==2){
            grid[i][j]=2;
            //rotten.push(new Pos(i,j,minute));
            rotten.offer(new Pos(i,j,minute));
        }
    }//奇怪，為什麼 LinkedList 的 push pop 卻變成 stack 的行為？
}
