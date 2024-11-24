// LeetCode 443. String Compression
// 字串裡的「連續字母」要利用「字母、重覆的次數」來壓縮。
// 把壓縮後的字串，放回 chars 裡，再回傳「壓縮後」的字串長度
class Solution {
public:
    int compress(vector<char>& chars) {
        char prev = chars[0]; // 重覆的字母
        int combo = 1, pos = 0, N = chars.size();
        // 重覆的次數、放回chars的位置、原本字串的長度
        for(int i=1; i<N+1; i++) { // 多走1位
            if(i<N && chars[i]==prev) combo++;
            else { // 如果字母不同 或 超過字串長度
                chars[pos++] = prev;
                if(combo>1) {
                    string strCombo = to_string(combo); // combo 先變字串
                    for(char c : strCombo) { // 再逐個字母「塞回」chars
                        chars[pos++] = c;
                    }
                }
                combo = 1; // 從新的1開始
                if(i<N) prev = chars[i]; // 加個 if(i<N) 才不會出錯
            }
        }
        return pos;
    }
};
