class Solution {
public:
    int largestVariance(string s) {
        unordered_set<char> unique(begin(s), end(s));//把字串每個字母拿去統計，了解有哪些 unique 的字母，以便暴力法的迴圈可以用
        int ans = 0;
        for(char a : unique){ //有出現的字母，暴力去試每個字母，兩兩比較
            for(char b : unique){ // a 比 b 多的情況，看看最大可以差多少
                int diff = 0;
                bool has_b = false, substring_begin_b = false;
                for(char c : s){ //將字串裡的字母，逐一比較
                    if(c == a) diff++; //a比b 再多1個
                    if(c == b) { //c有可能是其他字母，假設是b,那diff會減減哦
                        has_b = true; //現在的substring 有含b,就可以算diff了
                        //意思是，如果b都沒出現的話，這個substring的variance是0
                        if(substring_begin_b && diff>=0){
                            substring_begin_b = false; //diff恢復為正，就不用委曲了
                        }else if( --diff < 0){ //先減，再確認正負
                            substring_begin_b = true; //委曲一下吧
                            diff = -1; //這個值不會用
                        }
                    }
                    //現在結束在 c 的 substring，它的答案有更大嗎？
                    if(has_b && diff>ans) ans = diff;
                    //有b便能a與b比較，這時候若 diff值更大，那就更新
                }
            }
        }
        return ans;
    }
};
//case 124/138: "abbabaaba"
//題目超難看懂的。（理解錯誤）s裡，只有2種字母。substring的字母，差幾個，就是variance
//如果是DP解 table[i][k] 表示前i個字母的substring裡，最大的variance
// 因為substring要連續，所以 table[i][k]是要包含 k-th 字母
//
//查看解法，因有26種可能字母，有26x26種組合，要看差最多的。如果只有1種字母，那差的值是0
//要看差最多，就暴力挑2個字母，查看差最多是到多少
//https://leetcode.com/problems/substring-with-largest-variance/solutions/2039178/weird-kadane/


