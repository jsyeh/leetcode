int min(int a, int b){
    if(a<b) return a;
    else return b;
}
int comp(const void *p1, const void *p2){
    return *(int*)p2 - *(int*)p1;
}
int leastInterval(char* tasks, int tasksSize, int n){
    int H[26]={};
    for(int i=0; i<tasksSize; i++){
        H[tasks[i]-'A']++;
    }
    qsort(H, 26, sizeof(int), comp);
    int idle_time = (H[0]-1)*n;

    for(int i=1; i<26; i++){
        idle_time -= min(H[0]-1, H[i]);
    }
    if(idle_time<0) idle_time=0;
    return tasksSize + idle_time;
}
