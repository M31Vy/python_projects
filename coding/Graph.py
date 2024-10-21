class graph_node(object):
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
        self.visited = False

    def print(self):
        print(self.data)

def depth_first_traversal(node):
    if node:
        node.visited = True
        print(node.data)
        # for child in node.children:
        #     if not child.visited:
        #         child.visited = True
        #         depth_first_traversal(child)

        for i in range(len(node.children)):
        #     node.children[i].visited = True
            if not node.children[i].visited:
                depth_first_traversal(node.children[i])

def width_first_traversal(node):
    if not node:
        return
    node.visited = True
    queue = [node]
    while queue:
        node_2 = queue.pop(0)
        print(node_2.data)
        for child in node_2.children:
            if not child.visited:
                child.visited = True
                queue.append(child)

def minimum_distance(node_A, node_B):
    if not node_A:
        return -1
    queue = [(node_A,0)]
    while queue:
        node_2,distance = queue.pop(0)
        if node_2 == node_B:
            return distance
        for child in node_2.children:
            if not child.visited:
                child.visited = True
                # 注意下面的这种写法可以很好的解决distance可能会在循环中被修改的问题。
                queue.append((child,distance+1))
    return -1

A = graph_node(1)
B = graph_node(2)
C = graph_node(3,[A,B])
D = graph_node(4,[C,B])
A.children.append(D)
# width_first_traversal(D)
depth_first_traversal(D)
# print(minimum_distance(D,B))

a = [(1,2),(2,3)]
b = set(a)
print(b)