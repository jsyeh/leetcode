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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode next = head;
        ListNode one = head, two = head;
        int N = 0;
        while(next!=null) {
            if(N==k-1) one = next;
            next = next.next;
            N++;
        }
        next = head;
        for(int i=0; i<N-k; i++){
            next = next.next;
        }
        two = next;
        int temp = one.val;
        one.val = two.val;
        two.val = temp;
        return head;
    }
}
