class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(r==mat.length && c==mat[0].length) return mat;
        if(mat.length*mat[0].length != r*c) return mat;

        int [][] ans = new int[r][c];
        int id=0;
        for(int i=0; i<mat.length; i++){
            for(int j=0; j<mat[0].length; j++){
                int ii = id/c, jj = id%c;
                ans[ii][jj] = mat[i][j];
                id++;
            }
        }
        return ans;
    }
}
