// LeetCode 3019. Number of Changing Keys
// 大小寫視為相同。s裡，換幾次key?
class Solution {
public:
    int countKeyChanges(string s) {
        int ans = 0;
        s[0] = tolower(s[0]); // 轉成小寫
        for(int i=0; i<s.length()-1; i++){
            s[i+1] = tolower(s[i+1]); // 全部轉成小寫
            if(s[i]!=s[i+1]) ans++; // 相鄰不同，就要換key
        }
        return ans;
    }
};
