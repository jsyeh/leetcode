class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        //先找出 terminal node
        //再找出 safe node
        int N = graph.length;
        List<Integer> ans = new ArrayList<>();
        int[] state = new int[N];//0:unvisited, 1: safe, 2: unsafe

        for(int i=0; i<N; i++){
            if(dfs(graph, i, state)) ans.add(i);
        }
        return ans;
    }
    boolean dfs(int[][] graph, int i, int[] state) {
        if(state[i]==1) return true;//safe
        if(state[i]==2) return false;//unsafe

        state[i] = 2; //先unsafe 除非能通過下面檢測都沒事
        for(int next : graph[i]){
            if(dfs(graph, next, state)==false) return false;
        }
        state[i] = 1; //safe
        return true;
    }
}
