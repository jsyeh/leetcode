class Solution {
    
    public int latestDayToCross(int M, int N, int[][] cells) {
        //cells[i][0], cells[i][1] 表示第i天會增加淹水的座標
        //題目要問：最後一天還能渡過（也就表示，捷徑不管，要看「撐到最後天」是多久？
        //也就是問，幾天之後，路就斷光光了！
        //每次BFS需要 2*10^4 個 cell
        //因為這題 2*10^4 很大，所以要有效率一些，不能有2層迴圈
        //不能一天一天測，可使用 binary search來解決
        int[][] map = new int[M+2][N+2]; //每次都要一堆memory很慢
        //使用sentinel技巧，外面包一圈海洋
        for(int i=0; i<M+2; i++){
            map[i][0] = 1; //water
            map[i][N+1] = 1; //water
        }
        for(int j=0; j<N+2; j++){
            map[0][j] = 1; //water
            map[M+1][j] = 1; //water
        }

        int left = 0, right = M*N, mid = 0, oldMid=0;
        while(left<right) {
            oldMid = mid;
            mid = (left+right)/2;
//System.out.println("left:"+left+" right:"+right+" mid:"+mid+" oldMid:"+oldMid);
            if(oldMid<mid) { //正向去淹水
                for(int k=oldMid; k<mid; k++){
                    int i = cells[k][0], j = cells[k][1];
                    map[i][j] = 1;//想到一種「倒退嚕」的作法，重覆使用同一個map
                }
            }else{ //倒退嚕：倒向，陸地露出來
                for(int k=oldMid; k>=mid; k--){
                    int i = cells[k][0], j = cells[k][1];
                    map[i][j] = 0;//想到一種「倒退嚕」的作法，重覆使用同一個map
                }
            }
//for(int i=1; i<=M; i++){
//    for(int j=1; j<=N; j++){
//        System.out.print(map[i][j]);
//    }
//    System.out.println();
//}
            boolean success = BFS(M, N, map);
            if(success) left = mid+1;
            else right = mid;
//System.out.println("success:"+success);
        }
//System.out.println("left:"+left+" right:"+right+" mid:"+mid+" oldMid:"+oldMid+"--");
        //上面的迴圈，left是找到第1個失敗的位置，所以left-1就會變成「最後1次成功」
        return left-1;
    }
    boolean BFS(int M, int N, int[][] map) {
        boolean [][] visited = new boolean[M+2][N+2];
        Queue<int[]> queue = new LinkedList<>();
        for(int j=1; j<=N; j++) {
            testAndVisit(map, visited, queue, 1, j);//可能的開始點，全塞
        }
        while(queue.size()>0){
            int [] pos = queue.poll();
            int i = pos[0], j = pos[1];
//System.out.println("i:"+i+" j:"+j);
            if(i==M) return true; //順利走到對岸

            testAndVisit(map, visited, queue, i+1, j);
            testAndVisit(map, visited, queue, i-1, j);
            testAndVisit(map, visited, queue, i, j+1);
            testAndVisit(map, visited, queue, i, j-1);
        }
        return false; //無法順利走到對岸
    }
    void testAndVisit(int[][] map, boolean[][] visited, Queue<int[]>queue, int i, int j) {
        if(visited[i][j]==false && map[i][j]==0){ //（沒去過的）陸地
            queue.offer(new int[]{i,j});
            visited[i][j] = true;
        }
    }
}
