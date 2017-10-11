from catedra import to_table


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
                    4. TURNO CIRCULAR.
                    5. POR PRIORIDAD (NO APROPIATIVO)
                    6. POR PRIORIDAD (APROPIATIVO)
                    ''')
            alg = int(alg)
            if alg < 1 or alg > 6:
                print("Porfavor, insertá un número válido.\n")
                continue
            algoritmos = ['fcfs', 'sjfna', 'sjfa', 'rr', 'ppna', 'ppa']
            planificador = Planificador(algoritmos[alg - 1])
            planificador.ejecutar_algoritmo()
            procesos_terminados = planificador.terminados()
            print(to_table(procesos_terminados))

    except (SyntaxError, TypeError, NameError) as err:
        print(err)
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
