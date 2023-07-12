class Solution {
public:
    vector<int> ans;
    vector<int> terminal;
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int N = graph.size();
        vector<int> state(N, 0); //0: unvisited, 1: unsafe, 2: safe

        //這個演算法很特別：經過但未確認的點，都先當 unsafe, 
        //所以再度踩到自己時，便「確認」有loop而「不安全」，可以 return
        for(int i=0; i<graph.size(); i++){
            if( dfsCheckSafe(graph, state, i) == true ) ans.push_back(i);
        }

        //sort(ans.begin(), ans.end()); //題目說結果需要排序好
        //因為程式的迴圈是從小到大去檢查，所以已經排序好了，不用再排序一次
        return ans;
    }

    bool dfsCheckSafe(vector<vector<int>>& graph, vector<int>& state, int i) {
        //state[i] 0: unvisited, 1: unsafe, 2: safe
        if(state[i]==1) return false; //有走到 unsafe 包含可能有loop發生
        if(state[i]==2) return true; //有走到安全的，那就是安全

        //凡正在走過的，都先標為不安全，直到檢查成功，就確認安全
        state[i] = 1; //unsafe
        for(int next : graph[i]) {
            if(dfsCheckSafe(graph, state, next)==false) return false;//確認不安全
        }
        //都檢測通過（沒有走到險地）就是安全
        state[i] = 2; //safe

        return true;//safe
    }

    
};
