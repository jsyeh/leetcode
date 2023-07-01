public class Solution {
    public int FindCircleNum(int[][] isConnected) {
        int N = isConnected.Length;
        bool[] visited = new bool[N];
        int ans = 0;
        for(int i=0; i<N; i++) {
            if(!visited[i]) {
                ans++;
                bfs(isConnected, N, i, visited);
            }
        }
        return ans;
    }
    void bfs(int[][] isConnected, int N, int i, bool[] visited) {
        for(int k=0; k<N; k++) {
            if(isConnected[i][k]==1 && !visited[k]) {
                visited[k] = true;
                bfs(isConnected, N, k, visited);
            }
        }
    }
}
