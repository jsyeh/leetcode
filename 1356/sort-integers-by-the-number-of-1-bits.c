/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int bits(int n){
    int ans = 0;
    while(n>0){
        if(n%2==1) ans++;
        n = n / 2;
    }
    return ans;
}
int comp(const void *p1, const void *p2){
    int a = *(int*)p1, b = *(int*)p2;
    int bit1 = bits(a), bit2 = bits(b);
    if(bit1<bit2) return -1;
    if(bit1>bit2) return +1;
    return a-b;
}
int* sortByBits(int* arr, int arrSize, int* returnSize){
    *returnSize = arrSize;
    qsort(arr, arrSize, sizeof(int), comp);
    return arr;
}
