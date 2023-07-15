//根據lee215解釋的解法，主要就一個迴圈，照著 start 日放入event，再去參加「先到期」的活動
class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, (a,b)->a[0]-b[0]);
//for(int[] event : events){ //印出排序的結果，確認有沒有正確排好
//System.out.println(event[0] + " " + event[1]);
//}
        int ans = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>( (a,b)->a-b );
        for(int d=1, i=0; d<=100000; d++) {
            while(i<events.length && d>=events[i][0]) { //有跨起開始的時間，用while確認都送入queue
//System.out.println("day:"+d+" event:" + events[i][0] + " " + events[i][1]);
                queue.offer(events[i++][1]); //就加入一筆，裡是結束的時間
            }
//System.out.println("peek() " + queue.peek());

            while(queue.size()>0 && queue.peek()<d) { //過期的活動，逐一丟掉
                queue.poll();
            }
            if(queue.size()<=0) continue; //queue沒有活動可參加，跳過

            if(queue.peek()>=d){ //將到期的還在合理範圍，順利參加一場活動
                queue.poll();
                ans++;
//System.out.println("ans: " + ans);
            }
        }
        return ans;
    }
}
//case 40/44: [[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],[7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]]
//要調一下程式的順序，讓過期的活動先丟掉，以免塞住
