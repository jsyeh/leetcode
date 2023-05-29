class MRUQueue {
    ArrayList<Integer> queue;
    public MRUQueue(int n) {
        queue = new ArrayList<Integer>();
        for(int i=0; i<n; i++){
            queue.add(i+1);
        }
    }
    
    public int fetch(int k) {
        int temp = queue.get(k-1);
        for(int i=k-1; i<queue.size()-1; i++) {
            queue.set(i, queue.get(i+1));
        }
        queue.set(queue.size()-1, temp);
        return temp;
    }
}

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue obj = new MRUQueue(n);
 * int param_1 = obj.fetch(k);
 */
