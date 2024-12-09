import matplotlib.pyplot as plt
import networkx as nx


class PipelineNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()  # Создаем направленный граф

    def build_graph(self):
        """
        создание графа из узлов и ребер (труб)
        """
        nodes_data = [
            (node_id, {"pressure": node.pressure, "gas_consumption": node.gas_consumption})
            for node_id, node in self.pipeline_system.nodes.items()
        ]
        self.graph.add_nodes_from(nodes_data)

        edges_data = [
            (edge.start_node, edge.end_node, {
                "diameter": edge.diameter,
                "length": edge.length,
                "flow_resistance": edge.flow_resistance
            })
            for edge in self.pipeline_system.edges
        ]
        self.graph.add_edges_from(edges_data)

    def visualize_graph(self):
        """
        Метод для отображения графа
        """
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="lightblue")
        edge_labels = nx.get_edge_attributes(self.graph, "length")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()
