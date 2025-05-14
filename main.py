from proyecto_scheduler.src.fcfs_scheduler import FCFSScheduler
from proyecto_scheduler.src.round_robin_scheduler import RoundRobinScheduler
from proyecto_scheduler.src.repositorio import Repositorio
from proyecto_scheduler.src.proceso import Proceso
from proyecto_scheduler.src.metrics import Metrics

if __name__ == "__main__":
    print("Welcome to the CPU Scheduler Simulation!")
    repositorio = Repositorio()
    scheduler = Scheduler(repositorio)

    while True:
        print("\nMenu:")
        print("1. Add Process")
        print("2. Run FCFS Scheduler")
        print("3. Run Round-Robin Scheduler")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id_proceso = input("Enter process ID: ")
            tiempo_ejecucion = int(input("Enter execution time: "))
            prioridad = int(input("Enter priority: "))
            proceso = Proceso(id_proceso, tiempo_ejecucion, prioridad)
            repositorio.agregar_proceso(proceso)
            print(f"Process {id_proceso} added.")
        elif choice == "2":
            scheduler = FCFSScheduler(repositorio)
            gantt_chart = scheduler.planificar(repositorio.procesos)
            if gantt_chart:
                print("Gantt Chart (FCFS):")
                for entry in gantt_chart:
                    print(f"Process {entry[0]}: Start={entry[1]}, End={entry[2]}")
        elif choice == "3":
            quantum = int(input("Enter quantum: "))
            scheduler = RoundRobinScheduler(repositorio, quantum)
            gantt_chart = scheduler.planificar(repositorio.procesos)
            if gantt_chart:
                print("Gantt Chart (Round-Robin):")
                for entry in gantt_chart:
                    print(f"Process {entry[0]}: Start={entry[1]}, End={entry[2]}")
                promedio_respuesta, promedio_retorno, promedio_espera = Metrics.calcular_tiempos(
                    gantt_chart, repositorio.procesos
                )
                print(f"Average Response Time: {promedio_respuesta}")
                print(f"Average Turnaround Time: {promedio_retorno}")
                print(f"Average Wait Time: {promedio_espera}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
