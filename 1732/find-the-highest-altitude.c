int largestAltitude(int* gain, int gainSize){
    int now = 0, max=0;
    for(int i=0; i<gainSize; i++){
        now += gain[i];
        if(now>max) max = now;
    }
    return max;
}
