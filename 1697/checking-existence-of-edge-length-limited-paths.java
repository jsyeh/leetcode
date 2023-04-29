class Solution {
    int [] parent;
    int [] count;
    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        int qN = queries.length;
        int eN = edgeList.length;
        int [][] sortedQ = new int[qN][4];
        for(int i=0; i<qN; i++) {
            for(int k=0; k<3; k++) {
                sortedQ[i][k] = queries[i][k];
            }
            sortedQ[i][3] = i; //original index in queries
        }
        Arrays.sort(sortedQ, (a,b) -> a[2]-b[2]);
        Arrays.sort(edgeList, (a,b) -> a[2]-b[2]);

        //build union and parent
        parent = new int[n];
        count = new int[n];
        for(int i=0; i<n; i++) {
            parent[i] = i; //一開始node都獨立，parent是自己
            count[i] = 1; //每一群裡的數量都只有1
        }

        boolean [] ans = new boolean[queries.length];

        int edge = 0;
        for(int i=0; i<qN; i++){
            int limit = sortedQ[i][2];
            while(edge<eN && edgeList[edge][2]<limit){
                int a = edgeList[edge][0];
                int b = edgeList[edge][1];
                Union(a, b);
                edge++;
            }

            int setA = Find(sortedQ[i][0]);
            int setB = Find(sortedQ[i][1]);
            if(setA == setB) ans[sortedQ[i][3]]=true;
            else ans[sortedQ[i][3]]=false;
        }
        return ans;
    }
    void Union(int a, int b) {
        int setA = Find(a);
        int setB = Find(b);
        if(setA==setB) return;
        //以下則是要回併set
        if(count[setA]>count[setB]) { //如果 setA 比較大
            count[setA] += count[setB];//把 setB 都併到大的 setA 裡
            parent[setB] = setA;
        } else {
            count[setB] += count[setA];//把 setA 都併到大的 setB 裡
            parent[setA] = setB;
        }
    }
    int Find(int node) {
        if(parent[node]==node) return node; //本身獨立

        parent[node] = Find(parent[node]); //若有歸屬，整串都更新
        return parent[node];
    }
}
