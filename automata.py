"""
    Funcion que recorre un automata, dadas sus caracteristicas, para ver si
    una cadena pertenece o no a su lenguaje de aceptación.
    
    Recibe:
        cadena     - Cadena a evaluar el automata
        edo_actual - Numero del estado actual, a partir del cual evaluara <<cadena>>
        func_trans - Diccionario que posee las reglas de transicion del automata
        finales    - Lista con los estados finales
    Notas:
        A cada estado le corresponde un num. La func_trans se puede ver
        como una funcion de R^2 a R, donde recibe un par ordenado (una lista)
        con los valores (edo_actual, entrada) y devuelve un nuevo estado.
        Los automatas que procesa funcionan como deterministas, con la diferencia 
        de que no se necesita definir la función de transición para todos los 
        caracteres del alfabeto para cada estado.
        ie, si no defines que pasa en un estado # al recibir X, y se da dicha
        situación, el automata devuelve que la cadena no fue aceptada
"""
def automata(cadena,edo_actual,func_trans,finales):
    if cadena == "":                 # Si se terminó de revisar toda la cadena
        return edo_actual in finales # Verificar si se llego a un estado final
    else:
        entrada = cadena[0] 
        if (edo_actual, entrada) in func_trans: # Si la funcion de transicion esta definida para dicha entrada:
            return automata(cadena[1:], func_trans[(edo_actual,entrada)], func_trans, finales)
        else:
            return False



# # # # # # # # # # # # #
#                       #
#   Ejemplos de uso:    #
#                       #
# # # # # # # # # # # # #

"""
    Automata especifico cuyo lenguaje de aceptación es el mismo que el de la
    expresión regular fl[o+]w
"""
def ejemplo1(cadena):
    mi_func = { (1, 'f'): 2,
                (2, 'l'): 3,
                (3, 'o'): 4,
                (4, 'o'): 4,
                (4, 'w'): 5,
                }
    mis_finales = [5]
    return automata(cadena, 1, mi_func, mis_finales)

"""
    Automata especifico cuyo lenguaje de aceptación es el mismo que el de la
    expresión regular gall[o|(eta)|(ina)]
"""
def ejemplo2(cadena):
    mi_func = { (1, 'g'): 2,
                (2, 'a'): 3,
                (3, 'l'): 4,
                (4, 'l'): 5,
                (5, 'o'): 333,
                (5, 'e'): 6,
                (6, 't'): 7,
                (7, 'a'): 333,
                (5, 'i'): 8,
                (8, 'n'): 9,
                (9, 'a'): 333
                }
    mis_finales = [333]
    return automata(cadena, 1, mi_func, mis_finales)
    
