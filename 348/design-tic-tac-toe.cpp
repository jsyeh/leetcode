class TicTacToe {
public:
    int n;
    int cell[100][100];//因為n最大是100
    TicTacToe(int N) {
        n = N;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cell[i][j] = 0; //0: no, 1: player1, 2: player2
            }
        }
    }
    
    int move(int row, int col, int player) {
        cell[row][col] = player;//先把棋子下好

        int bad=0;
        for(int i=0; i<n; i++){
            if(cell[i][col]!=player) {
                bad=1;
                break;
            }
        }
        if(bad==0) return player;

        bad=0;
        for(int j=0; j<n; j++){
            if(cell[row][j]!=player) {
                bad=1;
                break;
            }
        }
        if(bad==0) return player;

        if(row!=col && n-1-row!=col) return 0;;//如果不是對角線，就結束了
        
        bad=0;
        for(int i=0; i<n; i++){
            if(cell[i][i]!=player){
                bad=1;
                break;
            }
        }
        if(bad==0) return player;

        bad=0;
        for(int i=0; i<n; i++){
            if(cell[i][n-1-i]!=player){
                bad=1;
                break;
            }
        }
        if(bad==0) return player;
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
