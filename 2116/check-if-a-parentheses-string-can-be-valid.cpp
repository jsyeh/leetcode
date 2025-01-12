// LeetCode 2116. Check if a Parentheses String Can Be Valid
// s 裡有很多括號，locked會鎖住某些括號/不能改變，問能不能變成正確的括號組合
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int d1 = 0, d2 = 0; // 括號深度的範圍：上界 d1 和下界 d2
        int N = s.length();
        if(N%2==1) return false; // 奇數，一定沒辦法正確括號配對
        for(int i=0; i<N; i++) { // 逐個字母處理
            if(locked[i]=='1') { // 被鎖住，不能變動
                if(s[i]=='(') { // 上括號，範圍一起就加深
                    d1++;
                    d2++;
                } else { // 下括號，範圍就一起變淺
                    d1--;
                    d2--;
                }
            } else { // locked[i]=='0' 沒有鎖住，可隨意變化
                d1++; // 加大範圍，上界上升
                d2--; // 加大範圍，下界下降
            }
            if(d1<0) return false; // 上界變成負的，就是全部範圍都變成負的，配對失敗
            if(d2<0) d2 = 0; // 負的範圍無效，就放新的下界在0的地方
        }
        if(d2==0) return true; // 最後範圍能順利到0，成功
        return false; // 沒有成功，就失敗
    }
};
