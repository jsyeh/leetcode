class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(stones.length, new Compare());
        for(int i=0; i<stones.length; i++){
            heap.offer(stones[i]);
        }

        while(heap.size()>1) {
            int a = heap.poll();
            int b = heap.poll();
            if(a-b!=0) heap.offer(a-b);
            //System.out.println(heap);
        }
        if(heap.size()==0) return 0;
        return heap.poll();
    }
}
class Compare implements Comparator<Integer> {
    public int compare(Integer a, Integer b){
        return b-a;
    }
}//Case3: [2,2]
