// LeetCode 1668. Maximum Repeating Substring
// 這題好難想。Solutions 有人用迴圈暴力做(測不同長度），就簡單了
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        string repeat = word;
        int ans = 0;
        while(sequence.find(repeat) != -1) {
            ans += 1;
            repeat += word;
        }
        return ans;
    }
};
