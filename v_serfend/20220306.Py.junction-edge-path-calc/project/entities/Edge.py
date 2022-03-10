# 道路路段
class Edge:
    name = ''  # 路段名
    id = 0  # 边序号
    length = 0  # 路段长度li
    dir = 0  # 方向：0为双向，1为s→e，2为e→s
    highway = 0  # 道路等级：1快速路，2主干路，3次干路，4支路
    s_id = 0  # 起始节点id
    _s_node = None # 起始节点
    e_id = 0  # 终止节点id
    _e_node = None # 终止节点
    key = 0  # 关键路段：0否，1是
    result = 0 # 输出的结果
    
    def __init__(self):
        pass

    def do_data_convert(self):
        self.convert_start_end()

    # 转换边的方向，如果dir=2则将s_id和e_id互换后dir=1
    def convert_start_end(self):
        if self.dir != 2:
            return
        self.s_id ^= self.e_id
        self.e_id ^= self.s_id
        self.s_id ^= self.e_id
        self.dir = 1

    @staticmethod
    def mapper():
        return {

        }
