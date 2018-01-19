# Leetcode: Merge Two Sorted Lists     :BLOG:Basic:


---

Merge Two Sorted Lists  

---

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.  

Example:  

Input: 1->2->4, 1->3->4  
Output: 1->1->2->3->4->4  

Blog link: <http://brain.dennyzhang.com/merge-two-sorted-lists>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def mergeTwoLists(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            ## Basic Idea:
            ##    l1: 1 -> 3 -> 5
            ##        p   r
            ##    l2: 2 -> 3 -> 6 -> 7
            ##        q   s
            ## Complexity:
            ## recursive
            if l1 is None:
                return l2
    
            if l2 is None:
                return l1
    
            if l1.val < l2.val:
                head = l1        
                p = l1
                q = l2
            else:
                head = l2
                p = l2
                q = l1
    
            while (p.next is not None) and (q is not None):
                r = p.next
                s = q.next
                if q.val <= r.val:
                    p.next = q
                    q.next = r
                    p = q
                    q = s
                else:
                    p = r
    
            if p.next is None:
                p.next = q
    
            return head