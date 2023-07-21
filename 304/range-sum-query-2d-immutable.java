class NumMatrix {
    int[][] sum;
    int M, N;
    public NumMatrix(int[][] matrix) {
        M = matrix.length;
        N = matrix[0].length;
        sum = new int[M][N];
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                sum[i][j] = matrix[i][j];
                if(i-1>=0) sum[i][j] += sum[i-1][j];
                if(j-1>=0) sum[i][j] += sum[i][j-1];
                if(i-1>=0 && j-1>=0) sum[i][j] -= sum[i-1][j-1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(row2>=M) row2 = M-1;
        if(col2>=N) col2 = N-1;
        int ans = sum[row2][col2];

        row1--;//不包含
        col1--;//不包含
        if(row1>=0) ans -= sum[row1][col2];
        if(col1>=0) ans -= sum[row2][col1];
        if(row1>=0 && col1>=0) ans += sum[row1][col1];
        return ans;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
