/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {

    //List<NestedInteger> all;
    //int used = 0;
    Queue<Integer> ans = new LinkedList<>();
    public NestedIterator(List<NestedInteger> nestedList) {
        //all = nestedList;
        //used = 0;
        helper(nestedList);
    }
    void helper(List<NestedInteger> nestList) {
        for(NestedInteger next : nestList) {
            if(next.isInteger()){
                ans.offer(next.getInteger());
            }else helper(next.getList());
        }
    }

    @Override
    public Integer next() {
        return ans.poll();
        //NestedInteger now = all.get(used);
        //if(now.isInteger()){
            //Integer ans = now.getInteger();
            //used++;
            //return ans;
        //} else { //它是 NestedInteger, 不是Integer
            //List<NestedInteger> temp = now.ngetList();
            //if(!now.hasNext()) used++;
            //return temp;
        //}
    }

    @Override
    public boolean hasNext() {
        return ans.size()>0;
        //if(used>=all.size()) return false; //超過了
        //else if(used<all.size()-1) return true; //還有剩
        //else { //剛好是最後一道
            //NestedInteger now = all.get(used);
            //if(now.isInteger())
            //if(now.hasNext()) return true;
            //else return false;
        //} 
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
