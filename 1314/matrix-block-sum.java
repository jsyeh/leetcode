//100*100 * 100*100 會超過時間，所以不能逐一全部加
//可改用 integral matrix 也就是 sum[i][j] 會把 0,0 .. i,j 的左上矩陣
class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        int M = mat.length, N = mat[0].length;
        int[][] sum = new int[M][N];
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                sum[i][j] = mat[i][j];
                if(i-1>=0) sum[i][j] += sum[i-1][j];
                if(j-1>=0) sum[i][j] += sum[i][j-1];
                if(i-1>=0 && j-1>=0) sum[i][j] -= sum[i-1][j-1];
                //System.out.print(sum[i][j] + " ");
            }
            //System.out.println();
        }

        int[][] ans = new int[M][N];
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                int ii1 = i-k-1, ii2 = i+k;
                int jj1 = j-k-1, jj2 = j+k;
// ans[i][j] = sum[ii2][jj2] - sum[ii1][jj2] - sum[ii2][jj1] + sum[ii1][jj1]
                if(ii2>=M) ii2 = M-1;
                if(jj2>=N) jj2 = N-1;
                ans[i][j] = sum[ii2][jj2];
                if(ii1>=0) ans[i][j] -= sum[ii1][jj2];
                if(jj1>=0) ans[i][j] -= sum[ii2][jj1];
                if(ii1>=0 && jj1>=0) ans[i][j] += sum[ii1][jj1];
            }
        }
        return ans;
    }
}
