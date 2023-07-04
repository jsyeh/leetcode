//如果是 2次 vs 1次，可以用 XOR 算出來
//但現在是 3次 vs. 1次，XOR出來的結果都一樣
//看了付費Editorial 裡，介紹4種方法（從直覺到符合題目要求）
//(1) sort, (2) hashmap, (3) hashset, (4) 修改xor
//也就是，每個bit的運算改成 MOD 3
int singleNumber(int* nums, int numsSize){
    int bits[32] = {};
    for(int i=0; i<numsSize; i++){
        int now = nums[i];
        for(int m=0; m<32; m++){
            int b = (now>>m) & 1;
            bits[m] = (bits[m] + b) % 3;
        }
    }
    //前面進行 bit3 XOR, 後面建出答案
    int ans = 0;
    //for(int m=31; m>=0; m--){
        //ans = ans << 2; ans = ans * 2; //正變負時出錯
        //ans += bits[m];
    //}
    //解法：用UINT_32
    //https://stackoverflow.com/questions/53566029/1-31-cannot-be-represented-by-type-int
    for(int m=31; m>=0; m--){
        if(bits[m]>0){
            ans ^= UINT32_C(1)<<m;
        }
    }
    return ans;
}
//Line 18: Char 13: runtime error: signed integer overflow: 2147483646 * 2 cannot be represented in type 'int' [solution.c]
//case 5/14: [-2,-2,1,1,4,1,4,4,-4,-2]
//這表示負的數字，在 在重建的過程中，會被警告「正數變負數」
