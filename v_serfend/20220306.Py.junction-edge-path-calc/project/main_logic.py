import controller.edge_generate
import controller.module_2
import controller.module_1
from utils.xlsx_handler import XlsxHandler
import utils.clazz
from entities.Edge import Edge
from entities.JunctionChildNode import JunctionChildNode
from entities.JunctionNode import JunctionNode
from entities.Direction import Direction
import json


def xls2object(xls, sheet_name, target_type, mapper):
    items = xls.read(sheet_name, mapper=mapper)
    func = utils.clazz.dict2obj
    return [func(target_type(), x) for x in items]


data = {
    'edges': None,
    'junctionNodes': None,
    'junctionChildNodes': None
}


def main(x8):
    initialize()
    statistics = {
        'edges': len(data["edges"]),
        'nodes': len(data["junctionNodes"]),
        'childNodes': len(data["junctionChildNodes"]),
        'connections': sum([len(x.connected_edges) for x in data["junctionNodes"]]),
    }
    s = json.dumps(statistics)
    print(f'data initilized,{s}')  # 初始化统计
    m1 = controller.module_1.main(x8, data['edges'])  # 计算模块1
    m2 = controller.module_2.main(x8, data['junctionNodes'])  # 计算模块2
    new_edges = [x.generate_edge_with_direction()
                 for x in data['junctionNodes']]
    for e in new_edges:
        data['edges'] += e
    output_data()


def output_data():
    xls = XlsxHandler('./output/n2_result.xlsx')
    edges = [{'id': x.id, 'result': x.result, 's_id': x.s_id,
              'e_id': x.e_id, 'dir': x.dir} for x in data['edges']]

    nodes = [
        {
            'id': x.id, 'result': x.result,
            'connected_edges': str.join(',', [str(t.id) for t in x.connected_edges]),
            'directions':str.join(',', [str(t.id) for t in x.directions])
        } for x in data['junctionNodes']]

    xls.write(edges, 'edge_result')
    xls.write(nodes, 'junction1_result')


def load_data():
    xls = XlsxHandler('./configuration/data.xlsx')
    edges = xls2object(xls, 'edge', Edge, Edge.mapper())
    data['edges'] = edges
    data['junctionNodes'] = xls2object(
        xls, 'junction1', JunctionNode, JunctionNode.mapper())
    data['junctionChildNodes'] = xls2object(
        xls, 'junction2', JunctionChildNode, JunctionChildNode.mapper())
    data['directions'] = xls2object(
        xls, 'direction', Direction, Direction.mapper())


def map_node_edge():
    node_dict = {}
    for n in data['junctionNodes']:
        node_dict[n.id] = n

    def node_check(node_id, edge):
        if not node_id in node_dict:
            print(f'{node_id} is not exist in database')
            return
        n = node_dict[node_id]
        n.add_edge(edge)
    edges = data['edges']
    for e in edges:
        node_check(e.s_id, e)
        node_check(e.e_id, e)

    for x in edges:
        x.do_data_convert()  # 将dir=2全部转换为dir=1
        x._s_node = node_dict[x.s_id]
        x._e_node = node_dict[x.e_id]

    directions = data['directions']
    for d in directions:
        node_dict[d.n_id].add_direction(d)


def map_node_childNode():
    node_dict = {}
    for n in data['junctionNodes']:
        node_dict[n.id] = n
    child_nodes = data['junctionChildNodes']
    for n in child_nodes:
        node_dict[n.o_id].add_child_node(n.id)


def initialize():
    load_data()
    map_node_edge()
    map_node_childNode()


if __name__ == '__main__':
    # x8 = input('input x8')
    x8 = 1
    main(int(x8))
