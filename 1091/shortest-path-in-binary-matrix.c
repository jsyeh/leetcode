int shortestPathBinaryMatrix(int** grid, int gridSize, int* gridColSize){
    if(grid[0][0]!=0) return -1;

    int M = gridSize, N = gridColSize[0];
    int Qi[M*N+1], Qj[M*N+1];
    int front=0, back=0, Qn=0;

    grid[0][0] = 1;
    Qi[back]=0;
    Qj[back]=0;
    back++;
    Qn++;
    while(Qn>0){
        int i = Qi[front], j = Qj[front], now = grid[i][j];
        if(i==M-1 && j==N-1) return now;

        front++;
        Qn--;
        if(i+1<M && grid[i+1][j]==0){
            grid[i+1][j] = now+1;
            Qi[back]=i+1;
            Qj[back]=j;
            back++;
            Qn++;
        }
        if(i-1>=0 && grid[i-1][j]==0){
            grid[i-1][j] = now+1;
            Qi[back]=i-1;
            Qj[back]=j;
            back++;
            Qn++;
        }
        if(j+1<N && grid[i][j+1]==0){
            grid[i][j+1] = now+1;
            Qi[back]=i;
            Qj[back]=j+1;
            back++;
            Qn++;
        }
        if(j-1>=0 && grid[i][j-1]==0){
            grid[i][j-1] = now+1;
            Qi[back]=i;
            Qj[back]=j-1;
            back++;
            Qn++;
        }
        if(i+1<M && j+1<N && grid[i+1][j+1]==0){
            grid[i+1][j+1] = now+1;
            Qi[back]=i+1;
            Qj[back]=j+1;
            back++;
            Qn++;
        }
        if(i+1<M && j-1>=0 && grid[i+1][j-1]==0){
            grid[i+1][j-1] = now+1;
            Qi[back]=i+1;
            Qj[back]=j-1;
            back++;
            Qn++;
        }
        if(i-1>=0 && j+1<N && grid[i-1][j+1]==0){
            grid[i-1][j+1] = now+1;
            Qi[back]=i-1;
            Qj[back]=j+1;
            back++;
            Qn++;
        }
        if(i-1>=0 && j-1>=0 && grid[i-1][j-1]==0){
            grid[i-1][j-1] = now+1;
            Qi[back]=i-1;
            Qj[back]=j-1;
            back++;
            Qn++;
        }
    }
    return -1;
}
//case 3/90: [[0,0,0],[1,1,0],[1,1,1]]
