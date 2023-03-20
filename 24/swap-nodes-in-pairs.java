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
    public ListNode swapPairs(ListNode head) {
        ListNode head2 = new ListNode();
        ListNode node = head;
        ListNode node2 = head2;
        
        while(node!=null && node.next!=null) {
            ListNode n1 = new ListNode(node.val);
            ListNode n2 = new ListNode(node.next.val);
            n2.next = n1;
            node2.next = n2;
            node = node.next.next;
            node2 = node2.next.next;
        }
        if(node!=null) {
            node2.next = new ListNode(node.val);
        }
        return head2.next;
    }
}
