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
        int N=0;
        ListNode temp = head;
        while(temp!=null){
            temp = temp.next;
            N++;
        }
        System.out.println(N);
        temp = head;
        if(N==n){
            head=head.next;
            return head;
        }
        for(int i=0; i<N-n-1; i++) {
            temp = temp.next;
        }
        temp.next = temp.next.next;
        return head;
    }
}//case 4: [1,2] 2
