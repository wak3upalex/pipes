class PipeNode:
    def __init__(self, node_id, pressure, gas_consumption=0):
        """
        :param node_id: уникальный идентификатор узла
        :param pressure: давление в узле
        :param gas_consumption: объем газа, потребляемый в узле
        """
        self.node_id = node_id
        self.pressure = pressure
        self.gas_consumption = gas_consumption

    def update_pressure(self, new_pressure):
        """
        Обновление давления в узле
        :param new_pressure: Значение нового давления, которое должно быть задано в узле
        """
        self.pressure = new_pressure
