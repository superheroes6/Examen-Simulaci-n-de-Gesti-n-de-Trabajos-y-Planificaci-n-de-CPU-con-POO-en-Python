class Metrics:
    @staticmethod
    def calcular_tiempos(gantt_chart):
        tiempos_respuesta = {}
        tiempos_espera = {}
        tiempos_retorno = {}

        for pid, start, end in gantt_chart:
            if pid not in tiempos_respuesta:
                tiempos_respuesta[pid] = start
            tiempos_retorno[pid] = end

        for pid in tiempos_respuesta:
            tiempos_espera[pid] = tiempos_retorno[pid] - tiempos_respuesta[pid]

        promedio_respuesta = sum(tiempos_respuesta.values()) / len(tiempos_respuesta)
        promedio_espera = sum(tiempos_espera.values()) / len(tiempos_espera)
        promedio_retorno = sum(tiempos_retorno.values()) / len(tiempos_retorno)

        return promedio_respuesta, promedio_espera, promedio_retorno
