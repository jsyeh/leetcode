int N;
int * visited;
int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize){
    N = isConnectedSize;
    visited = (int*)malloc(N*sizeof(int));
    for(int i=0; i<N; i++) visited[i] = 0;

    int ans = 0;
    for(int i=0; i<N; i++){
        if(visited[i]==0){
//printf("ans++\n");
            ans++;
            travel(isConnected, i);
        }
    }
    return ans;
}
void travel(int ** isConnected, int i) {
//print();
//    printf("i:%d\n", i);
    if(i<0 || i>=N) return;
    if(visited[i]==1) return;
//printf(".");
    visited[i] = 1;

    for(int j=0; j<N; j++){
//print();
        if(visited[j]==1) continue;
        if(isConnected[i][j]==1){
            travel(isConnected, j);
        }
    }
}//case 36/113: [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
void print(){
    for(int i=0; i<N; i++) printf(" %d ", visited[i]);
    printf("\n");
  
}
