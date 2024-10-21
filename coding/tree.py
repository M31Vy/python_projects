def add_func(var1, var2=0):
  return var1 + var2

ans = add_func(1, 2)
print(ans)

ans = add_func(1)

# [] 0 None '' == False


class tree_node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def display(self):
    print(self.data)

class child_tree_node(tree_node):
  def __init__(self, data, tag, left=None, right=None):
    super().__init__(data, left, right)
    self.tag = tag


  def display(self):
    if self.left:
      print(self.left.data)

node1 = tree_node(2)
node2 = tree_node(4)
root_node = tree_node(0, node1, node2)
node1.display()

node_child = child_tree_node(0, 'this is child node', node2)
node_child.display()