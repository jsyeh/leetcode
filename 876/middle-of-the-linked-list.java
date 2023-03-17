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
    public ListNode middleNode(ListNode head) {
        int N=0;
        ListNode now = head;
        while(now!=null){
            now = now.next;
            N++;
        }
        now = head;
        for(int i=0; i<N/2; i++){
            now = now.next;
        }
        return now;
    }
}
