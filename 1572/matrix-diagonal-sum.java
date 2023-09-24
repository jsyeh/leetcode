class Solution {
    public int diagonalSum(int[][] mat) {
        int N = mat.length;
        int sum = 0;
        for(int i=0; i<N; i++){
            sum += mat[i][i];
            sum += mat[N-1-i][i];
        }
        if(N%2==1) sum -= mat[N/2][N/2];

        return sum;
    }
}
