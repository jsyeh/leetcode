//和昨天的挑戰題有點像，就是在DFS時，看有沒有遇到「走到一半還沒確認安全」的loop狀況
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //先把 prerequisites 變成 以 course為主的結構，以便查詢
        vector<vector<int>> depend(numCourses); //所以 depend[i] 裡，就有 course i 的先修課程
        for(int i=0; i<prerequisites.size(); i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];  //先修b,才能修a
            depend[a].push_back(b);
        }

        vector<int> state(numCourses, 0); //state[i] 0:unvisited, 1: unsafe, 2: safe
        for(int i=0; i<numCourses; i++) {
            if(dfsCheckSafe(depend, state, i)==false) return false; //只要有1個人失敗，就失敗了
        }
        return true; //都沒有失敗，就是成功
    }
    bool dfsCheckSafe(vector<vector<int>>& depend, vector<int>& state, int i) {
        //state[i] 0:unvisited, 1: unsafe, 2: safe
        if(state[i]==1) return false;
        if(state[i]==2) return true;

        state[i]=1; //先當成unsafe,以便看有沒有人撞到就出事
        for(int next : depend[i]) {
            if(dfsCheckSafe(depend, state, next)==false) return false; //只要有失敗，就失敗
        }

        state[i]=2;//確認安全
        return true;
    }
};
