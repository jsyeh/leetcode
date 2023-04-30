class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        int [] parent = new int[n+1]; //每個點先都是自己一類
        int [] count = new int[n+1];
        for(int i=0; i<=n; i++) parent[i] = i;
        for(int i=0; i<=n; i++) count[i] = 1;

        //先針對 edge 排序
        Arrays.sort(edges, (a,b)->b[0]-a[0]);

        int ans = 0;
        //先把 type3的部分加進去
        for(int i=0; i<edges.length; i++) {
            System.out.println(edges[i][0] + " " + edges[i][1] + " " + edges[i][2]);
            if(edges[i][0]==3) {//先優先處理 type 3
                int a = Find(parent, edges[i][1]);
                int b = Find(parent, edges[i][2]);
                if(a==b) {
                    ans++;//若連在一起，就不用再加它了
                } else {
                    Union(parent, count, a, b);
                }
            }
        }//有了type3的連結資訊後
        //再接著處理 type1 和 type2 的部分
        int [] parentA = new int[n+1];//Alice世界的群組
        int [] parentB = new int[n+1];//Bob世界的群組
        int [] countA = new int[n+1];//Alice世界的群組的數量
        int [] countB = new int[n+1];//Bob世界的群組的數量
        for(int i=1; i<=n; i++){
            parentA[i] = parent[i];
            parentB[i] = parent[i];
            countA[i] = count[i];
            countB[i] = count[i];
        }//把 type3 的連結資訊拿來用

        for(int i=0; i<edges.length; i++){
            if(edges[i][0]==1) { //Alice世界
                int a = Find(parentA, edges[i][1]);
                int b = Find(parentA, edges[i][2]);
                if(a==b) {
                    ans++;
                } else {
                    Union(parentA, countA, a, b);
                }
            } else if(edges[i][0]==2) {
                int a = Find(parentB, edges[i][1]);
                int b = Find(parentB, edges[i][2]);
                if(a==b) {
                    ans++;
                } else {
                    Union(parentB, countB, a, b);
                }
            }
        }

        //最後檢查是否全部相連
        for(int i=1; i<=n; i++) {
            if(Find(parentA, 1)!=Find(parentA, i)) return -1;
            if(Find(parentB, 1)!=Find(parentB, i)) return -1;
        }//有任何不相連，就是失敗
        return ans;//全部相連時，回傳剛剛數的答案（可移除edge數)
    }
    int Find(int[] parent, int i) {
        if(i==parent[i]) return i;//自己在同一國
        
        parent[i] = Find(parent, parent[i]);
        return parent[i];
    }
    void Union(int[] parent, int[] count, int a, int b) {
        int setA = Find(parent, a);
        int setB = Find(parent, b);
        if(setA == setB) return;//已經同一國，很好
        if(count[setA]>count[setB]) {
            count[setA] += count[setB];
            parent[setB] = setA;
            
        } else {
            count[setB] += count[setA];
            parent[setA] = setB;
        }
    }
}
