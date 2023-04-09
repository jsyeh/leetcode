class SortNode implements Comparator<Node> {
    public int compare(Node n1, Node n2) { return n1.indegree-n2.indegree; }
}
class Node {
    int[] H = new int[26];
    boolean visited;
    int id;
    int indegree=0;
    ArrayList<Node> src, dest;
    int color;
    Node(int i, char c) {
        id = i;
        color = c-'a';
        src = new ArrayList<Node>();
        dest = new ArrayList<Node>();
    }
}
class Solution {
    //這題的策略：cicle的話return -1
    //沒有cycle的話，就照著map去找
    //不過看了有人分享的解答後，好像是要先分析 indegree 的人在哪裡,從這些人往下走
    //每個node會記錄它之前走過哪些色彩的count int [] H = new int[26]
    //下一個人，則是看它之前走過哪些
    //不過，如果某個點有2人以上走進來，那要看最大的數據嗎？比如之前 aaa 及 bbb 要記哪一個？
    //好像記錄最大值即可
    //HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
    Node[] node;
    int N;
    public int largestPathValue(String colors, int[][] edges) {
        N = colors.length();
        node = new Node[N];
        for(int i=0; i<N; i++){
            node[i] = new Node(i, colors.charAt(i));
        }

        for(int i=0; i<edges.length; i++){
            int a = edges[i][0], b = edges[i][1];
            if(a==b) return -1; //cycle
            //node[a].dest.add(b);
            node[a].dest.add(node[b]);
            node[b].src.add(node[a]);
            node[b].indegree++;
        }
        //02:45 建好 map
        //要怎麼 detect cicle呢？ 就dfs而且遇到visited的話，就是
        //build heap
        int ans=0;
        PriorityQueue<Node> heap = new PriorityQueue<Node>(new SortNode());
        for(int i=0; i<N; i++){
            if(node[i].indegree==0){
                heap.offer(node[i]);//如果indegree是0，就可以拿出來做事
            }
        }
        if(heap.size()==0) return -1;//等於全部都沒有，就完了
        while(heap.size()>0){
            Node now = heap.poll();
            for(Node parent : now.src){
                for(int c=0; c<26; c++){
                    if(parent.H[c]>now.H[c]) now.H[c]=parent.H[c];
                    if(now.H[c]>ans) ans = now.H[c];
                }
            }
            now.H[now.color]++;//加上自己的色彩
            if(now.H[now.color]>ans) ans = now.H[now.color];

            for(Node child : now.dest){
                child.indegree--; //這樣可能會破壞 PriorityQueue的結構
                if(child.indegree==0) heap.offer(child);
            }
        }
        for(int i=0; i<N; i++){
            if(node[i].indegree>0) return -1;//表示有點沒走到
        }
        return ans;
    }
}
