char * tictactoe(int** moves, int movesSize, int* movesColSize){
    int table[3][3]={};
    int ans = 0; //no answer
    for(int i=0; i<movesSize; i++){
        int x = moves[i][0], y = moves[i][1];
        if(i%2==0) table[x][y] = 1;
        else table[x][y] = 2;

        for(int t=1; t<=2; t++){
            if(table[0][0]==t && table[0][1]==t && table[0][2]==t) ans = t;
            if(table[1][0]==t && table[1][1]==t && table[1][2]==t) ans = t;
            if(table[2][0]==t && table[2][1]==t && table[2][2]==t) ans = t;

            if(table[0][0]==t && table[1][0]==t && table[2][0]==t) ans = t;
            if(table[0][1]==t && table[1][1]==t && table[2][1]==t) ans = t;
            if(table[0][2]==t && table[1][2]==t && table[2][2]==t) ans = t;

            if(table[0][0]==t && table[1][1]==t && table[2][2]==t) ans = t;
            if(table[0][2]==t && table[1][1]==t && table[2][0]==t) ans = t;
        }

        if(ans==1) return "A";
        if(ans==2) return "B";
    }

    if(movesSize==9)return "Draw";
    else return "Pending";
}
