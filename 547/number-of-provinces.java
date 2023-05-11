class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean [] visited = new boolean[n];

        int ans = 0;
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                ans++;
                visiting(visited, n, isConnected, i);
            }
        }
        return ans;
    }
    void visiting(boolean [] visited, int n, int[][] isConnected, int i) {
System.out.print(i+" ");
        visited[i] = true;
        for(int k=0; k<n; k++) {
            if(isConnected[i][k]==1 && !visited[k]) {
                visiting(visited, n, isConnected, k);
            }
        }
    }
}
