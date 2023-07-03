int max(int a, int b){
    if(a>b) return a;
    return b;
}
int deleteAndEarn(int* nums, int numsSize){
    //因為 1<= nums[i] <= 10^4, 所以可以開陣列來解
    int a[10001]={};
    int table[10002]={};//放答案
    for(int i=0; i<numsSize; i++){
        a[nums[i]]++;//統計數字出現的次數
    }

    //想重覆使用 a[i] ，但怕程式不好懂，所以再開 table[i]放答案
    table[0] = a[0];//取用0
    table[1] = a[1];//取用1
    table[2] = table[0] + 2*a[2];//要避開 table[2-1] 及 table[2+1]
    for(int i=3; i<10001; i++){
        table[i] = i*a[i] + max(table[i-2], table[i-3]);
    }
    return max(table[10000], table[9999]);
}
//case 50/51: 有一大堆數字，最後加出來的結果 61252683 vs. 61262682 差了 9999 因為答案可能是 table[10000] vs. table[9999]
