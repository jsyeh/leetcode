/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left=1, right=n;
        while(left<right){
            int mid = (int)((left+(long)right)/2);
            if(isBadVersion(mid)){
                right=mid;
            }else{
                left=mid+1;//再多走進一點
            }
        }
        return left;
    }
}//case3: 2126753390 1702766719
