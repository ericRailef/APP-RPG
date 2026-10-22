
from jugador import Jugador
from mago import Mago
from guerrero import Guerrero
from objeto import Objeto

def main():

    # =====================
    #     CREAR Jugador
    # =====================


    nuevo_jugador = Jugador("Eric")

    #=======================
    #       CREAR PJ
    #=======================

    mago = Mago("Gandalf", 10, 100, 90)


    guerrero = Guerrero("Aragorn", 8, 150, 60)


    # ============================
    #     ASOCIAR EL JUGADOR AL PJ
    # ============================

    nuevo_jugador.seleccionar_personaje(mago)

    nuevo_jugador.mostrar_personaje()

    # ===========================
    #     MOSTRAR INFO DEL Mago
    # ===========================

    mago.mostrar_informacion()

    # ===========================
    # ATAQUE DEL MAGO
    # ============================

    mago.atacar()

    #============================
    # HABILIDAD DEL Mago
    # =============================
    mago.usar_habilidad()

    # =================================
    #     agregar objetos al inventario
    # =================================

    pocion = Objeto(
        "Pocion de vida", 
        "Consumible"
    )

    staff = Objeto(
        "Staff del Arcangel", 
        "Arma"
    )

    # ====================================
    #         agregar al inventario
    # ====================================

    mago.inventario.agregar_objeto(staff)
    mago.inventario.agregar_objeto(pocion)

    # ======================================
    #         mostrar inventario
    # ======================================
    mago.inventario.mostrar_inventario()

    # ===============================
    #     Recibir Daño
    # ===============================

    mago.recibir_danio(30)

if __name__ == "__main__":
    main()