class Solution {
    HashMap<Integer, ArrayList<Integer>> tree = new HashMap<>();
    boolean [] visited;
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        visited = new boolean[n];
        for(int i=0; i<n; i++) {
            int m = manager[i];
            ArrayList<Integer> list;
            if(tree.containsKey(m)) {
                list = tree.get(m);
            } else {
                list = new ArrayList<Integer>();
                tree.put(m, list);
            }
System.out.print(" "+m);
            list.add(i);
        }
        return visiting(n, headID, manager, informTime);
    }
    int visiting(int n, int headID, int[] manager, int[] informTime) {
        visited[headID] = true;
        int ans = informTime[headID];
        ArrayList<Integer> list = tree.get(headID);
        if(list==null) return ans; //沒有下屬，就直接return

        int maxTime = 0;
System.out.println(".");
        for(Integer next : list) {
            int temp = visiting(n, next, manager, informTime);
            if(temp>maxTime) maxTime = temp;
        }
        return ans + maxTime;
    }
}
