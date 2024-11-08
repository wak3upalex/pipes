from pipeline_logic.pipe_edge import PipeEdge
from pipeline_logic.pipe_node import PipeNode


class PipelineSystem:
    def __init__(self):
        self.nodes = {}  # словарь с узлами {node_id: PipeNode}
        self.edges = []  # список с трубами [PipeEdge]

    def add_node(self, node_id, pressure, gas_consumption=0):

        node = PipeNode(node_id, pressure, gas_consumption)
        self.nodes[node_id] = node

    def add_edge(self, start_node, end_node, diameter, length, flow_resistance):
        if start_node in self.nodes and end_node in self.nodes:
            edge = PipeEdge(start_node, end_node, diameter, length, flow_resistance)
            self.edges.append(edge)
        else:
            raise ValueError("Указанные узлы должны быть добавлены в систему перед добавлением трубы.")

    def get_node(self, node_id):
        return self.nodes.get(node_id, None)

    def get_edges(self):
        return self.edges

    def update_node_pressure(self, node_id, new_pressure):
        node = self.get_node(node_id)
        if node:
            node.update_pressure(new_pressure)
