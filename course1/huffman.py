input_data = 'BCAADDCAADDDEAABB'

import time
start_time = time.perf_counter()

class Node(object):

    def __init__(self,left_node = None,right_node = None):
        self.left_node = left_node
        self.right_node = right_node

    def children(self):

        return (self.left_node,self.right_node)

    def nodes(self):

        return (self.left_node,self.right_node)
    
    def __str__(self):
        return ("%s%s" %(self.left_node,self.right_node))
    
def huffman(node,left_node = True,binString = ''):
    if type(node) is str:
        return {node: binString}
    (l,r) = node.children()
    d = dict()
    d.update(huffman(l,True,binString + '0'))
    d.update(huffman(r,False,binString + '1'))
    return d    


freq = {}
for c in input_data:
    freq[c] = freq.get(c, 0) + 1


freq = sorted(freq.items(),key = lambda x: x[1],reverse=True)
nodes = freq

while len(nodes) > 1:
    (key1,c1) = nodes[-1]
    (key2,c2) = nodes[-2]
    nodes = nodes[:-2]
    node = Node(key1,key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes,key = lambda x: x[1],reverse=True)

huffman_code = huffman(nodes[0][0])

for (char,frequency) in freq:
    print('%-4r | %12s' %(char,huffman_code[char]))

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\nelapsed time: {elapsed_time:.10f}")


