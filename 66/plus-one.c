/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    //先解決最特別的狀況：99999 + 1 要進位
    int nine=0;
    for(int i=0; i<digitsSize; i++){
        if(digits[i]==9) nine++;
    }
    if(nine==digitsSize){//特殊狀況，要準備多1格的memory
        int* ans = (int*)malloc(sizeof(int)*(digitsSize+1));
        ans[0] = 1;
        for(int i=1; i<=digitsSize; i++) ans[i] = 0;
        *returnSize = digitsSize+1;
        return ans;
    }

    //剩下的狀況，可輕鬆使用舊的 digits[i]陣列來放答案
    int carry=1;
    for(int i=digitsSize-1; i>=0; i--){
        digits[i]+=carry;
        if(digits[i]>9){
            digits[i] %= 10;
            carry=1;
        }else carry=0;
    }
    *returnSize = digitsSize;
    return digits;
}
