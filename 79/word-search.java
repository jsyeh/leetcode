class Solution {
    boolean [][] visited;
    int M, N;
    public boolean exist(char[][] board, String word) {
        M=board.length;
        N=board[0].length;
        visited = new boolean[M][N];
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(trace(board, i, j, word, 0)) return true;
            }
        }
        return false;
    }
    boolean trace(char[][] board, int i, int j, String word, int start) {
        if(i<0 || j<0 || i>=M || j>=N) return false;
        if(visited[i][j]) return false;
        if(board[i][j]==word.charAt(start)){
            if(start == word.length()-1) return true;
            visited[i][j] = true;
            if(trace(board, i+1, j, word, start+1)) return true;
            if(trace(board, i-1, j, word, start+1)) return true;
            if(trace(board, i, j+1, word, start+1)) return true;
            if(trace(board, i, j-1, word, start+1)) return true;

            visited[i][j] = false;
        }
        return false;
    }
}
