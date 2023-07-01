void show(int** grid, int N){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void testAndPush(int** grid, int N, int i, int j, int step, int** visited, int* Qi, int* Qj, int* Qstep, int* ptail){
    if(i<0 || j<0 || i>=N || j>=N) return;
    if(visited[i][j]==1 || grid[i][j]!=0) return;

    visited[i][j] = 1;
    Qi[*ptail] = i;
    Qj[*ptail] = j;
    Qstep[*ptail] = step + 1;
    (*ptail)++;
}
int shortestPathBinaryMatrix(int** grid, int gridSize, int* gridColSize){
    if(grid[0][0]==1) return -1;

    int N = gridSize;
    int** visited = (int**)malloc(sizeof(int*)*N);
    for(int i=0; i<N; i++){
        visited[i] = (int*)malloc(sizeof(int)*N);
        for(int j=0; j<N; j++) visited[i][j] = 0;
    }

    int Qi[N*N+1], Qj[N*N+1], Qstep[N*N+1], head = 0, tail = 1;
    Qi[0] = 0;
    Qj[0] = 0;
    Qstep[0] = 1;
    visited[0][0] = 1;
//show(grid, N);
    while(head<tail){
        int i = Qi[head], j = Qj[head], step = Qstep[head++];
        if(i==N-1 && j==N-1) return step;
        testAndPush(grid, N, i-1, j-1, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i-1, j, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i-1, j+1, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i, j-1, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i, j+1, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i+1, j-1, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i+1, j, step, visited, Qi, Qj, Qstep, &tail);
        testAndPush(grid, N, i+1, j+1, step, visited, Qi, Qj, Qstep, &tail);
    }
    return -1;
}
