from src.scheduler import Scheduler, GanttEntry
from typing import List

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
