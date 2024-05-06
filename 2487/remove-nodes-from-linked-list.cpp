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
// LeetCode 2487. Remove Nodes From Linked List
// 給個 Linked List，如果node的右邊有更大的值，就把node刪掉
// 如果右邊有任何人比你大，你就不能存在。使用 mono stack 來解即可。
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        stack<int> mono_stack;  // mono stack, 如果有更大的值，就pop()
        while(head!=nullptr) {
            while(mono_stack.size()>0 && head->val > mono_stack.top()) {  // 更大，要一直清
                mono_stack.pop();  // 更大，要一直清
            }
            mono_stack.push(head->val);  // 清完後, 把現在 head->val 壓進 stack 裡
            head = head->next;  // 換下一筆資料
        }
        ListNode* ans = NULL;  // 再建出 linked list
        while(mono_stack.size()>0) {
            ans = new ListNode(mono_stack.top(), ans);
            mono_stack.pop();
        }
        return ans;
    }
};
