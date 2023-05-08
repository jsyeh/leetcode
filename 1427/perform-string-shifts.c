char * stringShift(char * s, int** shift, int shiftSize, int* shiftColSize){
    int N = strlen(s);

    int now = 0;
    for(int i=0; i<shiftSize; i++){
        if(shift[i][0]==0) now -= shift[i][1];
        else now += shift[i][1];
    }
    now = ((now%N)+N)%N;
//printf("%d\n", now);
    char temp[N*2];
    for(int i=0; i<N; i++){
        temp[i] = s[i];
        temp[i+N] = s[i];
    }
    for(int i=0; i<N; i++){
        s[i] = temp[i+N-now];
    }
    s[N] = 0;
    return s;
}
