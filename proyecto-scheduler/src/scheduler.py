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

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List) -> List[GanttEntry]:
        if not procesos:
            print("No processes to schedule.")
            return []

        gantt_chart = []
        current_time = 0

        for proceso in procesos:
            start_time = current_time
            current_time += proceso.tiempo_ejecucion
            gantt_chart.append((proceso.id_proceso, start_time, current_time))

        print("Gantt Chart (FCFS):")
        for entry in gantt_chart:
            print(f"Process {entry[0]}: Start={entry[1]}, End={entry[2]}")
        return gantt_chart

class RoundRobinScheduler(Scheduler):
    def __init__(self, repositorio, quantum: int):
        super().__init__(repositorio)
        self.quantum = quantum

    def planificar(self, procesos: List) -> List[GanttEntry]:
        if not procesos:
            print("No processes to schedule.")
            return []

        gantt_chart = []
        queue = procesos[:]
        current_time = 0

        while queue:
            proceso = queue.pop(0)
            start_time = current_time
            if proceso.tiempo_ejecucion > self.quantum:
                current_time += self.quantum
                proceso.tiempo_ejecucion -= self.quantum
                queue.append(proceso)
            else:
                current_time += proceso.tiempo_ejecucion
                proceso.tiempo_ejecucion = 0
            gantt_chart.append((proceso.id_proceso, start_time, current_time))

        print("Gantt Chart (Round-Robin):")
        for entry in gantt_chart:
            print(f"Process {entry[0]}: Start={entry[1]}, End={entry[2]}")
        return gantt_chart
