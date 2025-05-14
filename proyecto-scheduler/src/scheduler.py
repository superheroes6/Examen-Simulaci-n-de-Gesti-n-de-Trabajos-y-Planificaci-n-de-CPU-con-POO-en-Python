from abc import ABC, abstractmethod
from typing import List, Tuple

GanttEntry = Tuple[str, int, int]  # Define GanttEntry as a tuple (pid, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    def __init__(self, repositorio):
        self.repositorio = repositorio

    @abstractmethod
    def planificar(self, procesos: List) -> List[GanttEntry]:
        """Abstract method to plan the execution of processes."""
        pass

    def ejecutar_fcfs(self):
        if not self.repositorio.procesos:
            print("No processes to schedule.")
            return

        print("Executing FCFS Scheduler:")
        for proceso in self.repositorio.procesos:
            print(f"Running process {proceso.id_proceso} with execution time {proceso.tiempo_ejecucion}.")

    def ejecutar_round_robin(self, quantum):
        if not self.repositorio.procesos:
            print("No processes to schedule.")
            return

        print(f"Executing Round-Robin Scheduler with quantum {quantum}:")
        gantt_chart = []
        queue = self.repositorio.procesos[:]
        current_time = 0

        while queue:
            proceso = queue.pop(0)
            start_time = current_time
            if proceso.tiempo_ejecucion > quantum:
                current_time += quantum
                proceso.tiempo_ejecucion -= quantum
                queue.append(proceso)
            else:
                current_time += proceso.tiempo_ejecucion
                proceso.tiempo_ejecucion = 0
            gantt_chart.append((proceso.id_proceso, start_time, current_time))

        print("Gantt Chart:", gantt_chart)
        return gantt_chart
