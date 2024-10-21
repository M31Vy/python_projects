class tree_node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print(self):
        print(self.data)

def convert_sorted_list_to_binary_search_tree(A):
    if not A:
        return None
    else:
        mid = int(len(A)/2)
        left = convert_sorted_list_to_binary_search_tree(A[:mid])
        right = convert_sorted_list_to_binary_search_tree(A[mid+1:])
        return tree_node(A[mid], left, right)



def search_recursive(node, x):
    if not node:
        return False
    if node.data == x:
        return True
    elif node.data > x:
        return search_recursive(node.left, x)
    else:
        return search_recursive(node.right,x)

B = [1,2,3,4,5,6,7,8,9,10]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
print(search_recursive(B_node, 10))

def search_iterative(node, x):
    while node:
        if node.data == x:
            return True
        elif node.data > x:
            node = node.left
        else:
            node = node.right
    return False

print(search_iterative(B_node, 0))