class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        //因為 10^5 如果兩層迴圈就會超時，所以不能用暴力法模擬
        //我本來以為「面試過的人就不能再面試」，不過好像可一直重覆面試
        //所以看了Editorial 的解法，使用Priority Queue會很適合
        PriorityQueue<Integer> first = new PriorityQueue<>();
        PriorityQueue<Integer> last = new PriorityQueue<>();
        int N = costs.length;
        int next1 = candidates; //頭的下一位
        int next2 = N-1-candidates; //尾的下一位
        //在模擬時，要保證 next1<=next2 不然就終局/殘局，不能再補人了
        if(costs.length>candidates*2) { 
            //有夠多人，可以頭尾都挑好 candidates 個人待合做
            for(int i=0; i<candidates; i++){
                first.offer(costs[i]);
                last.offer(costs[N-1-i]);
            }

        } else { //人不夠分成兩群面試，所以全部人都放入 first 的 PriorityQueue
            for(int i=0; i<costs.length; i++) {
                first.offer(costs[i]);
            }
        }

        long ans = 0; //totalCost
        for(int i=0; i<k; i++) { //要陸續錄取k位員工
            if(first.size()>0 && last.size()>0) { //兩個都要測
                if(first.peek()<=last.peek()) { //要改成<= 都優先用Fist
                    ans += first.poll();
                    //上面是挑好人，下面是若可補人就補人
                    if(next1<=next2) first.offer(costs[next1++]);
                } else {
                    ans += last.poll();
                    //上面是挑好人，下面是若可補人就補人
                    if(next1<=next2) last.offer(costs[next2--]);
                }
            } else if(first.size()>0 ){
                ans += first.poll();
                //上面是挑好人，下面是若可補人就補人
                if(next1<=next2) first.offer(costs[next1++]);
            } else {
                ans += last.poll();
                //上面是挑好人，下面是若可補人就補人
                if(next1<=next2) last.offer(costs[next2--]);
            }
        }

        return ans;
    }
}
//下方測資會出錯，可能是人數太多，讓ans 超過 int 所以要改成 long 
//case 156/160: 超多數字,讓答案太大,要改用 long 長整數
//52220
//725
//case 158/160: [10,1,11,10]
//2
//1
