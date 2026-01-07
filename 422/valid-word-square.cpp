// LeetCode 422. Valid Word Square
// 檢查 words 裡 words[i][j]與words[j][i]全部相同
// 不一定是「方塊」哦！
// case 33/35: ["abc", "b", "c"] 竟然有「奇怪形狀」的 words
class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        for (int i=0; i<words.size(); i++) {
            for (int j=0; j<words[i].size(); j++) { 
                // words[j][i] 跑到外面，失敗
                if (j>=words.size() || i>=words[j].size()) return false;
                // 只要有任何不同，就失敗
                if (words[i][j] != words[j][i]) return false;
            }
        }
        // 都沒有失敗，就成功
        return true;
    }
};
