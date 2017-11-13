# https://docs.python.org/3/library/unittest.html
from unittest import TestCase
from catedra import agregar_procesos, stats
from planificador import Planificador


class TestPlanificador(TestCase):

    def test_fcfs(self):
        self.planificador = Planificador('fcfs')
        # Archivos con instancias de procesos para ejecutar
        test_files = ['procesos/test_file1.csv', 'procesos/test_file2.csv']
        for test_file in test_files:
            agregar_procesos(planificador, test_file)

            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            _, promedio, datos_algoritmo = stats(procesos_terminados)
            # Aquí se carga el resultado esperado del algoritmo
            # Cada uno en el orden adecuado de FINALIZACIÓN
            estado_real = {
                'pids': ,
                'rafagas': ,
                'tiempos_finales': ,
                'tiempos_totales': ,
                'tiempos_espera': ,
                'promedio': ,
            }
            # Se comprueba que el resultado del algoritmo sea el esperado
            self.assertEqual(estado_real['pids'], promedio)

            self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

            self.assertEqual([0] * len(estado_real['pids']),
                             datos_algoritmo['rafagas'])

            self.assertEqual(estado_real['tiempos_finales'],
                             datos_algoritmo['tiempos_finales'])

            self.assertEqual(estado_real['tiempos_totales'],
                             datos_algoritmo['tiempos_totales'])

            self.assertEqual(estado_real['tiempos_espera'],
                             datos_algoritmo['tiempos_espera'])

    def test_sjfna(self):
        self.planificador = Planificador('sjfna')
        # Archivos con instancias de procesos para ejecutar
        test_files = ['procesos/test_file1.csv', 'procesos/test_file2.csv']
        for test_file in test_files:
            agregar_procesos(planificador, test_file)

            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            _, promedio, datos_algoritmo = stats(procesos_terminados)
            # Aquí se carga el resultado esperado del algoritmo
            estado_real = {
                'pids': ,
                'rafagas': ,
                'tiempos_finales': ,
                'tiempos_totales': ,
                'tiempos_espera': ,
            }
            # Se comprueba que el resultado del algoritmo sea el esperado
            self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

            self.assertEqual([0] * len(estado_real['pids']),
                             datos_algoritmo['rafagas'])

            self.assertEqual(estado_real['tiempos_finales'],
                             datos_algoritmo['tiempos_finales'])

            self.assertEqual(estado_real['tiempos_totales'],
                             datos_algoritmo['tiempos_totales'])

            self.assertEqual(estado_real['tiempos_espera'],
                             datos_algoritmo['tiempos_espera'])

    def test_sjfa(self):
        self.planificador = Planificador('sjfa')
        # Archivos con instancias de procesos para ejecutar
        test_files = ['procesos/test_file1.csv', 'procesos/test_file2.csv']
        for test_file in test_files:
            agregar_procesos(planificador, test_file)

            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            _, promedio, datos_algoritmo = stats(procesos_terminados)
            # Aquí se carga el resultado esperado del algoritmo
            estado_real = {
                'pids': ,
                'rafagas': ,
                'tiempos_finales': ,
                'tiempos_totales': ,
                'tiempos_espera': ,
            }
            # Se comprueba que el resultado del algoritmo sea el esperado
            self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

            self.assertEqual([0] * len(estado_real['pids']),
                             datos_algoritmo['rafagas'])

            self.assertEqual(estado_real['tiempos_finales'],
                             datos_algoritmo['tiempos_finales'])

            self.assertEqual(estado_real['tiempos_totales'],
                             datos_algoritmo['tiempos_totales'])

            self.assertEqual(estado_real['tiempos_espera'],
                             datos_algoritmo['tiempos_espera'])

    def test_rr(self):
        q = 5
        self.planificador = Planificador('rr')
        # Archivos con instancias de procesos para ejecutar
        test_files = ['procesos/test_file1.csv', 'procesos/test_file2.csv']
        for test_file in test_files:
            agregar_procesos(planificador, test_file)

            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            _, promedio, datos_algoritmo = stats(procesos_terminados)
            # Aquí se carga el resultado esperado del algoritmo
            estado_real = {
                'pids': ,
                'rafagas': ,
                'tiempos_finales': ,
                'tiempos_totales': ,
                'tiempos_espera': ,
            }
            # Se comprueba que el resultado del algoritmo sea el esperado
            self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

            self.assertEqual([0] * len(estado_real['pids']),
                             datos_algoritmo['rafagas'])

            self.assertEqual(estado_real['tiempos_finales'],
                             datos_algoritmo['tiempos_finales'])

            self.assertEqual(estado_real['tiempos_totales'],
                             datos_algoritmo['tiempos_totales'])

            self.assertEqual(estado_real['tiempos_espera'],
                             datos_algoritmo['tiempos_espera'])

    def test_ppna(self):
        self.planificador = Planificador('ppna')
        agregar_procesos(planificador, 'procesos/to_test_pp.csv')
        planificador.ejecutar_algoritmo()
        procesos_terminados = planificador.terminados()
        _, promedio, datos_algoritmo = stats(procesos_terminados)
        # Aquí se carga el resultado esperado del algoritmo
        estado_real = {
            'pids': ,
            'rafagas': ,
            'tiempos_finales': ,
            'tiempos_totales': ,
            'tiempos_espera': ,
        }
        # Se comprueba que el resultado del algoritmo sea el esperado
        self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

        self.assertEqual([0] * len(estado_real['pids']),
                         datos_algoritmo['rafagas'])

        self.assertEqual(estado_real['tiempos_finales'],
                         datos_algoritmo['tiempos_finales'])

        self.assertEqual(estado_real['tiempos_totales'],
                         datos_algoritmo['tiempos_totales'])

        self.assertEqual(estado_real['tiempos_espera'],
                         datos_algoritmo['tiempos_espera'])

    def test_ppa(self):
        self.planificador = Planificador('ppa')
        agregar_procesos(planificador, 'procesos/to_test_pp.csv')
        agregar_procesos(planificador, 'procesos/to_test_pp.csv')
        planificador.ejecutar_algoritmo()
        procesos_terminados = planificador.terminados()
        _, promedio, datos_algoritmo = stats(procesos_terminados)
        # Aquí se carga el resultado esperado del algoritmo
        estado_real = {
            'pids': ,
            'rafagas': ,
            'tiempos_finales': ,
            'tiempos_totales': ,
            'tiempos_espera': ,
        }
        # Se comprueba que el resultado del algoritmo sea el esperado
        self.assertEqual(estado_real['pids'], datos_algoritmo['pids'])

        self.assertEqual([0] * len(estado_real['pids']),
                         datos_algoritmo['rafagas'])

        self.assertEqual(estado_real['tiempos_finales'],
                         datos_algoritmo['tiempos_finales'])

        self.assertEqual(estado_real['tiempos_totales'],
                         datos_algoritmo['tiempos_totales'])

        self.assertEqual(estado_real['tiempos_espera'],
                         datos_algoritmo['tiempos_espera'])
