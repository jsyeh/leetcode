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
    public boolean isPalindrome(ListNode head) {
        ListNode head2 = null;
        ListNode now = head;
        ListNode now2 = null;
        while(now != null){
            head2 = new ListNode(now.val, head2);
            now = now.next;
        }
        now = head;
        now2 = head2;
        while(now != null){
            if(now.val!=now2.val) return false;
            now = now.next;
            now2 = now2.next;
        }
        return true;
    }
}
