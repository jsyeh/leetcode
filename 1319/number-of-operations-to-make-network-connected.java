class Solution {
    public int makeConnected(int n, int[][] connections) {
        int connN = connections.length; //Connection Number
        if(connN<n-1) return -1;
        //策略: (利用DFS/BFS)找出 connected component groupN
        //要數一下有幾個 group, 接下來便是 groupN-1 便是答案
        boolean [] visited = new boolean[n];
        int [] table = new int[n];//table[i]=哪一群,像篩子法一樣
        ArrayList<ArrayList<Integer>>mesh = new ArrayList<ArrayList<Integer>>(n);
        for(int i=0; i<n; i++){
            table[i] = i;
            visited[i] = false;
            mesh.add(i, new ArrayList<Integer>());
        }

        for(int i=0; i<connections.length; i++){
            int c1 = connections[i][0];
            int c2 = connections[i][1];
            mesh.get(c1).add(c2);
            mesh.get(c2).add(c1);
        }
        for(int i=0; i<n; i++){
            if(visited[i])continue;
            LinkedList<Integer> queue = new LinkedList<Integer>();
            queue.push(i);
            while(queue.size()>0){
                int now = queue.pop();
                visited[now]=true;
                ArrayList<Integer> array = mesh.get(now);
                for(int j=0; j<array.size(); j++){
                    int next = array.get(j);
                    table[next] = table[i];
                    if(!visited[next]){
                       queue.push(next);
                    }
                }
            }
        }
        /*for(int i=0; i<n; i++){ //這個方法好像不好
            ArrayList<Integer> array = mesh.get(i);
            int minGroup = table[i];
            for(int j=0; j<array.size(); j++){
                int next = array.get(j);
                if(table[next]<minGroup) { //??
                    minGroup = table[next];
                }
            }
            table[i] = minGroup;
            for(int j=0; j<array.size(); j++){
                table[j] = minGroup;
            }
        }*/

        HashSet<Integer> set = new HashSet<Integer>();
        for(int i=0; i<n; i++){
            if(!set.contains(table[i])) set.add(table[i]);
        }

        return set.size()-1;
    }
}//Case4: 11 [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]
//Case5: 8 [[0,2],[2,7],[5,7],[2,6],[1,3],[4,6],[1,2]]
//應該用DFS or BFS 去逐一改 table的鄰居,配合visited
