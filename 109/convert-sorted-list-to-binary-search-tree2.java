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

        ListNode now = head;
        int N=0;
        while(now!=null){
            N++;
            now = now.next;
        }

        int [] nums = new int[N];
        for(int i=0; i<N; i++){
            nums[i] = head.val;
            head = head.next;
        }
        return genTree(nums, 0, N);
    }
    TreeNode genTree(int[] nums, int i, int j) { //不包含右邊的j
        if(i>=j) return null;
        int mid = (i+j)/2;
        TreeNode ans = new TreeNode(nums[mid]);
        ans.left = genTree(nums, i, mid);
        ans.right = genTree(nums, mid+1, j);
        return ans;
    }
}
