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
    public ListNode mergeKLists(ListNode[] lists) {
        int N = lists.length;
        if(N==0) return null;
        if(N==1) return lists[0];
        if(N==2) return mergeTwoLists(lists[0], lists[1]);
        
        ListNode [] lists1 = new ListNode[N/2];
        ListNode [] lists2 = new ListNode[N-N/2];
        for(int i=0; i<N/2; i++){
            lists1[i] = lists[i];
        }
        for(int i=0; i<N-N/2; i++){
            lists2[i] = lists[N/2+i];
        }
        return mergeTwoLists( mergeKLists(lists1), mergeKLists(lists2));
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode root = new ListNode();
        ListNode next = root;
        while(true) {
            if(list1==null){
                next.next=list2;
                break;
            }
            if(list2==null){
                next.next=list1;
                break;
            }
            if(list1.val<list2.val){
                next.next = new ListNode(list1.val);
                next = next.next;
                list1 = list1.next;
            }else{
                next.next = new ListNode(list2.val);
                next = next.next;
                list2 = list2.next;
            }

        }
        return root.next;
    }
}
//Case 4: [[1,4,5],[1,3,4]]
//Case 5: [[],[]]
