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
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null) return null;
        ListNode ans = new ListNode();
        ListNode now = ans;
        int dupN=1;
        while(head!=null && head.next!=null) {
            if(head.val != head.next.val) {
                if(dupN==1){
                    now.next = new ListNode(head.val);
                    now = now.next;
                }
                dupN = 1;
            } else {
                dupN++;
            }
            head = head.next;
        }
        if(dupN==1){
            now.next = new ListNode(head.val);
        }
        return ans.next;
    }
}
