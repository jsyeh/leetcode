class Solution {
    public boolean isValidSudoku(char[][] board) {
        //check rows
        for(int i=0; i<9; i++){
            int [] a = new int[10];
            for(int j=0; j<9; j++){
                if(board[i][j]=='.') continue;
                char c = board[i][j];
                if(a[c-'0']==0){
                    a[c-'0']++;
                }else{
                    return false;
                }
            }
        }
        //check cols
        for(int j=0; j<9; j++){
            int [] a = new int[10];
            for(int i=0; i<9; i++){
                if(board[i][j]=='.') continue;
                char c = board[i][j];
                if(a[c-'0']==0){
                    a[c-'0']++;
                }else{
                    return false;
                }
            }
        }
        for(int row=0; row<3; row++){
            for(int col=0; col<3; col++){
                int [] a = new int[10];
                for(int i=0; i<3; i++){
                    for(int j=0; j<3; j++){
                        if(board[row*3+i][col*3+j]=='.') continue;
                        char c = board[row*3+i][col*3+j];
                        if(a[c-'0']==0){
                            a[c-'0']++;
                        }else{
                            return false;
                        }

                    }
                }
            }
        }
        return true;
    }
}
