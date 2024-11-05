// LeetCode 830. Positions of Large Groups
// 如果有連續3個以上「相同字母」，就把「開始、結束」加到ans裡
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        vector<vector<int>> ans;
        int count = 1; // 新的開始
        for(int i=0; i<s.length(); i++) {
            if(i<s.length()-1 && s[i]==s[i+1]) count++;
            else { // 不同時，便要看「是否 large group」連續3個
                if(count>=3) { //符合條件
                    vector<int> now;
                    now.push_back(i-count+1);
                    now.push_back(i);
                    ans.push_back(now);
                }
                count = 1; // 又是新的開始
            }
        }
        return ans;
    }
};
