class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((a,b)->b-a);
        for(int i=0; i<nums.length; i++){
            heap.offer(nums[i]);
        }
        int ans=0;
        for(int i=0; i<k; i++){
            ans = heap.poll();
        }
        return ans;
    }
}
