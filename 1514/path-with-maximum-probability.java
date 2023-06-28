class Node {
    int i;
    double p;//到達此點的機率
    Node(int index, double prob) {
        i = index;
        p = prob;
    }
}
class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        //可以用 BFS 的 full search 來把全部的機率算出來, 再找最大機率
        //但有個問題,是有時遠路反而要走,因為機率大。所以要用 Priority Queue 來標示下一個頂點的機率
        boolean[] visited = new boolean[n];
        PriorityQueue<Node> queue = new PriorityQueue<Node>((a,b)->(a.p-b.p)<=0?1:-1);
        queue.offer(new Node(start, 1));
        //visited[start] = true;//不可以先visited

        //要建 ArrayList 以便知道有哪些 next 點
        ArrayList<Integer>[] next = new ArrayList[n];
        ArrayList<Double>[] prob = new ArrayList[n];
        for(int i=0; i<n; i++) next[i] = new ArrayList<>();
        for(int i=0; i<n; i++) prob[i] = new ArrayList<>();

        for(int i=0; i<edges.length; i++) {
            int a = edges[i][0], b = edges[i][1];
            next[a].add(b);
            next[b].add(a);
            prob[a].add(succProb[i]);
            prob[b].add(succProb[i]);
        }

        while(queue.size()>0) {
            Node now = queue.poll();
            visited[now.i] = true;
            if(now.i==end) return now.p;
            
            ArrayList<Integer> nextI = next[now.i];
            ArrayList<Double> nextP = prob[now.i];
            for(int i=0; i<nextI.size(); i++) {
                int nextIndex = nextI.get(i);
                double nextProb = nextP.get(i);
                if(visited[nextIndex]==false) {
//System.out.println("nextIndex:"+nextIndex+ " nextProb:"+nextProb);
                    //visited[nextIndex]=true;//不可以先visited
                    queue.offer(new Node(nextIndex, nextProb * now.p));
                }
            }
        }
        return 0;
    }
}
