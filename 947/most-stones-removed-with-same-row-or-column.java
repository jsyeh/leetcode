class Solution {
    public int removeStones(int[][] stones) {
        int N = stones.length;
        boolean [] visited = new boolean[N];
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0; i<N; i++){
            adj.add(new ArrayList<Integer>()); //代表與 i 相接的點
        }

        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                if(stones[i][0]==stones[j][0] || stones[i][1]==stones[j][1]) {
                    adj.get(i).add(j);//兩個方向都相連
                    adj.get(j).add(i);//兩個方向都相連
                }
            }
        }

        int ans=0; //表示留下來的石頭
        for(int i=0; i<N; i++){
//System.out.print(adj.get(i).size()+" ");
            if(!visited[i]){
                dfs(adj, N, visited, i);
                ans++;
            }
        }
//System.out.println("ans:"+ans);
        return N - ans;//表示消掉的石頭
    }
    void dfs(ArrayList<ArrayList<Integer>> adj, int N, boolean[] visited, int i){
//System.out.print(i+ " ");
        visited[i] = true;
        for(int k : adj.get(i)){
            if(!visited[k]) {
                dfs(adj, N, visited, k);
            }
        }
    }
}
