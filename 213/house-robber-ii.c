int max(int a, int b){
    return (a>b)? a : b;
}
int max4(int a, int b, int c, int d){
    return max(max(a,b), max(c,d));
}
int max5(int a, int b, int c, int d, int e){
    return max(max(max(a,b), max(c,d)), e);
}
int rob(int* nums, int numsSize){
    if(numsSize==0) return 0;
    if(numsSize==1) return nums[0];
    if(numsSize==2) return max(nums[0], nums[1]);
    if(numsSize==3) return max4(nums[0], nums[1], nums[2], 0);

    //int table[numsSize+1];//table[i] 表示 第i個如果有取用,能賺到的最大值
    //頭尾的話,要怎麼處理? 可以考慮: 第0個不取用 vs. 第0個要用
    int table0[numsSize+1];//nums[0]要使用
    int table1[numsSize+1];//nums[1]要使用
    int table2[numsSize+1];//nums[2]要使用

    table0[0] = nums[0];
    table0[1] = 0;
    table0[2] = nums[2] + nums[0];

    table1[0] = 0;
    table1[1] = nums[1];
    table1[2] = 0;

    table2[0] = 0;
    table2[1] = 0;
    table2[2] = nums[2];

    for(int i=3; i<numsSize; i++){
        table0[i] = max(table0[i-2], table0[i-3]) + nums[i];
        table1[i] = max(table1[i-2], table1[i-3]) + nums[i];
        table2[i] = max(table2[i-2], table2[i-3]) + nums[i];
    }

    for(int i=0; i<numsSize; i++){
        printf("%d ", table0[i]);
    }
    printf("table0[i]\n");
    for(int i=0; i<numsSize; i++){
        printf("%d ", table1[i]);
    }
    printf("table1[i]\n");
    for(int i=0; i<numsSize; i++){
        printf("%d ", table2[i]);
    }
    printf("table2[i]\n");

    if(numsSize==3) return max5(table0[numsSize-2], 0, table1[numsSize-1], table1[numsSize-2], table2[numsSize-1]);
    else return max5(table0[numsSize-2], table0[numsSize-3], table1[numsSize-1], table1[numsSize-2], table2[numsSize-1]);
    

    return 0;
}//case: [0,0,99,0,99]
//case 74/75: [1,2,3,4,5,1,2,3,4,5]
