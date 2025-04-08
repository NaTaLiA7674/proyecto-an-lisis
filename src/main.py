from src.controllers.manager import Manager
import time
from src.controllers.strategies.q_nodes_memo import QNodesMemo


def iniciar():
    """Punto de entrada principal"""
                    # ABCD #
    inicio = time.time()
    estado_inicial = "100000000000000"
    condiciones =    "111111111111111"
    alcance =        "111111111111111"
    mecanismo =      "111111111111111"

    gestor_sistema = Manager(estado_inicial)

    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_fb = QNodesMemo(gestor_sistema)

    sia_uno = analizador_fb.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )
    print(sia_uno)

    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
