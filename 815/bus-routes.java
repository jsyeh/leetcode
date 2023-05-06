class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        //我有參考 lee215's solution, 他的解法蠻妙的
        if(source==target) return 0;
        
        HashMap<Integer,ArrayList<Integer>>mapStopRoutes = new HashMap<>();
        //將第stop站牌，對應有經過那個站牌的公車路線i
        for(int i=0; i<routes.length; i++) { //第i條公車路線
            for(int stop : routes[i]) { //停到第stop個站牌
                if(!mapStopRoutes.containsKey(stop)){
                    mapStopRoutes.put(stop, new ArrayList<Integer>()); //空白對照表
                }
                mapStopRoutes.get(stop).add(i); //第i條路，有經過第stop個站牌
            }
        }

        HashSet<Integer> visited_stop = new HashSet<>();
        HashSet<Integer> visited_route = new HashSet<>();
        Queue<int[]> queue = new LinkedList<int[]>();
        int[] start = {source, 0};
        queue.offer(start); //走0步，可以到source, 右邊是bfs的距離
        visited_stop.add(source);

        while(queue.size()>0){
            int []now_dist = queue.poll();
            int nowStop = now_dist[0], dist = now_dist[1];

            for(int i : mapStopRoutes.get(nowStop)) { //第i條route會經過nowStop
                if(visited_route.contains(i)) continue;
                visited_route.add(i);

                for(int stop : routes[i]){
                    if(stop==target) return dist+1;
                    int[] temp = {stop, dist+1};
                    queue.offer(temp);
                    visited_stop.add(stop);
                }
            }
        }
        return -1;
    }
}//case 44/47: [[1,7],[3,5]] 5 5
