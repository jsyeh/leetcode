char * tictactoe(int** moves, int movesSize, int* movesColSize){
    int table[3][3]={};
    int ans = 0; //no answer
    for(int i=0; i<movesSize; i++){
        int x = moves[i][0], y = moves[i][1];
        if(i%2==0) table[x][y] = 1;
        else table[x][y] = 2;

        if(table[0][0]==1 && table[0][1]==1 && table[0][2]==1) ans = 1;
        if(table[1][0]==1 && table[1][1]==1 && table[1][2]==1) ans = 1;
        if(table[2][0]==1 && table[2][1]==1 && table[2][2]==1) ans = 1;

        if(table[0][0]==1 && table[1][0]==1 && table[2][0]==1) ans = 1;
        if(table[0][1]==1 && table[1][1]==1 && table[2][1]==1) ans = 1;
        if(table[0][2]==1 && table[1][2]==1 && table[2][2]==1) ans = 1;

        if(table[0][0]==1 && table[1][1]==1 && table[2][2]==1) ans = 1;
        if(table[0][2]==1 && table[1][1]==1 && table[2][0]==1) ans = 1;

        if(table[0][0]==2 && table[0][1]==2 && table[0][2]==2) ans = 2;
        if(table[1][0]==2 && table[1][1]==2 && table[1][2]==2) ans = 2;
        if(table[2][0]==2 && table[2][1]==2 && table[2][2]==2) ans = 2;

        if(table[0][0]==2 && table[1][0]==2 && table[2][0]==2) ans = 2;
        if(table[0][1]==2 && table[1][1]==2 && table[2][1]==2) ans = 2;
        if(table[0][2]==2 && table[1][2]==2 && table[2][2]==2) ans = 2;

        if(table[0][0]==2 && table[1][1]==2 && table[2][2]==2) ans = 2;
        if(table[0][2]==2 && table[1][1]==2 && table[2][0]==2) ans = 2;

        if(ans==1) return "A";
        if(ans==2) return "B";
    }

    if(movesSize==9)return "Draw";
    else return "Pending";
}
