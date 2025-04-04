from src.controllers.manager import Manager

from src.controllers.strategies.q_nodes_memo import QNodesMemo


def iniciar():
    """Punto de entrada principal"""
                    # ABCD #
    estado_inicial = "1000000000"
    condiciones =    "1111111111"
    alcance =        "1101101101"
    mecanismo =      "1010101010"

    gestor_sistema = Manager(estado_inicial)

    ### Ejemplo de solución mediante módulo de fuerza bruta ###
    analizador_fb = QNodesMemo(gestor_sistema)
    sia_uno = analizador_fb.aplicar_estrategia(
        condiciones,
        alcance,
        mecanismo,
    )
    print(sia_uno)
