class Proceso:
    def __init__(self, id_proceso, tiempo_ejecucion, prioridad, tiempo_llegada=0):
        self.id_proceso = id_proceso
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad
        self.tiempo_llegada = tiempo_llegada

    def __repr__(self):
        return (
            f"Proceso(id={self.id_proceso}, tiempo={self.tiempo_ejecucion}, "
            f"prioridad={self.prioridad}, llegada={self.tiempo_llegada})"
        )
