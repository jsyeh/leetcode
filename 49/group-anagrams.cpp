class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, int> map;//把 sorted string 對應到 group ID
        int groupID = 0;
        for(int i=0; i<strs.size(); i++) {
            string sorted = sortString(strs[i]);
            //cout<< strs[i] << " to " << sorted << endl;
            auto got = map.find(sorted);
            if(got==map.end()) { //沒有找到
                vector<string> group;
                group.push_back(strs[i]);
                ans.push_back(group);
                map.insert( {sorted, groupID} );
                groupID++;
            } else {
                ans[got->second].push_back(strs[i]);
            }
        }
        return ans;
    }
    string sortString(string s) {
        std::sort(s.begin(), s.end());
        return s;
    }
};
