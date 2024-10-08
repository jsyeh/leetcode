// LeetCode 1963. Minimum Number of Swaps to Make the String Balanced
// 一堆括號，要交換幾次，才能 balanced 括號正確括好？
int minSwaps(char* s) {
    int ans=0; // 需要 swap 幾次（把前面的 ] 與後面的 [ 交換）
    int depth=0; // 目前殘留的「上括號」數，也就是「容忍度」
    for(int i=0; s[i]!=0; i++){ // 字串的迴圈
        if(s[i]=='[') depth++; // 太好了，多1個「上括號」備用
        else{ // 哇！遇到「下括號」，需要用掉「上括號」
            if(depth>0) depth--; // 上括號數量足夠，就簡單「減掉」
            else{ // 但是「上括號」數量不夠怎麼辦？
                ans++; // 需要多1次交換
                depth++; // 因為後面的「上括號」拿來前面用，所以「容忍度」增加1個
            }
        }
    }    
    return ans;
}
