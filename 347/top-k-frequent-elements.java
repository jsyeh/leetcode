class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i], map.get(nums[i])+1);
            }else map.put(nums[i], 1);
        }

        PriorityQueue<int[]>heap = new PriorityQueue<int[]>( (a,b)->b[1]-a[1]);
        for(Integer key : map.keySet()){
            int [] temp = {key, map.get(key)};
            heap.offer(temp);
        }

        int [] ans = new int[k];
        for(int i=0; i<k; i++){
            ans[i] = heap.poll()[0];
        }
        return ans;
    }
}
