// LeetCode 206. Reverse Linked List
// 換另一種寫法(慢、浪費空間)
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> a; // 「伸縮自如」的陣列
        while (head != nullptr) { // 不是結尾的nullptr
            a.push_back( head->val ); // 塞入「伸縮自如」的陣列
            head = head->next; // 換下一筆
        } // 以上, 把 Linked List 裡面的值, 逐一放入 陣列 a

        ListNode* ans = new ListNode(999); // 答案掛在這裡
        ListNode* now = ans; // 「現在」要處理的 node, 幫忙 ans 收尾
        for (int i=a.size()-1; i>=0; i--) { // 倒過來的迴圈
            now->next = new ListNode( a[i] ); // 建出「新」的node, 接起來
            now = now->next; // 換下一筆
        } // 跟上週的寫法很像
        //return ans; // 錯了!! (上週的學習計畫有發生一樣的事) 要怎麼改呢?????????
        return ans->next; // 真的答案, 是掛在 ans 的右邊下一筆
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
