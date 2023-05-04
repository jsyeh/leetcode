class Solution {
    int[][] H;
    int M, N;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        H = heights;
        M = heights.length;
        N = heights[0].length;
        boolean [][][]ocean = new boolean[2][M][N];
        for(int o=0; o<2; o++){
            boolean [][]visited = new boolean[M][N];
            Queue<int[]>queue = new LinkedList<>();
            if(o==0) {
                for(int i=0; i<M; i++) add(queue, i, 0, 0, visited, ocean[o]);
                for(int j=0; j<N; j++) add(queue, 0, j, 0, visited, ocean[o]);
            } else {
                for(int i=0; i<M; i++) add(queue, i, N-1, 0, visited, ocean[o]);
                for(int j=0; j<N; j++) add(queue, M-1, j, 0, visited, ocean[o]);
            }

            while(queue.size()>0) {
                int[] pos = queue.poll();
                int i = pos[0], j = pos[1];
                add(queue, i-1, j, H[i][j], visited, ocean[o]); 
                add(queue, i+1, j, H[i][j], visited, ocean[o]); 
                add(queue, i, j-1, H[i][j], visited, ocean[o]); 
                add(queue, i, j+1, H[i][j], visited, ocean[o]); 
            }
        }
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(ocean[0][i][j] && ocean[1][i][j]){
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(i);
                    temp.add(j);
                    ans.add(temp);
                }
            }
        }
        
        return ans;
    }
    void add(Queue<int[]>queue, int i, int j, int prevH, boolean[][] visited, boolean[][] ocean) {
        if(i<0 || j<0 || i>=M || j>=N) return;
        if(visited[i][j]) return;
        if(H[i][j]>=prevH){ //倒過來想，水可以逆流爬山
            ocean[i][j] = true;
            int[] pos = {i,j};
            queue.offer(pos);
            visited[i][j] = true;
        }
    }
}
