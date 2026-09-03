class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def fbt(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left and node.right:
        return fbt(node.left) and fbt(node.right)
    return False

def pbt(node):
    def depth(n):
        d = 0
        while n:
            d += 1
            n = n.left
        return d

    def is_perfect(n, level, leaf_depth):
        if n is None:
            return True
        if not n.left and not n.right:
            return level == leaf_depth
        if not n.left or not n.right:
            return False
        return (is_perfect(n.left, level + 1, leaf_depth) and
                is_perfect(n.right, level + 1, leaf_depth))

    leaf_depth = depth(node) - 1
    return is_perfect(node, 0, leaf_depth)

def cbt(node):
    if node is None:
        return True

    queue = [node]
    end = False
    i = 0

    while i < len(queue):
        current = queue[i]
        i += 1

        if current.left:
            if end:
                return False
            queue.append(current.left)
        else:
            end = True

        if current.right:
            if end:
                return False
            queue.append(current.right)
        else:
            end = True

    return True

def bbt(node):
    if node is None:
        return True, 0

    lbalanced, lheight = bbt(node.left)
    if not lbalanced:
        return False, 0
    rbalanced, rheight = bbt(node.right)
    if not rbalanced:
        return False, 0

    if abs(lheight - rheight) > 1:
        return False, 0

    return True, 1 + max(lheight, rheight)



root = Node("R")
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
nodeF.right = nodeH



print("Full binary tree" if fbt(root) else "Not Full binary tree")
print("Perfect binary tree" if pbt(root) else "Not Perfect binary tree")
print("Complete binary tree" if cbt(root) else "Not Complete binary tree")

balanced, _ = bbt(root)
print("Balanced binary tree" if balanced else "Not Balanced binary tree")
