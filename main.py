from generador import generar_contraseña
from gestor import guardar_contraseña, ver_contraseñas

def menu():
    while True:
        print("\n=== Gestor de Contraseñas ===")
        print("1. Generar y guardar nueva contraseña")
        print("2. Ver contraseñas guardadas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("¿Para qué servicio es la contraseña?: ")
            longitud = int(input("¿De cuántos caracteres?: "))
            contraseña = generar_contraseña(longitud)
            guardar_contraseña(nombre, contraseña)
            print(f"✅ Contraseña para {nombre} guardada exitosamente.")
        elif opcion == "2":
            ver_contraseñas()
        elif opcion == "3":
            print("Saliendo del gestor... ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
