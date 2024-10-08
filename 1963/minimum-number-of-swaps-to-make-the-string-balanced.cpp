// LeetCode 1963. Minimum Number of Swaps to Make the String Balanced
// 一堆括號，要交換幾次，才能 balanced 括號正確括好？
class Solution {
public:
    int minSwaps(string s) {
        int ans = 0; // 需要 swap 幾次（把前面的 ] 與後面的 [ 交換）
        int depth = 0; // 目前殘留的「上括號」數，也就是「容忍度」
        for(char c : s){ // 逐字母分析
            if(c=='[') depth++; // 遇到上括號，很好，增加深度
            else{ // 遇到下括號
                if(depth>0) depth--; // 如果「上括號」累積深度夠，就減
                else{ // 但累積的深度不夠時
                    ans++; // 要增加1次 swap，把 ] 與後面 [ 對調
                    depth++; // 對調後，還多1個上括號能用，很好
                }
            }
        }
        return ans;
    }
};
