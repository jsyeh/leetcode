int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
bool canMakeArithmeticProgression(int* arr, int arrSize){
    qsort(arr, arrSize, sizeof(int), comp);
    int diff = arr[1]-arr[0];
    for(int i=1; i<arrSize; i++){
        if(arr[i]-arr[i-1]!=diff) return false;
    }
    return true;
}
