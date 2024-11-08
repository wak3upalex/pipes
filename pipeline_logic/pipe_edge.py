class PipeEdge:
    def __init__(self, start_node, end_node, diameter, length, flow_resistance):
        """
        :param start_node: начальный узел
        :param end_node: конечный узел
        :param diameter: диаметр трубы
        :param length: длина трубы
        :param flow_resistance: сопротивление потоку
        """
        self.start_node = start_node
        self.end_node = end_node
        self.diameter = diameter
        self.length = length
        self.flow_resistance = flow_resistance

    def calculate_flow_capacity(self):
        """
        Условный Расчет пропускной способности трубы на основе физических параметров
        :return: Пропускную способность трубы
        """
        return self.diameter / self.length * (1 / self.flow_resistance)
