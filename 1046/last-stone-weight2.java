class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(stones.length, (a,b) -> b-a);

        for(int i=0; i<stones.length; i++){
            heap.add(stones[i]);
        }

        while(heap.size()>=2){
            int a = heap.poll();
            int b = heap.poll();
            if(a-b>0) heap.add(a-b);
        }
        int ans = 0;
        if(heap.size()==1) ans = heap.poll();

        return ans;
    }
}
