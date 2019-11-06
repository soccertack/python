class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    if not root:
        return None

    stack = []
    stack.append(root)
    visited = set()
    res = []

    while stack:
        n = stack.pop()
        has_child_to_visit = False

        #print "pop and at", n.val
        for child in [n.left, n.right]:
            if not child:
                continue
            if child not in visited:
                visited.add(child)
                stack.append(n)
                stack.append(child)
                #print "push child", child.val, "from ", n.val
                has_child_to_visit = True
                break

        if not has_child_to_visit:
            #print "done node", n.val
            res.append(n.val)

    return res

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

tree = '[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]'

root = deserialize(tree)
ret = postorderTraversal(root)
print ret
