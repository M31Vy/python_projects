class tree_node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print(self):
        print(self.data)

# sorted list => binary search tree (root_node)
# [1,2,3,4,5,6,7,8,9] =>
#              5
#          /       \
#         3         7
#       /  \      /  \
#      2    4    6    8
#     / .              \
# .  1 .                9
# O(n)

def convert_sorted_list_to_binary_search_tree(A):
    if not A:
        return None
    else:
        mid = int(len(A)/2)
        left = convert_sorted_list_to_binary_search_tree(A[:mid])
        right = convert_sorted_list_to_binary_search_tree(A[mid+1:])
        return tree_node(A[mid], left, right)

def depth_first_traversal_inorder(root_node):  #in-order, pre-order, post-order
    if root_node:
        depth_first_traversal_inorder(root_node.left)
        print(root_node.data)
        depth_first_traversal_inorder(root_node.right)

B = [1,2,3,4,5,6,7,8,9,10]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
depth_first_traversal_inorder(B_node)

B = [3]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
depth_first_traversal_inorder(B_node)



# sorted list => binary search tree (root_node)
# [1,2,3,4,5,6,7,8,9] =>
#              5
#          /       \
#         3         8
#       /  \      /  \
#      2    4    7    9
#     / .       /
# .  1 .       6
# Queue [5], [3,7], [7, 2, 4], [2, 4, 6, 8], [4, 6, 8, 1], [6, 8, 1], [8, 1], [1, 9], [9], []
# print      5,     3,         7,             2,            4 .       6,      8,       1,   9
def width_first_traversal(root_node):
    if not root_node:
        return
    queue = [root_node]
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# B = [1,2,3,4,5,6,7,8,9]
# print(B)
# B_node = convert_sorted_list_to_binary_search_tree(B)
# width_first_traversal(B_node)

# B = [3]
# print(B)
# B_node = convert_sorted_list_to_binary_search_tree(B)
# width_first_traversal(B_node)

def is_binary_search_tree_2(root_node):
    if not root_node:
        return [True, None, None]

    ans = [True, root_node.data, root_node.data]
    if root_node.left:
        ans_left = is_binary_search_tree_2(root_node.left)
        if not ans_left[0] or root_node.data < ans_left[2]:
            return [False, None, None]
        ans = [True, ans_left[1], root_node.data]

    if root_node.right:
        ans_right = is_binary_search_tree_2(root_node.right)
        if not ans_right[0] or root_node.data > ans_right[1]:
            return [False, None, None]
        ans = [True, ans[1], ans_right[2]]

    return ans


B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
print(is_binary_search_tree_2(B_node))

B = [3]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
print(is_binary_search_tree_2(B_node))

print(is_binary_search_tree_2(None))

B = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
print(B)
B_node = convert_sorted_list_to_binary_search_tree(B)
print(is_binary_search_tree_2(B_node))