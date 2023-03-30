/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head==null) return null;
        ArrayList<Integer> array = new ArrayList<Integer>(20000);

        int N=0;
        while(head!=null){
            array.add(head.val);
            head = head.next;
            N++;
        }
/*        int [] nums = new int[N];
        for(int i=0; i<N; i++){
            nums[i] = head.val;
            head = head.next;
        }*/
        return genTree(array, 0, N);
    }
    TreeNode genTree(ArrayList<Integer> array, int i, int j) { //右邊j不包含
        if(i>=j) return null;
        int mid = (i+j)/2;
        TreeNode ans = new TreeNode(array.get(mid));
        ans.left = genTree(array, i, mid);
        ans.right = genTree(array, mid+1, j);
        return ans;
    }
}
