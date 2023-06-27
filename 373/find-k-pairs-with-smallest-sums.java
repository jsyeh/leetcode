class Solution {
    //public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
    //    List<List<Integer>> ans = new ArrayList<List<Integer>>();
        //就把最小的數,慢慢增加,但這個方法是錯的，因為沒有把全部可能走法照小到大的優先順序走完
        //for(int i1=0, i2=0, ii=0; i1<nums1.length && i2<nums2.length && ii<k;  ii++) {
        //    List<Integer> temp = new ArrayList<>();
        //    temp.add(nums1[i1]);
        //    temp.add(nums2[i2]);
        //    ans.add(temp);
            //if(nums1[i1]<=nums2[i2] && i1<nums1.length+1) i1++;
            //else if(i2<nums2.length+1) i2++;
        //}
        //看了別人的解法 Editorial 及 bbccyy1 後，突然有靈感，就簡單的PriorityQueue
    //    return ans;
    //}
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b)->a[0]-b[0]); //意思是 a的和 要比 b的和 小，就會先出來

        for(int i=0; i<nums1.length; i++){
            queue.offer(new int[]{nums1[i]+nums2[0], 0});
            //照著Solution的解法，先把 nums2[0] vs. 全部的nums1[i]全算好答案、送到priority queue裡，再照著 sum 的大小來送出
            //右邊存 nums2 的 index,因為之後會逐步提昇
        }

        for(int kk=0; kk<k && queue.size()>0 ; kk++){//逐步取出答案
            int [] SumPos = queue.poll();
            int sum = SumPos[0], pos = SumPos[1];
            int n2 = nums2[pos], n1 = sum - n2; //還原n1,n2
            List<Integer> temp = new ArrayList<>();
            temp.add(n1);//還原回原本nums1[i]
            temp.add(n2);//還原回原本nums2[i]
            ans.add(temp);//找到一組最小的答案

            if(pos < nums2.length-1) {
                queue.offer(new int[]{n1+nums2[pos+1], pos+1});
                //nums2[] 的 index 再下一個
            }
        }
        return ans;
    }
}
