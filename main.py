from catedra import Proceso, agregar_procesos, stats
from planificador import Planificador


def ask(name):
    arg_str = input(name + '> ')
    return eval(arg_str)


while True:
    try:
        fstr = input('salir, mas o ayuda> ')
        if fstr == 'salir':
            exit()
        elif fstr == 'ayuda':
            a = '''Ejemplo de uso:

                salir, mas o ayuda> mas
                Seleccione un algoritmo de planificación de la siguiente lista:
                1. FCFS
                2. SJF (NO APROPIATIVO)
                3. SJF (APROPIATIVO)
                4. TURNO CIRCULAR.
                5. POR PRIORIDAD (NO APROPIATIVO)
                6. POR PRIORIDAD (APROPIATIVO)
                > 1
                '''
            print(a)

        elif fstr == 'mas':
            alg = ask('''Seleccione un algoritmo de planificación de la siguiente lista:
                    1. FCFS
                    2. SJF (NO APROPIATIVO)
                    3. SJF (APROPIATIVO)
                    4. TURNO CIRCULAR
                    5. POR PRIORIDAD (NO APROPIATIVO)
                    6. POR PRIORIDAD (APROPIATIVO)
                    ''')
            alg = int(alg)
            if alg < 1 or alg > 6:
                print("Porfavor, insertá un número válido.\n")
                continue
            algoritmos = ['fcfs', 'sjfna', 'sjfa', 'rr', 'ppna', 'ppa']
            alg = algoritmos[alg - 1]
            planificador = Planificador(alg)
            if alg == 'rr':
                q = ask('''Cuál será el quantum a utilizar?''')
                q = int(q)
                planificador.agregar_quantum(q)

            agregar_procesos(planificador, 'procesos.csv')
            print("\n\nALGORITMO EN EJECUCIÓN...\n\n")
            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            tabla, promedio, _ = stats(procesos_terminados)
            print("El promedio de espera de los procesos fue de {}", promedio)
            print(tabla)

    except (SyntaxError, TypeError, NameError, ValueError) as err:
        print(err)
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
