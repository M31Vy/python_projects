# 用邻接矩阵实现（不容易增加顶点，不包含增加顶点的代码）
class Graph(object):
    def __init__(self, mat, unconn=0):      # mat表示初始的邻接矩阵，是一个给定矩阵，是一个二维的表，提供图的基本框架，确定图顶点的个数
        vnum = len(mat)     # 确定邻接矩阵中顶点的个数,相当于行数
        for x in mat:       # 取出一行列表。看看里面的顶点个数是不是等于vnum，即确定二维表是不是一个方阵
            if len(x) != vnum:      # 列数不等于行数
                raise ValueError("参数错误，不是方阵，行数不等于列数！")
        self._mat = [mat[i][:] for i in range(vnum)]     # 将初始的邻接矩阵拷贝一份，mat[i][:]代表第i行的所有元素
        self._unconn = unconn       # unconn表示两节点之间无边，矩阵中默认用0
        self._vnum = vnum

    def vertex_num(self):       # 返回顶点的个数
        return self._vnum

    def _invalid(self, v):      # 检查顶点是否有效，若无效返回True
        if v < 0 or v > self._vnum:
            print("无效顶点！")


    def add_edge(self, vi, vj, val="1"):      # 在顶点vi，vj中间加入边，就相当于在二维矩阵中vi行vj列处的值为字符串1
        if self._invalid(vi) or self._invalid(vj):      # 检查是否为有效顶点
            raise ValueError("无效顶点！")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):      # 检查是否为有效顶点
            raise ValueError("无效顶点！")
        return self._mat[vi][vj]

    def get_out_edge(self, vi):     # 获得顶点vi的出边
        if self._invalid(vi):
            raise ValueError("无效顶点！")
        return self._out_edge(self._mat[vi])      # self._mat[vi]列表里存放的是与vi顶点相连的顶点


    def _out_edge(self, row):       # get_out_edge函数调用_out_edge函数
        edges = []      # 构造一个新列表用于存放与顶点vi具有相连关系的顶点之间的边
        for i in range(len(row)):
            if row[i] != "0":        # 与vi相连的顶点，即二维矩阵中vi行的值不为0,注意这里的0是字符串0，因为后面二维表里面的值都转换成字符串了
                edges.append((i, row[i]))       # vi的出边用（v,w）表示，v表示与vi相连的顶点的下标值，w表示两顶点之间的边
        return edges

    def __str__(self):      # 修改python内置的字符串str函数
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]"      # map函数将str作用于self._mat的每一个元素，再用join以“,\n”为分隔符，将vnum个一维列表连接起来并每个列表生成一行

lst = [['0', '0', '1', '0'],['0', '0', '1', '1'],['1', '1', '0', '1'],['1', '0', '1', '0']]

# 测试
g = Graph(lst)
print(g)        # 打印邻接矩阵
print(g.vertex_num())       # 打印出顶点的个数
g._invalid(6)        # 检查顶点所对应的下标是否超界，即顶点是否有效
print(g.get_out_edge(0))        # 打印第一个顶点的出边
g.add_edge(0, 1)    # 在第1个顶点(行标是0)和第2个顶点（列标是1）之间加入一条边，并打印出邻接矩阵查看效果
print(g)