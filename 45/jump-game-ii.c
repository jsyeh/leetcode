int min(int a, int b){
    if(a<b) return a;
    else return b;
}
int jump(int* nums, int numsSize){
    int table[numsSize+1];
    for(int i=0; i<numsSize; i++) table[i]=0;
    table[0]=0;
    for(int i=0; i<numsSize; i++){
        for(int k=i+1; k<=i+nums[i] && k<numsSize; k++) {
            if(table[k]==0) table[k] = table[i]+1;
            else table[k] = min(table[k], table[i]+1);
        }
    }
    return table[numsSize-1];
}//case 42/109: [4,1,1,3,1,1,1]
