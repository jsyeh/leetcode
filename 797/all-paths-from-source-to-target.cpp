class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> ans;
        vector<int> path;
        path.push_back(0);
        helper(graph, path, 0, ans);
        return ans;
    }
    void helper(vector<vector<int>>&graph, vector<int> path, int now, vector<vector<int>>& ans) {
        if(now==graph.size()-1) {
            ans.push_back(path);
        }
        for(int i : graph[now]) {
            path.push_back(i);
            helper(graph, path, i, ans);
            path.pop_back();
        }
    }
};
