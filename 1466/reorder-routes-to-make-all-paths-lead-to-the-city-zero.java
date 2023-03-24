class Solution { //條條大路通羅馬
    public int minReorder(int n, int[][] connections) {
        //題目描述，edge有n-1，所以其實就是最精簡的連線狀況。
        //所以解法就是，從0開始，進行 graph 旅行。然後看前後關係反過來的有幾個，就是答案
        //資料結構，可以存 connections的index
        boolean [] visited = new boolean[n];
        //ArrayList<ArrayList<Integer>> table = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> [] table = new ArrayList[n];
        for(int i=0; i<n; i++){
            //table.add(new ArrayList<Integer>());
            table[i] = new ArrayList<Integer>();
        }
        
        for(int i=0; i<connections.length; i++){
            int a = connections[i][0], b = connections[i][1];
            //table.get(a).add(i);
            //table.get(b).add(i);
            table[a].add(i);
            table[b].add(i);
        }

        int ans = 0;
        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.push(0);
        while(queue.size()>0){
            int now = queue.pop();
            visited[now]=true;
            //ArrayList<Integer> list = table.get(now);
            ArrayList<Integer> list = table[now];

            for(int i=0; i<list.size(); i++){
                int idx = list.get(i);
                if(connections[idx][0]==now){
                    if(!visited[connections[idx][1]]){
                        ans++;
                        queue.push(connections[idx][1]);
                    }
                }else{
                    if(!visited[connections[idx][0]]){
                        queue.push(connections[idx][0]);
                    }
                }
            }
        }
        return ans;
    }
}
