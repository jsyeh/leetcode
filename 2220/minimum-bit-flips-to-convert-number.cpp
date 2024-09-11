// LeetCode 2220. Minimum Bit Flips to Convert Number
// 比較2個數的 2進位 差幾個 bit
// 使用大一教過的「剝皮法」,再左右比對,不同就 ans++
class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;  //迴圈前面 ans=0
        while(start>0 || goal>0){ // 還有剩、還活著，就繼續剝皮
            if(start%2 != goal%2) ans++; //一言不合就++
            start /= 2; //剝皮
            goal /= 2; //剝皮
        }
        return ans; //迴圈後面 return ans
    }
};
