void testAndPush(char** maze, int M, int N, int i, int j, int step, int* Qi, int* Qj, int* Qstep, int *ptail){
    if(i<0 || j<0 || i>=M || j>=N) return;
//printf("%c", maze[i][j]);
    if(maze[i][j]!='.') return;

    maze[i][j] = 'v';//visted
    Qi[*ptail] = i;
    Qj[*ptail] = j;
    Qstep[*ptail] = step + 1;
    (*ptail)++;
//printf("i:%d j:%d\n", i, j);
}

int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize){
    int M = mazeSize, N = mazeColSize[0];

    int Qi[M*N+1], Qj[M*N+1], Qstep[M*N+1], head = 0, tail = 1;
    int ei = Qi[0] = entrance[0];
    int ej = Qj[0] = entrance[1];
    Qstep[0] = 0;
    maze[ei][ej] = '@';//entrance, 因為 entrance 不能是 exit 所以要避開

    while(head<tail){
        int i = Qi[head], j = Qj[head], step = Qstep[head++];
        if((i==0 || j==0 || i==M-1 || j==N-1)&&maze[i][j]!='@') return step;
        //因為 entrance 不能是 exit 所以要避開

        testAndPush(maze, M, N, i+1, j, step, Qi, Qj, Qstep, &tail);
        testAndPush(maze, M, N, i-1, j, step, Qi, Qj, Qstep, &tail);
        testAndPush(maze, M, N, i, j+1, step, Qi, Qj, Qstep, &tail);
        testAndPush(maze, M, N, i, j-1, step, Qi, Qj, Qstep, &tail);
    }
    return -1;
}
