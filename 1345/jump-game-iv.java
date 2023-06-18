class Solution {
    HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
    boolean[] visited;
    public int minJumps(int[] arr) {
        //有三種跳法：前一格、後一格、數字相同的格瞬間移動
        //這題好像可以用BFS，那為什麼是Hard?
        //先建出 HashMap<Integer,ArrayList<Integer>> 表示能跳的相同點
        int n = arr.length;
        for(int i=0; i<n; i++){
            int key = arr[i];
            if(map.containsKey(key)){
                ArrayList<Integer> list = map.get(key);
                list.add(i); //所以list最後面的數字，是能到最後的捷徑
            }else{
                ArrayList<Integer> list = new ArrayList<>();
                list.add(i);
                map.put(key, list);
            }
        }
        visited = new boolean[n];

        Queue<Integer> queueI = new LinkedList<Integer>();
        Queue<Integer> step = new LinkedList<Integer>();
        queueI.offer(0);
        step.offer(0);
        visited[0]=true;

        while(queueI.size()>0) {
            int nextI = queueI.poll();
            int s = step.poll();
            if(nextI==n-1) return s;
            if(nextI+1<n && !visited[nextI+1]) {
                queueI.offer(nextI+1);
                step.offer(s+1);
                visited[nextI+1]=true;
            }
            if(nextI-1>=0 && !visited[nextI-1]) {
                queueI.offer(nextI-1);
                step.offer(s+1);
                visited[nextI-1]=true;
            }

            //for(Integer i : map.get(arr[nextI])) {
            //這裡可能改成，凡用過的話，就減少map 的 ArrayList的內容
            ArrayList<Integer> list = map.get(arr[nextI]);
            for(int ii=list.size()-1; ii>=0; ii--){
                int i = list.get(ii);
                list.remove(ii);//邊做邊remove,減少數量，加速             
                int n2 = arr[i];
                if(!visited[i]){
                    queueI.offer(i);
                    step.offer(s+1);
                    visited[i]=true;
                }
            }
        }
        return n-1;
    }
}
//case 26/33: 有一大堆7,最後是11
//因為
