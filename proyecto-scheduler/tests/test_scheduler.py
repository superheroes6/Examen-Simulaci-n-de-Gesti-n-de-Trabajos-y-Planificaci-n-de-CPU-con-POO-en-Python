from src.proceso import Proceso
from src.fcfs_scheduler import FCFSScheduler
from src.round_robin_scheduler import RoundRobinScheduler

def test_scheduler_fcfs():
    procesos = [
        Proceso("P1", 5, 1, tiempo_llegada=0),
        Proceso("P2", 3, 2, tiempo_llegada=1),
    ]
    scheduler = FCFSScheduler(None)
    gantt_chart = scheduler.planificar(procesos)
    assert gantt_chart == [("P1", 0, 5), ("P2", 5, 8)]
    print("Test for FCFS scheduling passed.")

def test_scheduler_round_robin():
    procesos = [
        Proceso("P1", 5, 1, tiempo_llegada=0),
        Proceso("P2", 3, 2, tiempo_llegada=1),
    ]
    scheduler = RoundRobinScheduler(None, quantum=2)
    gantt_chart = scheduler.planificar(procesos)
    assert gantt_chart == [("P1", 0, 2), ("P2", 2, 4), ("P1", 4, 7)]
    print("Test for Round-Robin scheduling passed.")
