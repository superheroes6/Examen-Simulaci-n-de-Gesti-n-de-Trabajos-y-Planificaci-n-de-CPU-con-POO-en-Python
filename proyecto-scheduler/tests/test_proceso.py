from proyecto_scheduler.src.proceso import Proceso

def test_proceso_creation():
    proceso = Proceso("P1", 10, 1, tiempo_llegada=0)
    assert proceso.id_proceso == "P1"
    assert proceso.tiempo_ejecucion == 10
    assert proceso.prioridad == 1
    assert proceso.tiempo_llegada == 0
    print("Test for Proceso creation passed.")
