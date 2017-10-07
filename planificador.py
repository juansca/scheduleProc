from catedra import CPU, Proceso


class Planificador:

    def __init__(self, algoritmo='rr'):
        algoritmos = {
            'fcfs': Planificador.fcfs,
            'sjfna': Planificador.sjfna,
            'sjfa': Planificador.sjfa,
            'rr': Planificador.round_robin,
            'ppna': Planificador.ppna,
            'ppa': Planificador.ppa,

        }

        self.listos = []
        self.finalizados = []
        self.algoritmo = algoritmo

    def ejecutar_algoritmo(self):
        pass

    def _entra_proceso(self, proc):
        pass

    def _proceso_termina(self, proc):
        pass

    def fcfs(self):
        """Algoritmo de planificación Firts-Come, First-Served (FCFS)"""
        # Aquí va su código ###
        pass

    def sjfna(self):
        """Algoritmo de planificación Shortest Job First (No apropiativo)"""
        # Aquí va su código ###
        pass

    def sjfa(self):
        """Algoritmo de planificación Shortest Job First (Apropiativo)"""
        # Aquí va su código ###
        pass

    def rr(self):
        """Algoritmo de planificación Round Robin (Turno Circular)"""
        # Aquí va su código ###
        pass

    def ppna(self):
        """Algoritmo de planificación por prioridad (No Apropiativo)"""
        # Aquí va su código ###
        pass

    def ppa(self):
        """Algoritmo de planificación por prioridad (No Apropiativo)"""
        # Aquí va su código ###
        pass
