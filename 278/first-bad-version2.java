/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return firstBadVersion(1, n);
    }
    int firstBadVersion(int i, int j) {
        //System.out.println(i+" "+j);
        if(i>=j) return i;
        int mid = (int)((i+(long)j)/2);
        if(isBadVersion(mid)) return firstBadVersion(i, mid);
        else return firstBadVersion(mid+1, j);
    }
}//case3: 2126753390 1702766719
