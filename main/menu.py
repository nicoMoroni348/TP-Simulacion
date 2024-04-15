import os
from soporte import clear_console, wait_for_enter



while True:
    clear_console()
    print("\n-- Opciones --")
    print("1 - Distribución uniforme(A,B)")
    print("2 - Distribución normal")
    print("3 - Distribución exponencial")
    print("0 - Salir ")

    try:
        opc = int(input("\nIngrese su opción: "))
        
        if opc not in [1, 2, 3, 0]:
            print("\nIngrese un valor dentro de las opciones...")
            wait_for_enter()
        
        elif opc == 1:
            clear_console()
            print("Opción 1")
            print("\nPresione enter para continuar...")
            wait_for_enter()
        
        elif opc == 2:
            clear_console()
            print("Opción 2")
            print("\nPresione enter para continuar...")
            wait_for_enter()
        
        elif opc == 3:
            clear_console()
            print("Opción 3")
            print("\nPresione enter para continuar...")
            wait_for_enter()
        
        elif opc == 0:
            clear_console()
            print("Gracias por utilizar el código")
            print("\nPresione enter para finalizar...")
            wait_for_enter()
            break
    
    except ValueError:
        print("Opción no válida. Por favor ingrese un número entero.")
        wait_for_enter()
