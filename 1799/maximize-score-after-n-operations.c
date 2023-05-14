int gcd(int a, int b){
    if(a==0) return b;
    if(b==0) return a;
    return gcd(b, a%b);
}
int visiting(int* nums, int numsSize, int table[8][1<<14], int level, int mask){
    //針對還沒有 visited 的數字，繼續進行計算
    if(2*level>numsSize) return 0; //第n層計算，如果剛好數字用完，就結束
    if(table[level][mask]!=0) return table[level][mask];

    for(int i=0; i<numsSize; i++){
        for(int j=i+1; j<numsSize; j++){
            int newMask = (1<<i) | (1<<j);
            if((mask & newMask)==0){ //這個i,j組合，之前沒用過
                int temp = level*gcd(nums[i],nums[j]) + visiting(nums, numsSize, table, level+1, mask|newMask);
                if(temp > table[level][mask]) table[level][mask] = temp;
            }
        }
    }
    return table[level][mask];
}
int maxScore(int* nums, int numsSize){
    //題目超難：每次挑2個數字， i*gcd(a,b)
    //最多是14個數字，所以挑7次/算7層
    //排列組合，可能次數：14*13/2+...+2*1/2 最多有84組合,但相同組合卻可能有不同的值，需要用 DP來解

    int table[8][1<<14]={}; //table[i][mask] 表示第i層，如果mask的挑法，可以找到最好的結果
    int ans = 0, mask=0; //bit mask,用來了解「有哪些數字已被拿來用
    ans = visiting(nums, numsSize, table, 1, mask);//先第1層計算

    return ans;
}
//case 46/76: [39759,619273,859218,228161,944571,597983,483239,179849,868130,909935,912143,817908,738222,653224]
