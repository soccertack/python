
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(root):

    while root:
        print (root.val)
        root = root.next

#Alway return two arrays
# One: a pointer to the reversed first half
# Two: a pointer to the original second half
def get_mid_list(root):

    if not root.next:
        return root, root

    f = root.next.next
    next_head = root.next
    root.next = None

    # root is the start of the reversed list
    # slow_head is the start of the second list
    while f:
        curr_head = next_head
        next_head = next_head.next

        f = f.next
        if not f:
            break

        curr_head.next = root
        root = curr_head

        f = f.next

    return root, next_head

def reverse_list(root):

    if not root.next:
        return root

    next_head  = root.next
    root.next = None

    # root is the end of the first list
    # next_head is the start of the second list
    while next_head:
        curr_head = next_head
        next_head = next_head.next

        curr_head.next = root
        root = curr_head


    return root

a = Node(10)
b = Node(120)
a.next = b

c = Node(777)
b.next = c

d = Node(8888)
c.next = d

e = Node(99999)
d.next = e

f = Node('aaaa')
e.next = f

print_list(a)

#reversed = reverse_list(a)
#print ('reversed')
#print_list(reversed)

left, right = get_mid_list(a)
print ('split')
print ('left')
print_list(left)
print ('right')
print_list(right)
