class Proceso:
    """Esta clase representa un proceso con sus caracteristicas básicas para
    simular una planificación de procesos.
    """
    def __init__(pid=pid, estado='listo', prioridad=None,
                 tiempo_inicial=tiempo_inicial, rafaga=rafaga):
        """Un proceso tiene los siguientes atributos:
        pid: id del proceso. Cada proceso tiene un único id y existe un único
        proceso con un cierto id.
        estado: el estado del proceso en un momento dado. Los estados posibles
                son: 'listo', 'dormido' y 'terminado'.
                NOTA: el estado es un string.
        prioridad: es la prioridad del proceso. Esto sólo se utilizará en el
                  caso en que el algoritmo utilizado haga uso de las
                  prioridades de los procesos.
        tiempo_inicial: es una marca temporal, se corresponderá con el instante
                        en el que el proceso llega.
        rafaga: es la rafaga de CPU que el proceso necesita para ejecutarse por
                completo. Una vez que se termine este contador, el proceso
                pasará al estado 'terminado'.
        """
        self.pid = pid
        self.estado = status
        self.prioridad = priority
        self.tiempo_inicial = tiempo_inicial
        self.end_time = None
        self.rafaga = rafaga

    def ejecutar():
        self.rafaga -= 1


class cpu:
    def __init__(self):
        pass
