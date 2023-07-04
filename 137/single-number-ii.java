//如果是 2次 vs 1次，可以用 XOR 算出來
//但現在是 3次 vs. 1次，XOR出來的結果都一樣
//看了付費Editorial 裡，介紹4種方法（從直覺到符合題目要求）
//(1) sort, (2) hashmap, (3) hashset, (4) 修改xor
//也就是，每個bit的運算改成 MOD 3
class Solution {
    int [] bits = new int[32];
    public int singleNumber(int[] nums) {
        for(int i=0; i<nums.length; i++){
            int now = nums[i];
            for(int m=0; m<32; m++){
                int b = (now>>m)&1;
                bits[m] = (bits[m] + b)%3;
            }
        }
        //前面進行 bit3 XOR, 後面建出答案
        int ans = 0;
        for(int m=31; m>=0; m--){
            ans *=2;
            ans += bits[m];
        }
        return ans;
    }
}
