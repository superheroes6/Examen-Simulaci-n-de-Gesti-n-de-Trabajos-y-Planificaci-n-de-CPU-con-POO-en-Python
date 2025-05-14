from proyecto_scheduler.src.scheduler import Scheduler
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
            scheduler.ejecutar_fcfs()
        elif choice == "3":
            quantum = int(input("Enter quantum: "))
            gantt_chart = scheduler.ejecutar_round_robin(quantum)
            if gantt_chart:
                promedio_respuesta, promedio_espera, promedio_retorno = Metrics.calcular_tiempos(gantt_chart)
                print(f"Average Response Time: {promedio_respuesta}")
                print(f"Average Wait Time: {promedio_espera}")
                print(f"Average Turnaround Time: {promedio_retorno}")