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
    Stack<Pos> stack = new Stack<Pos>();
    public void solve(char[][] board) {
        M = board.length;
        N = board[0].length;
        visited = new boolean[M][N];
        //先從boundry下手，標示成 'B'
        //最後把 non-'B' 標成'X', 再把 'B' 標成 'O'
        for(int i=0; i<M; i++){
            testAndAdd(board, i, 0);
            testAndAdd(board, i, N-1);
        }
        for(int j=0; j<N; j++){
            testAndAdd(board, 0, j);
            testAndAdd(board, M-1, j);
        }
        while(stack.size()>0) {
            Pos now = stack.pop();
            board[now.i][now.j] = 'B';
            testAndAdd(board, now.i-1, now.j);
            testAndAdd(board, now.i+1, now.j);
            testAndAdd(board, now.i, now.j-1);
            testAndAdd(board, now.i, now.j+1);
        }

        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if(board[i][j]!='B') board[i][j] = 'X';
                else board[i][j] = 'O';
            }
        }
    }
    void testAndAdd(char[][] board, int i, int j) {
        if(i<0 || j<0 || i>=M || j>=N) return;
        if(visited[i][j]) return;
        visited[i][j] = true;

        if(board[i][j]=='X' || board[i][j]=='B') return;
        stack.add(new Pos(i,j));//board[i][j]=='O';
    }
}
