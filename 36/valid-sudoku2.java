class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0; i<9; i++){
            int []H = new int[10];
            for(int j=0; j<9; j++){
                if(board[i][j]=='.') continue;
                int now = board[i][j]-'0';
                if(H[now]==0) H[now]++;
                else return false;
            }
        }
        for(int j=0; j<9; j++){
            int []H = new int[10];
            for(int i=0; i<9; i++){
                if(board[i][j]=='.') continue;
                int now = board[i][j]-'0';
                if(H[now]==0) H[now]++;
                else return false;
            }
        }
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                int []H = new int[10];
                for(int ii=i*3; ii<i*3+3; ii++){
                    for(int jj=j*3; jj<j*3+3; jj++){
                        if(board[ii][jj]=='.') continue;
                        int now = board[ii][jj]-'0';
                        if(H[now]==0) H[now]++;
                        else return false;
                    }
                }
            }
        }
        return true;
    }
}
