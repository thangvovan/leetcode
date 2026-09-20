from dataStructures.LinkedList import ListNode

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head == None:
            return False

        stack = []

        node = head
        while node != None:
            stack.append(str(node.val))
            node = node.next

        s = "".join(stack)
        return s == s[::-1]