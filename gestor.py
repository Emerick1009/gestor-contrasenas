import os

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

def buscar_contraseña(nombre, archivo="contraseñas_guardadas.txt"):
    try:
        with open(archivo,"r") as f:
            for linea in f:
                if linea.lower().startswith(nombre.lower() + ":"):
                    print(f"{linea.strip()}")
                    return
            print("No se encontró esa contraseña")
    except FileNotFoundError:
        print("No se encontro el archivo de contraseñas")

def eliminar_contraseña(nombre, archivo="contraseñas_guardadas.txt"):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            eliminada = False
            for linea in lineas: 
                if not linea.lower().startswith(nombre.lower() + ":"):
                    f.write(linea)
                else:
                    eliminada = True
                if eliminada:
                    print(f"Contraseña de {nombre} eliminada.")
                else:
                    print("No se encontró esa contraseña.")
    except FileNotFoundError:
        print("No hay contraseñas guardadas aun.")

def actualizar_contraseña(nombre,nueva, archivo="contraseñas_guardadas.txt"):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            actualizada = False
            for linea in lineas:
                if linea.lower().startswith(nombre.lower() + ":"):
                    f.write(f"{nombre}: {nueva}\n")
                    actualizada = True
                else:
                    f.write(linea)
            if actualizada:
                print(f"Contraseña de {nombre} actualizada.")
            else:
                print("No se encontro esa contraseña")
    except FileNotFoundError:
        print("No hay contraseñas guardadas aun.")