// LeetCode 1773. Count Items Matching a Rule
// items[i] 裡有 [type, color, name] 資訊。
// 另有 ruleKey 和 ruleValue，請統計「符合rule」有幾個 items，
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int ans = 0;
        for(int i=0; i<items.size(); i++) {
            if(ruleKey=="type" && ruleValue == items[i][0]) ans++;
            else if(ruleKey=="color" && ruleValue == items[i][1]) ans++;
            else if(ruleKey=="name" && ruleValue == items[i][2]) ans++;
        }
        return ans;
    }
};

