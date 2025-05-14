import json

class Repositorio:
    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)

    def guardar_en_disco(self, archivo="procesos.json"):
        with open(archivo, "w") as f:
            json.dump([p.__dict__ for p in self.procesos], f)

    def cargar_desde_disco(self, archivo="procesos.json"):
        try:
            with open(archivo, "r") as f:
                self.procesos = [Proceso(**p) for p in json.load(f)]
        except FileNotFoundError:
            print("Archivo no encontrado. Iniciando con un repositorio vacío.")
