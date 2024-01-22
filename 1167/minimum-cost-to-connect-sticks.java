// 要把小棒子都接成長棒子，直到全部接在一起
// 但是 cost 是兩段的長度。所以要利用 PriorityQueue 
// 每次挑「最短」的兩根結合，使用 offer() 和 poll()即可
class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int s : sticks) pq.offer(s);
        int ans = 0;
        while(pq.size()>1){ //只要還有2根以上，就繼續做
            int a = pq.poll(), b = pq.poll(); //最小的兩數
            ans += a+b;
            pq.offer(a+b); //再塞回去1個
        }
        return ans;
    }
}
