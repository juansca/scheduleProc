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
                son: 'listo', 'ejecutando' y 'terminado'.
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
        self.estado = estado
        self.prioridad = prioridad
        self.tiempo_inicial = tiempo_inicial
        self.end_time = None
        self.rafaga = rafaga

    def ejecutar():
        """Este método ejecuta durante un instante de tiempo el proceso.
        Mientra el proceso está ejecuntándose, su estado será "ejecutando".
        Una vez que haya finalizado su tiempo de ráfaga, el estado pasará a ser
        "terminado".

        IMPORTANTE: Será responsabilidad del planificador cambiar el estado de
        "ejecutando" a "listo" en caso de que el algoritmo de planificación sea
        apropiativo.
        """
        self.estado = "ejecutando"
        self.rafaga -= 1
        if self.rafaga == 0:
            self.estado = "terminado"

    def estado_listo(self):
        """Este método simplemente cambia el estado a listo.
        Sirve como interfaz.
        """
        self.estado = "listo"


class ProcesoSinRafaga(Exception):
    pass


class CPU:
    """Esta clase representa el cpu de una máquina. Ella ejecutará procesos
    conforme se los brinden.
    """
    def __init__(self):
        """El cpu, en esta caso (muy) simplificado para enfocar la atención a
        la ejecución de los procesos, tendrá como atributos:
        proc: proceso que está ejecutando en un momento dado.
        run_time: tiempo total de ejecución (para simplificación, sólo se
                  contará el tiempo en que haya un proceso en la cpu)
        """
        self.proc = None
        self.run_time = 0

    def ejecutar(self, proceso):
        if proceso.estado == "terminado":
            raise ProcesoSinRafaga("El proceso ha terminado de ejecutarse!")

        proceso.ejecutar()
        self.run_time += 1
