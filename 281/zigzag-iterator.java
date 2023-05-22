public class ZigzagIterator {
    LinkedList<Integer> z1;
    LinkedList<Integer> z2;
    int pt = 1; //1: z1, 2: z2, pt = 3 - pt;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        z1 = new LinkedList(v1);
        z2 = new LinkedList(v2);
    }

    public int next() {
        if(z1.size()==0) pt = 2;

        if(pt==1){
            if(z2.size()>0) pt = 2;
            return z1.poll();
        }else{
            if(z1.size()>0) pt = 1;
            return z2.poll();
        }
    }

    public boolean hasNext() {
        if(z1.size()>0 || z2.size()>0) return true;
        else return false;
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */
