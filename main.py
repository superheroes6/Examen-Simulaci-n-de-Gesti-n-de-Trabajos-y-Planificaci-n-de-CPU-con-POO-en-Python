from proyecto_scheduler.src.scheduler import Scheduler
from proyecto_scheduler.src.repositorio import Repositorio

if __name__ == "__main__":
    print("Welcome to the CPU Scheduler Simulation!")
    # Initialize repository and scheduler
    repositorio = Repositorio()
    scheduler = Scheduler(repositorio)
    
    # Placeholder for CLI logic
    print("CLI not implemented yet.")
