int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int maxScoreSightseeingPair(int* values, int valuesSize){
    int ans = 0;
    int prevMax = values[0];
    //int table[valuesSize+1];//table[j]表示 value[i]...value[j-1]為止的最大值
    //最大值會慢慢變小，遇到更大的值，就會更新
    //table[0] = values[0];
    for(int i=1; i<valuesSize; i++){
        if(prevMax+values[i]-1>ans) ans = prevMax+values[i]-1;
        prevMax = max(prevMax-1, values[i]);
        //table[i] = max(table[i-1]-1, values[i]);
        //if(table[i-1]+values[i]-1>ans) ans =table[i-1]+values[i]-1;
    }
    return ans;
}
