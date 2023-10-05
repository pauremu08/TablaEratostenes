def criba_eratostenes(n):
    # Crear una lista de booleanos para representar los números del 2 hasta n
    # Inicialmente, todos los números se consideran primos (True)
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for p in range(2, int(n**0.5) + 1):
        if es_primo[p]:
            # Si p es primo, marcar todos sus múltiplos como no primos
            for i in range(p * p, n + 1, p):
                es_primo[i] = False

    # Recorrer la lista y recopilar los números primos
    primos = [i for i in range(2, n + 1) if es_primo[i]]
    return primos

# Solicitar al usuario que ingrese un número máximo
try:
    limite = int(input("Ingrese un número máximo para encontrar todos los números primos hasta ese número: "))
    if limite < 2:
        print("No hay números primos en ese rango.")
    else:
        lista_primos = criba_eratostenes(limite)
        print("Números primos hasta", limite, ":", lista_primos)

        # Preguntar al usuario si desea guardar la lista en un archivo .txt
        guardar_archivo = input("¿Desea guardar la lista en un archivo .txt? (Sí/No): ")
        if guardar_archivo.lower() == "si":
            nombre_archivo = input("Ingrese el nombre del archivo (sin la extensión .txt): ")
            with open(f"{nombre_archivo}.txt", "w") as archivo:
                for primo in lista_primos:
                    archivo.write(f"{primo}\n")
            print(f"La lista de números primos ha sido guardada en {nombre_archivo}.txt")
except ValueError:
    print("Por favor, ingrese un número válido.")
