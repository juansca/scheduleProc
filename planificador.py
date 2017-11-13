from catedra import CPU, Proceso


class Planificador:

    def __init__(self, algoritmo='rr'):
        algoritmos = {
            'fcfs': self.fcfs,
            'sjfna': self.sjfna,
            'sjfa': self.sjfa,
            'rr': self.rr,
            'ppna': self.ppna,
            'ppa': self.ppa,

        }
        self.quantum = None
        self.listos = []
        self.finalizados = []
        self.algoritmo = algoritmos[algoritmo]

    def agregar_quantum(self, quantum):
        self.quantum = quantum

    def ejecutar_algoritmo(self):
        self.algoritmo()

    def entra_proceso(self, proc):
        self.listos.append(proc)

    def terminados(self):
        return self.finalizados

    def fcfs(self):
        """Algoritmo de planificación Firts-Come, First-Served (FCFS)"""
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
