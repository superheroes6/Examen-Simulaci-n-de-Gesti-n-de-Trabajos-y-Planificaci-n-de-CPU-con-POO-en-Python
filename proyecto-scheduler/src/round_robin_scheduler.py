from src.scheduler import Scheduler, GanttEntry
from typing import List

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
