/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        ListNode sz = head;
        int len = 0;
        while (sz != null) {
            len += 1;
            sz = sz.next;
        }
        if (len == n) {
            return head.next;
        }

        ListNode rm = head;
        for (int i = 1; i < len - n; i++) {
            rm = rm.next;
        }
        ListNode temp = rm.next;
        rm.next = temp.next;
        return head;
    }
}
