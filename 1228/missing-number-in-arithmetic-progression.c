// LeetCode 1228. Missing Number In Arithmetic Progression
// 找到「等差級數」中，缺的那個數
int missingNumber(int* arr, int arrSize) {
    int diff = arr[1]-arr[0], diff2 = arr[2]-arr[1];
    if(diff<0) diff = (diff>diff2)?diff:diff2;
    else diff = (diff<diff2)?diff:diff2;

    if(diff==0) return arr[0]; // 如果都相同的數，那缺的是同一個數

    for(int i=0; i<arrSize-1; i++){
        if(arr[i+1]-arr[i] != diff) return arr[i]+diff;
    }
    return arr[0]; // 隨便啦，因為題目保證前面會有答案
}
