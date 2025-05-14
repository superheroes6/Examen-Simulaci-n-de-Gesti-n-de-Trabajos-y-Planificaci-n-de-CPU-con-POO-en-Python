import json
import csv

class RepositorioProcesos:
    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, proceso):
        if any(p.id_proceso == proceso.id_proceso for p in self.procesos):
            print(f"Process with ID {proceso.id_proceso} already exists.")
            return False
        self.procesos.append(proceso)
        return True

    def listar_procesos(self):
        if not self.procesos:
            print("No processes in the repository.")
        else:
            print("Processes in the repository:")
            for proceso in self.procesos:
                print(proceso)

    def eliminar_proceso(self, pid):
        for proceso in self.procesos:
            if proceso.id_proceso == pid:
                self.procesos.remove(proceso)
                print(f"Process with ID {pid} removed.")
                return True
        print(f"Process with ID {pid} not found.")
        return False

    def obtener_proceso(self, pid):
        for proceso in self.procesos:
            if proceso.id_proceso == pid:
                return proceso
        print(f"Process with ID {pid} not found.")
        return None

    def guardar_en_json(self, archivo="procesos.json"):
        """Save processes to a JSON file."""
        with open(archivo, "w") as f:
            json.dump([p.__dict__ for p in self.procesos], f)
        print(f"Processes saved to {archivo} in JSON format.")

    def cargar_desde_json(self, archivo="procesos.json"):
        """Load processes from a JSON file, replacing existing ones."""
        try:
            with open(archivo, "r") as f:
                self.procesos = [Proceso(**p) for p in json.load(f)]
            print(f"Processes loaded from {archivo}.")
        except FileNotFoundError:
            print(f"File {archivo} not found. No processes loaded.")

    def guardar_en_csv(self, archivo="procesos.csv"):
        """Save processes to a CSV file."""
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["id_proceso", "tiempo_ejecucion", "prioridad"])
            for proceso in self.procesos:
                writer.writerow([proceso.id_proceso, proceso.tiempo_ejecucion, proceso.prioridad])
        print(f"Processes saved to {archivo} in CSV format.")

    def cargar_desde_csv(self, archivo="procesos.csv"):
        """Load processes from a CSV file, replacing existing ones."""
        try:
            with open(archivo, "r") as f:
                reader = csv.DictReader(f, delimiter=";")
                self.procesos = [
                    Proceso(row["id_proceso"], int(row["tiempo_ejecucion"]), int(row["prioridad"]))
                    for row in reader
                ]
            print(f"Processes loaded from {archivo}.")
        except FileNotFoundError:
            print(f"File {archivo} not found. No processes loaded.")
