class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int N = isConnected.size();
        bool visited[N];
        for(int i=0; i<N; i++) visited[i] = false;

        int ans = 0;
        for(int i=0; i<N; i++) {
            if(!visited[i]) {
                ans++;
                visiting(isConnected, i, visited);
            }
        }
        return ans;
    }
    void visiting(vector<vector<int>>& isConnected, int i, bool * visited) {
        visited[i] = true;
        for(int k=0; k<isConnected.size(); k++) {
            if(isConnected[i][k]==1 && !visited[k]){
                visiting(isConnected, k, visited);
            }
        }
    }
};
