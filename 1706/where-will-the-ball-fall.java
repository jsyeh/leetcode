class Solution {
    public int[] findBall(int[][] grid) {
        int M=grid.length, N=grid[0].length;//N也決定有幾個球
        int [] ans = new int[N];
        for(int i=0; i<N; i++) ans[i] = i;

        for(int i=0; i<N; i++) { //有N顆球要做實驗
            for(int k=0; k<M; k++){
                int prev=ans[i];
                if(grid[k][prev]==1){//往右
                    if(prev==N-1 || grid[k][prev+1]==-1){//卡住右壁 || 右邊卡住
                        ans[i] = -1;
                        break;//離開模擬的迴圈
                    }
                }
                if(grid[k][prev]==-1){//往左
                    if(prev==0 || grid[k][prev-1]==1){//卡住左壁 || 左邊卡住
                        ans[i] = -1;
                        break;//離開模擬的迴圈
                    }
                }
                ans[i] += grid[k][prev];//就走吧
            }
        }
        return ans;
    }
}
