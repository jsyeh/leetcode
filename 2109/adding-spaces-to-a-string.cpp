// LeetCode 2109. Adding Spaces to a String
// 要在字串裡，照著 spaces[i] 的位置，加入空格。
class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int L = s.length(), S = spaces.size();
        string ans(L+S, ' '); // 先準備全部的長度
        for(int i=0, i2=0, spacesI=0; i<L; i++, i2++) { // 迴圈有2個index
            if(spacesI<S && spaces[spacesI]==i) { //遇到空格的座標
                ans[i2++] = ' '; // 就填上空格
                spacesI++;
            }
            ans[i2] = s[i];
        }
        return ans;
    }
};
