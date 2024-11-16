// LeetCode 147. Insertion Sort List
// 把 head 裡的每一個 node，照「小到大」的方式，回傳 linked list
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* ans = new ListNode();
        while(head!=nullptr){ // 每次挑1個node處理
            ListNode* now = ans;
            while(now->next != nullptr && now->next->val < head->val){
                now = now->next; // 只要 now 的下一個 node還有，且太小，就往右移
            } // 所以離開迴圈時，就代表「找到合適的插入點」
            now->next = new ListNode(head->val, now->next); // 插入
            head = head->next;
        }
        return ans->next;
    }
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
