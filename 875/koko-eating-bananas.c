bool canEatInTime(int* piles, int pilesSize, int speed, int h){
    int t = 0;
    for(int i=0; i<pilesSize; i++){
        if(piles[i]<=speed) t++;
        else {
            t += piles[i]/speed;
            if(piles[i]%speed>0) t+=1;
        }
    }
    if(t<=h) return true;
    else return false;
}
int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
int minEatingSpeed(int* piles, int pilesSize, int h){
    qsort(piles, pilesSize, sizeof(int), comp);

    int left = 1, right = piles[pilesSize-1];
    while(left<right){
        int mid = (left+right)/2;
        if(canEatInTime(piles, pilesSize, mid, h)){
            right = mid;
        }else{
            left = mid+1;
        }
    }
    return left;
}
