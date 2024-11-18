// LeetCode 2515. Shortest Distance to Target String in a Circular Array
// 從 words 的 startIndex 出發，可往右走 or 往左走，希望走到 target 要幾步
class Solution {
public:
    int closetTarget(vector<string>& words, string target, int startIndex) {
        int N = words.size();
        for(int i=0; i<N; i++) { // 由近到遠，逐一試各種距離
            if(words[(startIndex+i)%N]==target) return i;
            if(words[(startIndex+N-i)%N]==target) return i;
        }
        return -1; // 找不到的話，就回傳 -1
    }
};
