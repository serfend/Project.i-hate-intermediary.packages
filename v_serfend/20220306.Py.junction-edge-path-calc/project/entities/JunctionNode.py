from entities.Edge import Edge


class JunctionNode:
    id = 0  # 节点序号
    x = 0  # x坐标
    y = 0  # y坐标
    key = 0  # 关键节点：0否，1是
    Di = 0  # Damage值
    Ti = 0  # 交叉口信号周期
    Li = 0  # 交叉口直行绿信比
    Ci = 0  # 交叉口直行通行能力
    land_use = 0  # 土地利用：1住宅商用，2其他
    connected_edges = None  # 相连的边，需要通过Edge的s_id和e_id去map
    child_nodes = None  # 所有分裂节点
    directions = None  # 所有的可用转向
    result = 0 # 计算的Tid值

    def __init__(self):
        self.connected_edges = []
        self.child_nodes = []
        self.directions = []
        pass

    def add_child_node(self, id):
        self.child_nodes.append(id)

    def add_edge(self, edge):
        self.connected_edges.append(edge)

    def add_direction(self, direction):
        self.directions.append(direction)

    # 检查当前节点连接的边
    # 检查当前节点包含的可用方向
    def generate_edge_with_direction(self):
        direction_list = [[1, 1.5], [2, 1.0], [3, 0.2]]
        result = []
        for direction in self.directions:
            dir_item = direction.s_dir
            for d in direction_list:
                if not dir_item & d[0]:
                    continue
                e = Edge()
                e.id = f'{self.id}_{direction.e_id}_{d[0]}'
                e.result = d[1] * self.result # yita · Tid
                result.append(e)
        return result

    # 该方法暂时不实现，使用人工标注方向的方法实现
    # # 根据child_nodes，创建子边（0-6条），并赋不同的yita返回delay
    # # 需要判断左转直行右转（生成0-3种）
    # # 需要判断是否是双向行驶（生成1-2种）
    # #      2\
    # #   -1-- · -3--
    # #        4\
    # # 左转 12,23,34,41 yita=1.5
    # # 右转 14,21,32,43 yita=0.3
    # # 直行 13,24,31,42 yita=1.0
    # def generate_child_edge(self):
    #     result = []
    #     for edge in self.connected_edges:
    #         both_direction = edge.dir == 0 # 是否允许双向行驶
    #         is_end = edge.e_id == self.id # 当仅允许单行时，当前节点是否是end_node
    #         if not both_direction and is_end:
    #             result.append(self.)
    #     pass

    # 该方法暂时不实现，通过预定义北向道路为id=1，东向道路为id=2从而固定了车子视角
    # # 通过边和点的关系计算得到司机视角的真实child_nodes_id
    # # 例如从北方来的车，则北方为child_id=1，即原来id=2的child_node变更为了id=1
    # def get_user_view_id(self,edge):
    #     s_x = edge._s_node.x
    #     s_y = edge._s_node.y
    #     e_x = edge._e_node.x
    #     e_y = edge._e_node.y
    #     pass

    @property
    def max_edge_length(self):
        return max([x.length for x in self.connected_edges])

    @staticmethod
    def mapper():
        return {
            'λi': 'Li'
        }


a = JunctionNode()
print(a.__dict__)
