import texttable as tt
from numpy import mean


class Proceso:
    """Esta clase representa un proceso con sus caracteristicas básicas para
    simular una planificación de procesos.
    """
    def __init__(self, pid=None, estado='listo', prioridad=None,
                 tiempo_arribo=None, rafaga=None):
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
        self.tiempo_arribo = tiempo_arribo
        self.tiempo_inicial = None
        self.end_time = -1
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
    """Esta clase representa la excepción que ocurre cuando se quiere ejecutar
    un proceso que no tiene más ráfaga.
    """
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
        self.run_time = 0

    def ejecutar(self, proceso):
        """Este método ejecuta un proceso en la CPU.
        Se encargará de cambiar el estado a 'terminado' en caso de ser
        necesario, pero NO lo cambiará a 'listo'.
        Asignar el tiempo una vez que se termine de ejecutar el proceso será
        responsabilidad del planificador.
        """
        if proceso.tiempo_inicial is None:
            proceso.tiempo_inicial = self.run_time
        if proceso.estado == "terminado":
            raise ProcesoSinRafaga("El proceso ha terminado de ejecutarse!")

        proceso.ejecutar()
        self.run_time += 1

    def gettime(self):
        """Este método retorna el tiempo total que ha ejecutado la CPU en el
        momento en que se lo invoca.
        """
        return self.run_time

###############################################################################


def table(procesos, headers):
    """Toma una lista de procesos (instancias de la clase Proceso), confecciona
    una tabla con los datos de cada uno.
    Esta función se usará para mostrar la instancia del problema inicial, una
    vez que se cargan desde el archivo.
    Notar que para este caso, le pasamos como argumento los nombres de las
    columnas.
    """
    # Aquí creamos cada columna
    pids = [proc.pid for proc in procesos]
    rafagas = [proc.rafaga for proc in procesos]
    tiempos_arribo = [proc.tiempo_arribo for proc in procesos]

    table = tt.Texttable()
    table.header(headers)

    if len(headers) == 4:
        prioridades = [proc.prioridad for proc in procesos]
        filas = zip(pids, rafagas, tiempos_arribo, prioridades)
    else:
        filas = zip(pids, rafagas, tiempos_arribo)
    for fila in filas:
        table.add_row(fila)

    tabla = table.draw()
    return tabla


def stats(procesos):
    """Toma una lista de procesos (instancias de la clase Proceso), confecciona
    una tabla con los datos de cada uno y calcula el promedio de espera de
    todos los procesos
    """
    # Estas serán las etiquetas de las columnas
    headears = ["PID", "Ráfaga", "T Arribo",
                "T Inicial", "T Final", "Tiempo Total"]

    # Aquí creamos cada columna
    pids = [proc.pid for proc in procesos]
    rafagas = [proc.rafaga for proc in procesos]
    tiempos_arribo = [proc.tiempo_arribo for proc in procesos]
    tiempos_iniciales = [proc.tiempo_inicial for proc in procesos]
    tiempos_finales = [proc.end_time for proc in procesos]

    tiempos_totales = [tf - ta for ta, tf in zip(tiempos_arribo,
                                                 tiempos_finales)]
    tiempos_espera = [tt - r for tt, r in zip(tiempos_totales,
                                              rafagas)]
    promedio_espera = mean(tiempos_espera)
    table = tt.Texttable()
    table.header(headears)

    for fila in zip(pids, rafagas, tiempos_arribo, tiempos_iniciales,
                    tiempos_finales, tiempos_totales):
        table.add_row(fila)

    tabla = table.draw()
    return tabla, promedio_espera
