
import Funciones as fn


while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        fn.validar_rut_dueño()
        fn.validar_nombre_dueño()
        fn.validar_nombre_mascota()
        fn.cantidad_dias_mascota()
    elif opcion==2:
        fn.ver_habitacion_disponible()
    elif opcion==3:
        fn.ver_habitacion()
    elif opcion==4:
        pass
    else:
        print("")
    