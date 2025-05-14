from proyecto_scheduler.src.metrics import Metrics
from proyecto_scheduler.src.proceso import Proceso

def test_metrics_calculation():
    gantt_chart = [("P1", 0, 5), ("P2", 5, 8)]
    procesos = [
        Proceso("P1", 5, 1, tiempo_llegada=0),
        Proceso("P2", 3, 2, tiempo_llegada=1),
    ]
    promedio_respuesta, promedio_retorno, promedio_espera = Metrics.calcular_tiempos(gantt_chart, procesos)
    assert promedio_respuesta == 2.0
    assert promedio_retorno == 6.5
    assert promedio_espera == 1.5
    print("Test for metrics calculation passed.")
