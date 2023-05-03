class Solution {
    ArrayList<Integer> seen = new ArrayList<Integer>();
    int [] states;
    HashMap<Integer,ArrayList<Integer>> map = new HashMap<Integer,ArrayList<Integer>>();
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        states = new int[numCourses]; //states[i]: 0:unvisited, 1: visiting, 2:visited

        for(int [] pre : prerequisites) {
            if(map.containsKey(pre[0])) {
                ArrayList<Integer> temp = map.get(pre[0]);
                temp.add(pre[1]);
            } else {
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(pre[1]);
                map.put(pre[0], temp);
            }
        }

        for(int i=0; i<numCourses; i++){
            if(states[i]==0) { //unvisited
                boolean error = dfs(i);//如果有錯誤
                //visiting的點又再度被visit,表示cyclic 錯誤
                if(error) return new int[0];
            }
        }
        int[] ans = new int[numCourses];
System.out.println(numCourses);
System.out.println("seen.size():" + seen.size());
        for(int i=0; i<numCourses; i++){
            ans[i] = seen.get(i);
        }
        return ans;
    }
    boolean dfs(int i) {
        if(states[i]==1) return true; //true error! 因為發生cycle
        states[i] = 1; //visiting
        if(map.get(i)!=null){
            for(var next : map.get(i)) {
                if(states[next]==2) continue; //visited
                boolean error = dfs(next);
                if(error) return error;//如果有錯誤，提早結束
            }
        }
        seen.add(i);
        states[i]=2;//visited
        return false; //no error
    }
}
