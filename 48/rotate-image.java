class Solution {
    public void rotate(int[][] matrix) {
        int N = matrix.length;
        int[][] temp = new int[N][N];
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                temp[i][j] = matrix[N-1-j][i];
            }
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                matrix[i][j] = temp[i][j];
            }
        }
    }
}
