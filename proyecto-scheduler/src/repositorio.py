import json

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

    def guardar_en_disco(self, archivo="procesos.json"):
        with open(archivo, "w") as f:
            json.dump([p.__dict__ for p in self.procesos], f)

    def cargar_desde_disco(self, archivo="procesos.json"):
        try:
            with open(archivo, "r") as f:
                self.procesos = [Proceso(**p) for p in json.load(f)]
        except FileNotFoundError:
            print("Archivo no encontrado. Iniciando con un repositorio vacío.")
