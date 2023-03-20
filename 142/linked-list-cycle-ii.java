/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    Map<ListNode,Integer> map;
    public ListNode detectCycle(ListNode head) {
        map = new HashMap<ListNode, Integer>();
        ListNode now = head;
        while(now!=null){
            if(map.containsKey(now)) return now;
            map.put(now, 0);

            now = now.next;

        }
        return null;
    }
}
