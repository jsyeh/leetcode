class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int N1=1;
        for(int i=1; i<nums1.length; i++){
            if(nums1[N1-1]==nums1[i]) continue;
            else nums1[N1++] = nums1[i];
        }

        int N2=1;
        for(int i=0; i<nums2.length; i++){
            if(nums2[N2-1]==nums2[i]) continue;
            else nums2[N2++] = nums2[i];
        }
/*for(int i=0; i<N1; i++){
    System.out.print(" "+nums1[i]);
}
System.out.println();
for(int i=0; i<N2; i++){
    System.out.print(" "+nums2[i]);
}
System.out.println();*/

        List<Integer> list1 = new ArrayList<Integer>();
        List<Integer> list2 = new ArrayList<Integer>();

        for(int i1=0, i2=0; i1<N1 && i2<N2; ) {
            if(nums1[i1]==nums2[i2]){
                i1++;
                i2++;
            }else if(nums1[i1]<nums2[i2]){
                list1.add(nums1[i1]);
                i1++;
            }else if(nums1[i1]>nums2[i2]){
                list2.add(nums2[i2]);
                i2++;
            }

            if(i1==N1){//num1[i1] 走到盡頭,就把num2[i2]全部加進去
                for(int i=i2; i<N2; i++) list2.add(nums2[i]);
            }
            if(i2==N2){//num2[i2] 走到盡頭,就把num1[i1]全部加進去
                for(int i=i1; i<N1; i++) list1.add(nums1[i]);
            }
        }

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        ans.add(list1);
        ans.add(list2);
        return ans;
    }
}
// case 2/202: [-68,-80,-19,-94,82,21,-43]
//[-63]
