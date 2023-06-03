class SeatManager {
//想到，可以用PriorityQueue來做
    PriorityQueue<Integer> heap;
    public SeatManager(int n) {
        heap = new PriorityQueue<Integer>(n);
        for(int i=1; i<=n; i++) heap.offer(i);
    }
    
    public int reserve() {
        Integer ans = heap.poll();
        return ans;
    }
    
    public void unreserve(int seatNumber) {
        heap.offer(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
