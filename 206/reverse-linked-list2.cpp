// LeetCode 206. Reverse Linked List
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head==nullptr || head->next==nullptr) return head; // 終止條件

        ListNode* ans = reverseList(head->next); // 右邊反過來的答案

        head->next->next = head; // 看左圖, 1的下一個是2,的下一個,要指回1
        head->next = nullptr; // 接下來, 1的下一個要收起來

        return ans;
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
