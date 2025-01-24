// LeetCode 1071. Greatest Common Divisor of Strings
// 想找 str1 和 str2 共同的 substring 子字串（str1 和 str2 需全部由它重覆組合出來）
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // 特殊性質：若有重覆成份，那正著接、反著接，都會是相同的
        if(str1+str2 == str2+str1) { 
            int len = gcd(str1.length(), str2.length()); // 只要找出長度即可
            // 沒想到 C++ 也有 gcd() 可以用
            return str1.substr(0, len);
        } else return "";
    }
};
