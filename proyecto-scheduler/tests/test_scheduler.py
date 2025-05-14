def test_scheduler_fcfs():
    from proyecto_scheduler.src.proceso import Proceso
    from proyecto_scheduler.src.repositorio import Repositorio
    from proyecto_scheduler.src.scheduler import Scheduler

    repositorio = Repositorio()
    scheduler = Scheduler(repositorio)

    proceso1 = Proceso("P1", 5, 1)
    proceso2 = Proceso("P2", 3, 2)
    repositorio.agregar_proceso(proceso1)
    repositorio.agregar_proceso(proceso2)

    scheduler.ejecutar_fcfs()
    # Placeholder for assertions
    print("Test for FCFS scheduling executed.")

def test_scheduler_round_robin():
    from proyecto_scheduler.src.proceso import Proceso
    from proyecto_scheduler.src.repositorio import Repositorio
    from proyecto_scheduler.src.scheduler import Scheduler

    repositorio = Repositorio()
    scheduler = Scheduler(repositorio)

    proceso1 = Proceso("P1", 5, 1)
    proceso2 = Proceso("P2", 3, 2)
    repositorio.agregar_proceso(proceso1)
    repositorio.agregar_proceso(proceso2)

    gantt_chart = scheduler.ejecutar_round_robin(quantum=2)
    assert gantt_chart == [("P1", 0, 2), ("P2", 2, 4), ("P1", 4, 7)]
    print("Test for Round-Robin scheduling executed.")
