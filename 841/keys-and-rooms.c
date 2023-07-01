bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize){
    bool visited[roomsSize];
    for(int i=0; i<roomsSize; i++) visited[i] = false;

    int Q[roomsSize], head = 0, tail = 1;
    Q[0] = 0;
    visited[0] = true;

    int openN = 1;
    while(head<tail){
        int i = Q[head++];
        for(int j=0; j<roomsColSize[i]; j++){
            int k = rooms[i][j];
            if(visited[k]) continue;
            visited[k] = true;
            Q[tail++] = k;
            openN++;
//printf("key:%d\n", k);
        }
    }
//printf("openN:%d\n", openN);
    if(openN==roomsSize) return true;
    else return false;
}
