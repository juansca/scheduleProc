from catedra import stats, Proceso, table
from planificador import Planificador
import csv


def ask(name):
    arg_str = input(name + '> ')
    return eval(arg_str)


def agregar_procesos(planificador):
    """Esta función leerá el archivo que contiene una instancia de procesos.
    A partir de él, creará los procesos correspondientes y utilizará métodos
    del planificador para que éste último se haga de ellos.
    Además, la función imprimirá por consola una tabla con la instancia que
    ha cargado del archivo.
    """
    procesos = []
    with open('procesos.csv', 'r') as f:
        i = 0
        reader = csv.reader(f)
        for proc_info in reader:
            if i == 0:
                headers = proc_info
                i += 1
                continue
            pid = proc_info[0]
            rafaga = int(proc_info[1])
            tiempo_arribo = int(proc_info[2])
            # Si el algoritmo que vamos a usar no utiliza la prioridad,
            # no se tendrá en cuenta la misma
            prioridad = None
            if len(proc_info) == 4:
                prioridad = int(proc_info[3])
            proc = Proceso(pid=pid, rafaga=rafaga, tiempo_arribo=tiempo_arribo,
                           prioridad=prioridad)
            planificador.entra_proceso(proc)
            procesos.append(proc)
    estado_inicial = table(procesos, headers)
    print(estado_inicial)


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

            agregar_procesos(planificador)
            print("\n\nALGORITMO EN EJECUCIÓN...\n\n")
            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            tabla, promedio = stats(procesos_terminados)
            print("El promedio de espera de los procesos fue de {}", promedio)
            print(tabla)

    except (SyntaxError, TypeError, NameError, ValueError) as err:
        print(err)
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
