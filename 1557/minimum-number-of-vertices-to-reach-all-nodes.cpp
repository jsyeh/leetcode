class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        //技巧:如果可以從別人走過來,那這個頂點就不用留下來
        //所以先照"進來的數量" 排序, 再依序移掉
        vector<int> ans;
        vector<bool> hasIncome(n);
        for(vector<int> edge : edges) {
            hasIncome[edge[1]] = true;
        }

        for(int i=0; i<n; i++){
            if(!hasIncome[i]) ans.push_back(i);
        }

        return ans;
    }
};
