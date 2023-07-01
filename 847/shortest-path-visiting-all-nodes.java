//這題有點難，我參考別人的解法
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/135686/java-dp-solution/ 
//想到今天2023-07-02 挑戰題，也有利用 mask 進行 DP 的作法，很親切
// https://leetcode.com/submissions/detail/983628671/
class Solution {
    public int shortestPathLength(int[][] graph) {
        int N = graph.length, maskRange = 1 << N, maskAll = maskRange - 1;
        //maskRange 是在迴圈裡使用，如果 N 是 4個點, 0b1111 我用 maskAll 代表
        //for(int i=0; i<0b10000; i++) 可把 0b0000 ~ 0b1111 都走過一次
        int [][] table = new int[N][maskRange];
        Queue<State> queue = new LinkedList<>();
        for(int i=0; i<N; i++){ //思考第 i 個 node
            for(int k=0; k<maskRange; k++){ //mask k 有使用的點的排列組合
                table[i][k] = Integer.MAX_VALUE; //先設極大值，以便之後替換
            }
            table[i][1<<i] = 0; //第i個點，經過i可以到的距離，是0步
            //table[i][mask] 代表:只考慮mask裡的點全部走到，要到i的最短值
            queue.offer(new State(1<<i, i)); //上述每一個都可以是簡單的出發點
        }

        while( queue.size()>0 ) {
            State now = queue.poll(); //取出一組值，進行更新
            //now 可以再到的點
            for(int i=0; i<graph[now.start].length; i++){
                int next = graph[now.start][i]; //它可以找到的點，進行BFS
                int nextMask = now.mask | (1<<next); //將 nextMask 加next對應的bit 成為更完整的 mask
                if(table[now.start][now.mask]+1 < table[next][nextMask] ) {
                    table[next][nextMask] = table[now.start][now.mask]+1;
                    queue.offer(new State(nextMask, next)); //而且這個訊息要更新其他相關的 mask 的值
                } //如果經由 now 走到 next 的距離，比原本 next記錄的距離更短，就更新
            }
        }
        int ans = table[0][maskAll];
        for(int i=1; i<N; i++) { //想找出最短的距離值
            if(table[i][maskAll]<ans) ans = table[i][maskAll];
            //有更短的距離，就用更短的距離
        }
        return ans;
    }

    class State {
        int mask, start;
        State(int m, int s) {
            mask = m;
            start = s;
        }
    }
}
