int maxDistance(int** grid, int gridSize, int* gridColSize){
    int M = gridSize, N = gridColSize[0];

    int Q[10000]={}, front=0, tail=0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==1){
                Q[tail++] = (i*100+j);
            }
        }
    }

    int di[4]={0,1,0,-1}, dj[4]={1,0,-1,0};
    int ans = 0;
    while(front<tail){
        int now = Q[front++];
        int i = now/100, j = now%100;
        int next = grid[i][j]+1;
        for(int d=0; d<4; d++){
            int ii = i+di[d], jj = j+dj[d];
            if(ii<0 || jj<0 || ii>=M || jj>=N || grid[ii][jj]!=0) continue;
            grid[ii][jj] = next;
            Q[tail++] = (ii*100+jj);
            if(next>ans) ans = next;
        }
    }
    return ans-1;
}
//case 36/38: [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
