class RandomizedSet {
    ArrayList<Integer> list = new ArrayList<Integer>();
    HashMap<Integer,Integer> map = new HashMap<>();
    public RandomizedSet() {
        
    }
    
    public boolean insert(int val) {
        if(!map.containsKey(val)){
            list.add(val);
            map.put(val, list.size()-1);
            return true;
        }
        return false;
    }
    
    public boolean remove(int val) {
        if(map.containsKey(val)){
            int i = map.get(val);
            map.remove(val);
            if(list.size()>1 && i!=list.size()-1){//這樣就避開問題了！
                map.put(list.get(list.size()-1), i);
                list.set(i, list.get(list.size()-1));
            }
            list.remove(list.size()-1);
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        int i = (int)Math.floor(Math.random()*list.size());
        return list.get(i);
    }
}
//case 4/19: ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
//[[],[0],[0],[0],[],[0],[0]]
//要確認在交換時，如果只剩1個時，是不能再map.put()因為會把待刪的建加回
//case 16/19 有大量的 insert 插入0...4999 再大量 remove
//Index 3358 out of bound for length 2141 表示在 remove 時，有殘留的index出錯
//if(list.size()>1 && i!=list.size()-1){...) 這樣就避開問題了！
/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
