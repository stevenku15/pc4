##1. Bitcoins

import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Levanta una excepción si hay un error en la respuesta

        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_usd = n * precio_bitcoin
        print(f"Costo de {n} Bitcoins en USD: ${costo_usd:,.4f}")

if __name__ == "__main__":
    main()

##2. FIGlet
from pyfiglet import Figlet
import random

def seleccionar_fuente_aleatoria(fuentes_disponibles):
    return random.choice(fuentes_disponibles)

def main():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()

    fuente_seleccionada = input("Ingrese el nombre de una fuente (deje en blanco para aleatoria):\n")
    if not fuente_seleccionada:
        fuente_seleccionada = seleccionar_fuente_aleatoria(fuentes_disponibles)
        print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
    elif fuente_seleccionada not in fuentes_disponibles:
        print("La fuente seleccionada no es válida.")
        return

    texto_imprimir = input("Ingrese el texto a imprimir:\n")
    figlet.setFont(font=fuente_seleccionada)
    resultado = figlet.renderText(texto_imprimir)
    print(resultado)

if __name__ == "__main__":
    main()

##3. Imagen perrito

##4. Tareas
def guardar_tabla_multiplicar(numero):
    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")
    print(f"Tabla de multiplicar {numero} guardada en tabla-{numero}.txt")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1].strip())
            else:
                print(f"La línea {linea} no existe en tabla-{numero}.txt")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe")

def main():
    while True:
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == 2:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == 3:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

##5. Bitcoins
import requests
import csv

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        response.raise_for_status()
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_en_archivo_texto(precio):
    with open("precios_bitcoin.txt", "a") as archivo:
        archivo.write(f"{precio}\n")
    print("Precio guardado en precios_bitcoin.txt")

def guardar_en_archivo_csv(precio):
    with open("precios_bitcoin.csv", "a", newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([precio])
    print("Precio guardado en precios_bitcoin.csv")

def main():
    precio = obtener_precio_bitcoin()
    if precio is not None:
        guardar_en_archivo_texto(precio)
        guardar_en_archivo_csv(precio)

if __name__ == "__main__":
    main()

##6.
