//如果模擬，8^100 太多可能性，所以想到要用DP
//走k步 就要模擬k次。每固格子要依序乘上機率，
int dx[] = { 2, 1,-1,-2, -2,-1, 1, 2};
int dy[] = { 1, 2, 2, 1, -1,-2,-2,-1};
double table[101][25][25] = {}; //table[k][r][c] 表示在走了k步後，還在棋盤上的機率
//小心，在C語言裡，global變數會被共用，所以要手動將table[k][r][c]清為0
double find(int n, int k, int r, int c){
    if(r<0 || c<0 || r>=n || c>=n) return 0;//超過範圍，不是我們要的，棋盤上的機率為0
    //find()函式，會把k倒數計算，而k減為0還在棋盤上，便是我們要的機率
    //而如果走到外面，就算中斷了
    if(k==0) return 1; //走到最後一步，機率為1 (還在棋盤上，還在棋盤上的機率為1)

    //利用 table 記錄答案，讓 DP 可省下重覆計算的時間
    if(table[k][r][c]!=0) return table[k][r][c]; //有走過的話，直接回傳答案

    double ans = 0;
    for(int i=0; i<8; i++){
        ans += 0.125 * find(n, k-1, r+dy[i], c+dx[i]);
        //8個方向，每個方向的機率平等，1.0/8 ＝0.125
    }
    table[k][r][c] = ans;
    return ans;
}
double knightProbability(int n, int k, int row, int column){
    for(int kk=0; kk<=k; kk++){
        for(int i=0; i<n;i++){
            for(int j=0; j<n; j++){
                table[kk][i][j] = 0; 
            }
        }//在C語言裡，global變數會被共用，所以要手動將table[k][r][c]清為0
    }

    return find(n, k, row, column); //一開始的位置在 row, column
    //find()函式，會把k倒數計算，而k減為0還在棋盤上，便是我們要的機率
    //而如果走到外面，就算中斷了
}
//case 12/22: 10 13 5 3
