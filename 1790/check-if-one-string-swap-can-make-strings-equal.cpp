// LeetCode 1790. Check if One String Swap Can Make Strings Equal
// 字串 s1 最多「只調動2個字母」的位置，能不能變成 s2
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> diffI; // 用來記錄「不同字母」的 index i
        for(int i=0; i<s1.length(); i++) {
            if(s1[i] != s2[i]) {
                diffI.push_back(i);
                if(diffI.size()>2) return false; // 太多不同，失敗
            }
        }
        if(diffI.size()==0) return true; // 沒有不同/都相同，成功
        if(diffI.size()==2) { // 2個字母不同（怕程式太長，就斷開成3行）
            int i0 = diffI[0], i1 = diffI[1]; // 交錯的位置，剛好相同
            if(s1[i0]==s2[i1] && s1[i1]==s2[i0]) return true; // 就是成功
        }
        return false; // 都沒有成功
    }
};
