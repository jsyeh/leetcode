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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int len = findLength(head);
        ListNode ans = new ListNode(0, head);
        ListNode node=ans;
        for(int i=0; i<len-n+1; i++){
            node = node.next;
        }
        node.next = node.next.next;
        return ans.next;
    }
    int findLength(ListNode head) {
        if(head.next==null) return 0;
        return 1+findLength(head.next);
    }
}
