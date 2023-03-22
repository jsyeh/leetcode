class Solution {
    Map<Integer, ArrayList<Integer>> map;
    Set<Integer> visited;
    public int minScore(int n, int[][] roads) {
        int ans=Integer.MAX_VALUE;
        map = new HashMap<Integer, ArrayList<Integer>>();
        visited = new HashSet<Integer>();
        LinkedList<Integer> queue = new LinkedList<Integer>();
        //看了之後,好像可以環繞世界一週。所以應該是看 1 能到的全部地方,找到最小的值。
        //不想要有太大的 10^10 的table,應該就要善用 Map HashMap 來找到 roads
        for(int i=0; i<roads.length; i++){
            addList(roads[i][0], roads[i][1], roads[i][2]);
        }
        queue.push(1);
        while(queue.size()>0){
            int now = queue.pop();
            if(!visited.contains(now)){
                visited.add(now);
                ArrayList<Integer> list = map.get(now);
                for(int i=0; i<list.size(); i+=2){
                    int next = list.get(i);
                    int val = list.get(i+1);
                    if(!visited.contains(next)){
                        queue.add(next);
                        if(val<ans) ans = val;
                    }
                }
            }
        }
        

        return ans;
    }
    void addList(int from, int to, int val){
        if(!map.containsKey(from)){
            map.put(from, new ArrayList<Integer>());
        }
        ArrayList<Integer> list = map.get(from);
        list.add(to);
        list.add(val);

        if(!map.containsKey(to)){
            map.put(to, new ArrayList<Integer>());
        }
        list = map.get(to);
        list.add(from);
        list.add(val);
    }
}
