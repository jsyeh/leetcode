class Solution {
    boolean [][] edge;
    boolean [] visited;
    int N;
    public int numSimilarGroups(String[] strs) {
        N = strs.length;
        edge = new boolean[N][N];
        for(int i=0; i<strs.length; i++) {
            for(int j=i+1; j<strs.length; j++) {
                if( similar(strs[i], strs[j]) ) {
                    edge[i][j] = edge[j][i] = true;
                }
            }
        }
        visited = new boolean[N];
        
        int groupN=0;
        for(int i=0; i<N; i++) {
            if(!visited[i]) {
                groupN++;
                dfs(i);
            }
        }
        return groupN;
    }
    void dfs(int i) {
        visited[i] = true;
        for(int j=0; j<N; j++){
            if( visited[j] == false && edge[i][j] == true) {
                dfs(j);
            }
        }
    }
    boolean similar(String a, String b) {
        int diff=0;
        for(int i=0; i<a.length(); i++){
            if(a.charAt(i)!=b.charAt(i)) diff++;
        }
        if(diff==0 || diff==2) return true;
        else return false;
    }
}
