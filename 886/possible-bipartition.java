class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        //建出 map, 要小心題目是 1-index 不是 0-
        ArrayList<Integer> [] next = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            next[i] = new ArrayList<Integer>();
        }
        for(int i=0; i<dislikes.length; i++){
            int a = dislikes[i][0], b = dislikes[i][1];
            next[a].add(b);
            next[b].add(a);
        }
        //Idea: 照著dislike的資訊，逐一標號 1 or 2
        int [] color = new int[n+1]; //小心，題目是 1-index
        for(int i=1; i<=n; i++) { //小心，題目是 1-index
            if(color[i]==0) {
                boolean t = dfs(i, next, color, 1);
                if(t==false) return false;
            }
        }
        return true;
    }

    boolean dfs(int i, ArrayList<Integer>[] next, int[] color, int c) {
        if(color[i]==c) return true;//走過了，沒事
        if(color[i]==3-c) return false;//有衝突

        color[i] = c;
        for(Integer a : next[i]){
            boolean t = dfs(a, next, color, 3-c);
            if(t==false) return false;
        }

        return true;
    }
}
