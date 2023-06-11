//lee215使用TreeMap<Integer,Integer>[] 很帥，不過我已經用 HashMap 配 ArrayList
//頭洗下去了，只好硬做下去。只是在 ArrayList 的 Binary Search 要怎麼做呢？
//不過在 int result = Collections.binarySearch(list, snap_id, new SnapCompare()); 這行遇到問題
class SnapshotArray {
    int snapID = 0;
    int N = 0;
    int[] snapshot;
    HashMap<Integer, ArrayList<int[]>> history; //某個位置，全部的修改記錄，配合binary search
    //HashMap<Integer, Boolean> modified = new HashMap<>(); //會超時
    TreeMap<Integer,Boolean> modified = new TreeMap<>();
    //利用 HashMap 快速找到
    public SnapshotArray(int length) {
        N = length;
        snapshot = new int[length];
        history = new HashMap<>();
        //hisotry.get(id) 會得到 ArrayList,
    }
    
    public void set(int index, int val) {
        snapshot[index] = val;
        modified.put(index, true);
//for(int i=0; i<N; i++){
//System.out.print(snapshot[i] + " ");
//}
//System.out.println(" set()");
    }
    
    public int snap() { //不適合在snap()把全部值存起來，因memory用太大
        //在snap()時，把每個數字都巡一次，清好這次id
//System.out.println("snap:"+snapID);

        //for(int i=0; i<N; i++){ //這裡也可能超時。改寫。程式變複雜了
//            if(modified.containsKey(i)){
        for(Map.Entry<Integer,Boolean> entry : modified.entrySet()){
            int i = entry.getKey();
//System.out.println("modify:" + i);
                ArrayList<int[]> list;
                if(history.containsKey(i)){
                    list = history.get(i);
                } else list = new ArrayList<int[]>();
                int[] one = {snapID, snapshot[i]};
                list.add(one);
                history.put(i, list);
            //}
        }
        modified.clear(); //是這行超時嗎？ 果然！ 別用 HashMap 改用TreeMap
        //https://www.quora.com/Java-Why-does-clear-on-a-HashMap-take-O-n-time-while-clear-on-a-TreeMap-takes-only-O-1-time

        return snapID++;
    }
    
    public int get(int index, int snap_id) {
        ArrayList<int[]> list = history.get(index);
        if(list==null) return 0;
        //int result = Collections.binarySearch(list, snap_id, new SnapCompare()); //這行遇到問題
        //if(result<0) return list.get(-result)[1];
        //else return list.get(result)[1];
        int left=-1, right=list.size(), ans = -1;
        while(left+1<right){
            int mid = (left+right)/2;
//System.out.println("left:"+left + " mid:" + mid + " right: " + right);
            if(list.get(mid)[0]==snap_id) {
                left = mid;
                ans = mid;
                break;
            } else if(list.get(mid)[0]<snap_id) {
                left = mid;
            } else right = mid;
        }
//System.out.println("get() "+index+" snap_id:"+snap_id + " left:"+left + " ans:"+list.get(left)[1]);
        if(left==-1) return 0; //最前面的版本沒找到，就0
        else return list.get(left)[1];
    }
}
//case 9/74: ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
//[[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
//這裡遇到的問題，是snap很多次後，後面其實是空的。
//case 35/74: ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
//[[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
//case 67/74: 有大量input會超時 10000筆
//case 69/74: 就算 System.out.print()都註解掉，有大量input還是會超時 50000筆

//https://www.geeksforgeeks.org/comparator-interface-java/
//class SnapCompare implements Comparator<int[]> {
//    public int compare(int[] a, int[] b)
//    {
//        return a[0] - b[0];
//    }
//}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
