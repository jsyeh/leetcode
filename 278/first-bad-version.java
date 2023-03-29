/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return check(1, n);
    }
    // good good bad
    // bad bad bad (return i)
    // good bad bad (return check(i, mid))
    // good good bad (return check(mid, i))
    //
    int check(int i, int j) {
        if(i==j) return i;
        if(i+1==j){
            if(isBadVersion(i)) return i;
            if(isBadVersion(j)) return j;
            return j;
        }
        long ii=i;
        ii += j;
        ii /= 2;
        int mid = (int) ii;
        boolean a = isBadVersion(i);
        boolean b = isBadVersion(mid);
        boolean c = isBadVersion(j);
        if(a) return i;
        if(!a && b) return check(i, mid);
        else return check(mid, j);
    }
}//Case3: 2126753390
//1702766719 因為相加之後是 long long, 所以爆炸了
