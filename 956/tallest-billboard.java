//這題應該是用Dynamic Programming
//參考 Editorial 的 Dynamic Programming 解法後，發現 HashMap 很巧妙
//尤其是在 map 更新的部分
class Solution {
    public int tallestBillboard(int[] rods) {
        HashMap<Integer,Integer> map = new HashMap<>();
        //左邊：差距值diff，右邊：最高值taller
        map.put(0, 0); //最簡單的，是taller為0，空無一物, diff也是0

        for(int rod : rods) {
            //如果不加 rod, 也值得放進來。不過還是需要檢查是有 更 taller
            HashMap<Integer,Integer> newMap = new HashMap<>(map);
            //整組map會更新，這是新的map

            //利用迴圈，把map裡的內容都拿出來，產生兩倍的新可能
            for(Map.Entry<Integer,Integer> entry : map.entrySet() ) {
                int diff = entry.getKey();
                int taller = entry.getValue();
                int shorter = taller - diff;
//System.out.println(taller + " " + shorter + " diff:"+diff);

                //把 rod 加到 taller 的話, 是否會讓 diff+taller 對應的taller更高？
                if(newMap.containsKey(diff+rod)){ //若已重覆新的diff值
                    int oldTaller = newMap.get(diff+rod);
                    if(taller+rod > oldTaller) newMap.put(diff+rod, taller+rod);
                    //若能更高，那存新的這筆資料
                } else newMap.put(diff+rod, taller+rod); //沒存過，就理所當然存起來
//System.out.println((taller+rod) + " " + shorter + " diff:"+(diff+rod));
                
                //把 rod 加到 shorter 的話，是否會讓 newDiff 對應的taller更高？
                int newDiff = taller - (shorter+rod);
                if(newDiff<0) {
                    newDiff = - newDiff; //轉成正的 newDiff
                    taller = shorter+rod; //因為taller不夠高，換新的 taller
                    //這裡曾經寫錯，修正即可
                }
                if(newMap.containsKey(newDiff)) {
                    int oldTaller = newMap.get(newDiff);
                    if(taller > oldTaller) newMap.put(newDiff, taller);
                }else newMap.put(newDiff, taller);

//System.out.println((taller) + " " + (taller-newDiff) + " diff:"+(newDiff));

                map = newMap; //新的一輪，就改用新的 newMap
            }
        }
        return map.get(0); //想要一樣長的taller，就查看 diff 是0 對應的 taller
    }
}
//case 64/80: [3,4,3,3,2]
