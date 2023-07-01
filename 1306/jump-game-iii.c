bool canReach(int* arr, int arrSize, int start){
    int visited[50000]={};
    int Q[50000]={}, head=0, tail=1;
    Q[0] = start;
    visited[start]=1;

    while(head<tail){
        int i = Q[head++];
        if(arr[i]==0) return true;
        if(i-arr[i]>=0 && visited[i-arr[i]]==0){
            Q[tail++] = i-arr[i];
            visited[i-arr[i]]=1;
        }
        if(i+arr[i]<arrSize && visited[i+arr[i]]==0){
            Q[tail++] = i+arr[i];
            visited[i+arr[i]]=1;
        }
    }
    return false;
}
