class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        //陣列很長，一定要有技巧才行。可能要先排序
        //如果position排序，便能知道先後關係，可逐一比對（在時間內會不會撞在一起）
        //其實車隊，就是撞在一起的意思
        //對speed排序，可能較沒有用。
        //但現在要將 position 及 speed 綁在一起排序，才有意義
        int N = position.length;
        int [][] car = new int[N][2]; //car[i][0] 是位置，car[i][1]是速度
        for(int i=0; i<N; i++) {
            car[i][0] = position[i];
            car[i][1] = speed[i];
        }
        Arrays.sort(car, (a,b)->a[0]-b[0]);
//for(int i=0; i<N; i++){
//System.out.println(car[i][0] + "(" + car[i][1] + ") ");
//}
        float [] time = new float[N]; //到target的時間
        for(int i=0; i<N; i++) {
            float dist = target - car[i][0]; //到target的距離
            time[i] = dist / car[i][1];//預計到target的時間
//System.out.print(time[i] + " ");
        }

        int group = 1; //最右車 car[N-1] 是第1個group
        for(int i=N-2; i>=0; i--) { //迴圈要倒過來，因可能前面都沒撞，但最後撞成一團
            //逐一檢查 car[i] vs. car[i+1] 會不會追上
            //題目說，在target剛好追上，也視為追上
            if(time[i] > time[i+1]) group++; //左車晚到，不會追上，car[i]是新group
            else { //若有撞上，還需要更新 car[i] 的到達的時間 time[i]
                time[i] = time[i+1];
            }
        }
        return group;
    }
}
