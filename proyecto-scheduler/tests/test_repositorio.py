from src.proceso import Proceso
from src.repositorio import RepositorioProcesos

def test_repositorio_json_persistence(tmp_path):
    repo = RepositorioProcesos()
    proceso = Proceso("P1", 5, 1, tiempo_llegada=0)
    repo.agregar_proceso(proceso)
    json_file = tmp_path / "procesos.json"
    repo.guardar_en_json(json_file)
    repo.cargar_desde_json(json_file)
    assert len(repo.procesos) == 1
    assert repo.procesos[0].id_proceso == "P1"
    print("Test for JSON persistence passed.")

def test_repositorio_csv_persistence(tmp_path):
    repo = RepositorioProcesos()
    proceso = Proceso("P1", 5, 1, tiempo_llegada=0)
    repo.agregar_proceso(proceso)
    csv_file = tmp_path / "procesos.csv"
    repo.guardar_en_csv(csv_file)
    repo.cargar_desde_csv(csv_file)
    assert len(repo.procesos) == 1
    assert repo.procesos[0].id_proceso == "P1"
    print("Test for CSV persistence passed.")
