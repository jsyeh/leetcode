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
    public ListNode reverseList(ListNode head) {
        ListNode ans = new ListNode();
        ListNode now = ans;
        while(head!=null) {
            now.next = new ListNode(head.val, now.next);
            head = head.next;
        }
        return ans.next;
    }
}
