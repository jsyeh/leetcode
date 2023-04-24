void addStone(int* stones, int one, int stonesSize){
    stones[stonesSize]=one;
}
int findRemoveMax(int* stones, int stonesSize){
    int maxI = 0;
    for(int i=1; i<stonesSize; i++){
        if(stones[i]>stones[maxI]){
            maxI = i;
        }
    }
    int ans = stones[maxI];
    stones[maxI] = stones[stonesSize-1];
    return ans;
}
int lastStoneWeight(int* stones, int stonesSize){
    while(stonesSize>1){
        int a = findRemoveMax(stones, stonesSize--);
        int b = findRemoveMax(stones, stonesSize--);
        if(a-b>0){
            addStone(stones, a-b, stonesSize++);
        }
    }
    if(stonesSize==1) return stones[0];
    else return 0;
}
