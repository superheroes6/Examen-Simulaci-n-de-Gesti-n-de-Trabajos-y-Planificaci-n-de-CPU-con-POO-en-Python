def test_metrics_calculation():
    from proyecto_scheduler.src.metrics import Metrics

    gantt_chart = [("P1", 0, 2), ("P2", 2, 4), ("P1", 4, 7)]
    promedio_respuesta, promedio_espera, promedio_retorno = Metrics.calcular_tiempos(gantt_chart)

    assert promedio_respuesta == 1.0
    assert promedio_espera == 3.0
    assert promedio_retorno == 5.0
    print("Test for metrics calculation executed.")
