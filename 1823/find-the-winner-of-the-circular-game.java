class Solution {
    Queue<Integer> queue = new LinkedList<Integer>();
    public int findTheWinner(int n, int k) {
        for(int i=1; i<=n; i++){
            queue.offer(i);
        }
        while(queue.size()>1){
            for(int i=0; i<k-1; i++){
                queue.offer(queue.poll());
            }
            queue.poll();
        }
        return queue.poll();
    }
}
