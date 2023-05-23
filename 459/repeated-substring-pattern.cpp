class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        //這題我沒什麼頭緒, 所以看了 Solutions 裡別人的解答。
        //很多人使用 s + s 再剪掉頭尾
        //然後把 s 拿去比對, 如果有出現,表示是 repeated 的 patern
        //我猜測它的原理, 是因為 s + s 再剪掉頭尾, 造成前半、後半,都無法與 s 比對成功
        //這時候, 如果還成功比對, 那一定是重覆pattern在中間疊起來了。
        //那會不會有反例呢? 不會有的。因為 s 很長, 如果能比到, 就把前半、後半都有照顧到
        int N = s.length();
        string s2 = s + s;
        return s2.substr(1, N*2-2).find(s) != string::npos ;
    }
};
