#may2-may9
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		carry = 0
		head = current = ListNode(0)
		while l1 or l2:
			val = carry
			if l1:
				val += l1.val
				l1 = l1.next
			if l2:
				val += l2.val
				l2 = l2.next
			current.next = ListNode(val % 10)
			current = current.next
			carry = val // 10
		if carry > 0:
			current.next = ListNode(carry)
		return head.next				

def getList(l):
	head = ListNode(l[0])
	current = head
	for i in range(1, len(l)):
		current.next = ListNode(l[i])
		current = current.next
	return head

def printList(l):
	head = l 
	while head != None:
		print(head.val)
		head = head.next

x = getList([2,4,3])
y = getList([5,6,4])

s = Solution()
z = s.addTwoNumbers(x, y)
printList(z)