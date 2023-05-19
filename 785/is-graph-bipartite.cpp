class Solution {
public:
    bool bad = false;
    bool isBipartite(vector<vector<int>>& graph) {
        int N = graph.size();
        bool visited[N];
        int group[N];
        for(int i=0; i<N; i++){
            group[i] = 0; //1:A, 2:B
            visited[i] = false;
        }
        group[0] = 1;
        for(int i=0; i<N; i++){
            if(visited[i]) continue;
            visiting(graph, N, i, visited, group, 1);
        }
        if(bad) return false;
        else return true;
    }
    //利用函式呼叫函式，來完成DFS，把有相連的點全部處理掉（標號好）
    void visiting(vector<vector<int>>& graph, int N, int i, bool * visited, int * group, int expected) {
        if(visited[i]) {
            if(group[i]!=expected) bad=true; //不符合預期
            return;
        }
        visited[i] = true;
        group[i] = expected;
        for(int next : graph[i]) {
            visiting(graph, N, next, visited, group, 3-expected);
        }
    }
};
