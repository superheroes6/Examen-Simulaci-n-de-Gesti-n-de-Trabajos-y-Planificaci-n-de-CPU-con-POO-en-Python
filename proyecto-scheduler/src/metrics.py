class Metrics:
    @staticmethod
    def calcular_tiempos(gantt_chart, procesos):
        tiempos_respuesta = {}
        tiempos_retorno = {}
        tiempos_espera = {}

        for pid, start, end in gantt_chart:
            proceso = next(p for p in procesos if p.id_proceso == pid)
            if pid not in tiempos_respuesta:
                tiempos_respuesta[pid] = start - proceso.tiempo_llegada
            tiempos_retorno[pid] = end - proceso.tiempo_llegada
            tiempos_espera[pid] = tiempos_retorno[pid] - proceso.tiempo_ejecucion

        promedio_respuesta = sum(tiempos_respuesta.values()) / len(tiempos_respuesta)
        promedio_retorno = sum(tiempos_retorno.values()) / len(tiempos_retorno)
        promedio_espera = sum(tiempos_espera.values()) / len(tiempos_espera)

        return promedio_respuesta, promedio_retorno, promedio_espera
