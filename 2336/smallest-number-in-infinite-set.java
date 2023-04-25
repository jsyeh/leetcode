class SmallestInfiniteSet {
    PriorityQueue<Integer> heap;
    HashSet<Integer> set;
    int smallest = 1;
    public SmallestInfiniteSet() {
        heap = new PriorityQueue<Integer>();//1000, (a,b)->a-b);
        set = new HashSet<Integer>();
    }
    //如果沒有值, 就記得連續的最小的值
    public int popSmallest() {
        if(heap.size()==0){
            return smallest++;
        }
        int ans = heap.poll();
        set.remove(ans);
        return ans;
    }
    
    public void addBack(int num) {
        if(num>=smallest){
            return;//不做
        }
        if(!set.contains(num)){
            set.add(num);
            heap.offer(num);
        }
    }
}//case 119/135: ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
//[[],[],[],[3],[],[2],[],[]]

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */
