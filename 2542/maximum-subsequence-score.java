class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int N = nums1.length;
        //挑k組資料,num1加起來, 乘num2最小值。數字很多, 無法用暴力法        
        int[][] all = new int[N][2];
        for(int i=0; i<N; i++){
            all[i][0] = nums1[i];
            all[i][1] = nums2[i];
        }

        Arrays.sort(all, (a,b)->(b[1]-a[1]));
//Q:若nums2[i] 相等時,要再比對nums1[i]呢? A: 不用
        //for(int i=0; i<N; i++){
        //    System.out.print(" "+all[i][1]);
        //}

        PriorityQueue<Integer> topK = new PriorityQueue<>(k, (a,b)->(a-b) );
        //會放前k大的值,每次吐出裡面最小的值,以便最取代換另一個值

        //找到前k項的和,與最小的nums2[i] 的值
        long sum = 0;
        for(int i=0; i<k; i++){
            topK.add(all[i][0]);//把 nums1[i] 前k項加進來
            sum += all[i][0];//把 nums1[i] 前k項加進來
        }
        long ans = sum * all[k-1][1];//前k項的nums[i], 配上最小的 nums2[k-1], 先當一開始的答案

//Q:我有個疑問,因為什麼從第k個繼續,那 nums2[1]...nums2[k-1]是否都漏算了? 
//A:因為找nums2[i]最小值, 所以只要用 nums[k-1]...nums2[n-1] 即可, nums[0]...nums[k-2] 都太大,就忽略吧
        for(int i=k; i<N; i++) {//接下來持續更新答案
            sum -= topK.poll();//丟掉K個中,最小的數
            sum += all[i][0];//抽換下一個數
            topK.add(all[i][0]);//topK 也更新

            long temp = sum * all[i][1];//現在的組合結果
            if(temp>ans) ans = temp;//如果更, 那換新的答案
        }

        //在迴圈裡,每次丟掉 heap 最小的, 再把現在的 nums1[i] 加進去,以便隨時有最大的sum
        return ans;
    }
}
