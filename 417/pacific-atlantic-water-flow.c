/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
}
 */
void show(bool** grid, int M, int N){
    printf("showing\n");
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("showed\n");
}
void showInt(int** grid, int M, int N){
    printf("showingInt\n");
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("showed\n");
}
void testAndPush(int** heights, bool** visited, int i, int j, int M, int N, int**map, int prev, int* qi, int* qj, int *ptail){
    if(i<0 || j<0 || i>=M || j>=N) return;
//printf("ii:%d jj:%d\n", i, j);
    if(!visited[i][j] && heights[i][j]>=prev) {
        qi[*ptail] = i;
        qj[*ptail] = j;
        (*ptail)++;
//printf("*ptail:%d\n", *ptail);
        map[i][j] = 1;
        visited[i][j] = true;
    }
}
int** pacificAtlantic(int** heights, int heightsSize, int* heightsColSize, int* returnSize, int** returnColumnSizes){
    int M = heightsSize, N = heightsColSize[0];

    //int map1[M][N], map2[M][N];
    int ** map1 = (int**)malloc(sizeof(int*)*M);
    int ** map2 = (int**)malloc(sizeof(int*)*M);
    bool ** visited = (bool**)malloc(sizeof(bool*)*M);
    for(int i=0; i<M; i++){
        map1[i] = (int*)malloc(sizeof(int)*N);
        map2[i] = (int*)malloc(sizeof(int)*N);
        visited[i] = (bool*)malloc(sizeof(bool)*N);
        for(int j=0; j<N; j++){
            map1[i][j]=0;
            map2[i][j]=0;
            visited[i][j]=false;
//printf("%d ", visited[i][j]);
        }
//printf("visited\n");
    }
//show(visited, M, N);
    int qi[M*N*10], qj[M*N*10], head=0, tail=0;
    //先計算Pacific Ocean
    for(int i=0; i<M; i++){ //標示上緣
        for(int j=0; j<N; j++) map1[i][j] = 0; //先清為0 (1則為標示)

        qi[tail] = i;
        qj[tail++] = 0;
        //map1[i][0] = 1;
        //visited[i][0] = true;
    }
    for(int j=1; j<N; j++){//標示左緣，從1開始，是因0,0在前面已塞過
        qi[tail] = 0;
        qj[tail++] = j;
        //map1[0][j] = 1;
        //visited[0][j] = true;
    }
    while(head<tail){//開始逐格拆解
        int i = qi[head], j = qj[head++];
//printf("i:%d j:%d\n", i, j);
        map1[i][j] = 1;
        visited[i][j] = true;
        int now = heights[i][j];
        testAndPush(heights, visited, i+1, j, M, N, map1, now, qi, qj, &tail);
        testAndPush(heights, visited, i-1, j, M, N, map1, now, qi, qj, &tail);
        testAndPush(heights, visited, i, j+1, M, N, map1, now, qi, qj, &tail);
        testAndPush(heights, visited, i, j-1, M, N, map1, now, qi, qj, &tail);
    }
//show(visited, M, N);
//showInt(map1, M, N);
    for(int i=0; i<M; i++){ //將 visited[i][j] 清空，重來一次
        for(int j=0; j<N; j++){
            visited[i][j] = false;
        }
    }
    //接下來計算 Atlantic Ocean
    head = 0;
    tail = 0;//將Queue清空
    for(int i=0; i<M; i++){//標示右緣
        qi[tail] = i;
        qj[tail++] = N-1;
        //map2[i][N-1] = 1;
        //visited[i][N-1] = true;
    }
    for(int j=0; j<N-1; j++){//標示下緣，右下角重覆，所以跳掉
        qi[tail] = M-1;
        qj[tail++] = j;
        //map2[M-1][j] = 1;
        //visited[M-1][j] = true;
    }
    while(head<tail){
        int i = qi[head], j = qj[head++];
        map2[i][j] = 1;
        visited[i][j] = true;
        int now = heights[i][j];
        testAndPush(heights, visited, i+1, j, M, N, map2, now, qi, qj, &tail);
        testAndPush(heights, visited, i-1, j, M, N, map2, now, qi, qj, &tail);
        testAndPush(heights, visited, i, j+1, M, N, map2, now, qi, qj, &tail);
        testAndPush(heights, visited, i, j-1, M, N, map2, now, qi, qj, &tail);    
    }
//show(visited, M, N);
//showInt(map2, M, N);
    //最後，計算 map1[i][j] 及 map2[i][j] 交集的地方，算答案
    //先算出 ans 的 len 之後，再準備好 memory
    int len = 0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(map1[i][j]==1 && map2[i][j]==1) len++;
        }
    }
    int** ans = (int**)malloc(sizeof(int*)*len);
    *returnColumnSizes = (int*)malloc(sizeof(int)*len);
    *returnSize = len;
//printf("len:%d\n", len);
    len = 0;
    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            if(map1[i][j]==1 && map2[i][j]==1){
                ans[len] = (int*)malloc(sizeof(int)*2);
                ans[len][0] = i;
                ans[len][1] = j;
                (*returnColumnSizes)[len] = 2;
                len++;
            }
        }
    }
    return ans;
}
//case 71/113: [[2,1],[1,2]]
//如果之前 visited過但不及格，應該要再給第2次機會，所以不能標注 visited
//問題應該只是漏了標示右下角是Atlantic Ocean
