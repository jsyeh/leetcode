int uniquePaths(int m, int n){
    int table[101][101];
    for(int j=0; j<n; j++) table[0][j] = 1;

    for(int i=1; i<m; i++){
        table[i][0] = table[i-1][0];
        for(int j=1; j<n; j++){
            table[i][j] = table[i-1][j] + table[i][j-1];
        }
    }
    return table[m-1][n-1];
}
