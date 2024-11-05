// LeetCode 3114. Latest Time You Can Obtain After Replacing Characters
// 時鐘有些字被 '?' 蓋住。問「最晚」的可能時間是何時？
class Solution {
public:
    string findLatestTime(string s) {
        for(int hh=11; hh>=0; hh--) {
            for(int mm=59; mm>=0; mm--) {
                char h0 = '0' + (hh/10);
                char h1 = '0' + (hh%10);
                char m0 = '0' + (mm/10);
                char m1 = '0' + (mm%10);
                bool b0 = s[0]=='?' || (s[0]==h0);
                bool b1 = s[1]=='?' || (s[1]==h1);
                bool b3 = s[3]=='?' || (s[3]==m0);
                bool b4 = s[4]=='?' || (s[4]==m1);
                if(b0 && b1 && b3 && b4) return string("") + h0 + h1 + ':' + m0 + m1;
            }
        }
        return "";
    }
}
