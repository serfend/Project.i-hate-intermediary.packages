class JunctionChildNode:
    id = 0 # 分裂节点序号，1上，2左，3下，4右
    o_id = 0 # 对应原始节点序号
    def __init__(self):
        pass

    @staticmethod
    def mapper():
        return {
            'λi':'Li'
        }