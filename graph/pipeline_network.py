import networkx as nx


class PipelineNetwork:
    def __init__(self, pipeline_system):
        self.pipeline_system = pipeline_system
        self.graph = nx.DiGraph()  # Создаем направленный граф

    def build_graph(self):
        """
        создание графа из узлов и ребер (труб)
        """
        for node_id, node in self.pipeline_system.nodes.items():
            self.graph.add_node(node_id, pressure=node.pressure, gas_consumption=node.gas_consumption)

        # Добавляение трубы/рёбра в граф
        for edge in self.pipeline_system.get_edges():
            self.graph.add_edge(edge.start_node, edge.end_node,
                                diameter=edge.diameter,
                                length=edge.length,
                                flow_resistance=edge.flow_resistance)

    def visualize_graph(self):
        """
        Метод для отображения графа
        """
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=500, node_color="lightblue")
        edge_labels = {(edge.start_node, edge.end_node): edge.diameter for edge in self.pipeline_system.get_edges()}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

    def calculate_total_flow_capacity(self):
        """
        Метод для рассчета общей пропускной способности сети
        :rtype: object
        """
        total_capacity = 0
        for edge in self.pipeline_system.get_edges():
            total_capacity += edge.calculate_flow_capacity()
        return total_capacity
