def guardar_contraseña(nombre, contraseña, archivo="contraseñas_guardadas.txt"):
    with open(archivo, "a") as f:
        f.write(f"{nombre}: {contraseña}\n")

def ver_contraseñas(archivo="contraseñas_guardadas.txt"):
    try:
        with open(archivo, "r") as f:
            contenido = f.readlines()
            if not contenido:
                print("No hay contraseñas guardadas todavía.")
            else:
                print("\n--- Contraseñas guardadas ---")
                for linea in contenido:
                    print(linea.strip())
    except FileNotFoundError:
        print("No se encontró el archivo de contraseñas.")
