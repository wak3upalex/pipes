from graph import PipelineNetwork
from pipeline_logic import PipelineSystem

pipeline_system = PipelineSystem()
pipeline_system.add_node("A", pressure=100)
pipeline_system.add_node("B", pressure=90)
pipeline_system.add_node("C", pressure=80)
pipeline_system.add_edge("A", "B", diameter=5, length=100, flow_resistance=1.2)
pipeline_system.add_edge("B", "C", diameter=6, length=150, flow_resistance=1.5)

# Построение графа и отображение
pipeline_network = PipelineNetwork(pipeline_system)
pipeline_network.build_graph()
pipeline_network.visualize_graph()

# Рассчет общей пропускной способности
total_capacity = pipeline_network.calculate_total_flow_capacity()
print("Общая пропускная способность:", total_capacity)
