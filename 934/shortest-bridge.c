void dfs(int** grid, int M, int N, int i, int j, int id){
    if(i<0 || j<0 || i>=M || j>=N) return;
    if(grid[i][j]==1) grid[i][j] = id;
    else return;

    dfs(grid, M, N, i+1, j, id);
    dfs(grid, M, N, i-1, j, id);
    dfs(grid, M, N, i, j+1, id);
    dfs(grid, M, N, i, j-1, id);
}

int front=0, back=0, Qn=0;
int ans = -1;
void testAndPush(int** grid, int M, int N, int i, int j, int*Qi, int*Qj, int*D, int dist){
    if(i<0 || j<0 || i>=M || j>=N) return;
//printf("Qn:%d\n", Qn);
//printf("grid[%d][%d]:%d\n", i, j, grid[i][j]);
    if(grid[i][j]==0){
        grid[i][j]=-1;//要設成visited的意思
        Qi[back]=i;
        Qj[back]=j;
        D[back]=dist;
        back++;
        Qn++;
//printf("A");
    }else if(grid[i][j]==3 && ans==-1){
//printf("B");
        ans = dist;
        return;
    }
}

int shortestBridge(int** grid, int gridSize, int* gridColSize){
    int M = gridSize, N = gridColSize[0];
    ans = -1;

    int id=2;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==1){
                dfs(grid, M, N, i, j, id++);
            }
        }
    }

//for(int i=0; i<M; i++){
//    for(int j=0; j<N; j++){
//        printf("%d", grid[i][j]);
//    }
//    printf("\n");
//}

    int Qi[M*N+1], Qj[M*N+1], D[M*N+1];
    front=0;
    back=0;
    Qn=0;
    int dist=0; //因為0,2,3都用過了，4代表走1步，5代表走2步
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(grid[i][j]==2){
//printf(".");
                Qi[back]=i;
                Qj[back]=j;
                D[back]=dist;
                back++;
                Qn++;
            }
        }
    }
//printf("Qn:%d\n", Qn);
    while(Qn>0){
        int i = Qi[front], j = Qj[front], dist = D[front];
//printf("i:%d j:%d\n", i, j);
        front++;
        Qn--;
//void testAndPush(int** grid, int M, int N, int i, int j, int*Qi, int*Qj, int back, int dist){
        testAndPush(grid, M, N, i-1,j, Qi, Qj, D, dist+1);
        testAndPush(grid, M, N, i+1,j, Qi, Qj, D, dist+1);
        testAndPush(grid, M, N, i,j-1, Qi, Qj, D, dist+1);
        testAndPush(grid, M, N, i,j+1, Qi, Qj, D, dist+1);
    }

    return ans-1;
}
