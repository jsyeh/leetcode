class SnapshotArray {
    ArrayList<int[]> [] history;
    int snapID = 0;
    public SnapshotArray(int length) {
        history = new ArrayList[length];
        for(int i=0; i<length; i++) {
            history[i] = new ArrayList<>();
            int[] a = {0, 0};
            history[i].add(a);
        }
    }
    
    public void set(int index, int val) {
        int [] a = {snapID, val};
        history[index].add(a);
    }
    
    public int snap() {
        snapID++;
        return snapID - 1;
    }
    
    public int get(int index, int snap_id) {
        ArrayList<int[]> now = history[index];
        int left = 0, right = now.size();
        while(left<right) {
            int mid = (left+right)/2;
            if(now.get(mid)[0]<=snap_id) {
                left = mid + 1;
            }else{
                right = mid;
            }
        }
//        for(int[] a : now){
//            System.out.println(a[0] + "," + a[1]);
//        }
        System.out.println("left:"+left);
//        System.out.println("snap_id:"+snap_id);
        return now.get(left-1)[1];
    }
}
//case 9/74: ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
//[[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
//這裡遇到的問題，是snap很多次後，後面其實是空的。
//case 35/74: ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
//[[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
//case 67/74: 有大量input會超時 10000筆
//case 69/74: 就算 System.out.print()都註解掉，有大量input還是會超時 50000筆
/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
