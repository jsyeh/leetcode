class Solution {
    int N;
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        //for(Integer j : graph[0]) 會把 0 走到的j全部列出來
        N = graph.length;
        dfs(graph, 0, new ArrayList<Integer>());

        return ans;
    }
    void dfs(int[][] graph, int i, List<Integer> path) {
        path.add(i);
        if(i==N-1) {
            List<Integer> temp = new ArrayList<Integer>();
            for(Integer now : path){
                temp.add(now);
            }
            ans.add(temp);
        }
        for(Integer next : graph[i]){
            dfs(graph, next, path);
        }
        path.remove(path.size()-1);
    }
}
