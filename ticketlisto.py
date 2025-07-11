#SISTEMA DE TICKETS Correa :p

import pickle
import random
import os
import sys

# Función para generar un código aleatorio
def generar_codigo():
    return random.randint(1000, 9999)

# Función para cargar los datos desde el archivo pickle
def cargar_datos():
    if os.path.exists('datos.pickle'):
        with open('datos.pickle', 'rb') as file:
            return pickle.load(file)
    else:
        return {}

# Función para guardar los datos en el archivo pickle
def guardar_datos(datos):
    with open('datos.pickle', 'wb') as file:
        pickle.dump(datos, file)

# Función para ingresar y almacenar datos
def ingresar_datos():
    datos_guardados = cargar_datos()
    
    codigo = generar_codigo()
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese su sector: ")
    asunto = input("Ingrese el asunto: ")
    problema = input("Ingrese un mensaje detallando el problema: ")
    
    # Verificar si el código ya existe
    while codigo in datos_guardados:
        codigo = generar_codigo()
    
    # Asignar los datos al código generado
    datos_guardados[codigo] = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'problema': problema
    }
    
    # Guardar los datos actualizados
    guardar_datos(datos_guardados)
    
    print(f"""
                      ┌──────────────────────────────────────────────────────────── ┐
                      │               Se generó el siguiente TICKET                  │
                      │                                                             │
                      │    ❤︎ Su nombre: {nombre}       ❤︎ N de ticket: {codigo}          │ 
                      │    ❤︎ Sector: {sector}                                           │
                      │    ❤︎ Asunto: {asunto}                                          │
                      │    ❤︎ Mensaje:{problema}                                       │
                      │                                                              │
                      │   Por favor, recuerde su número de ticket: {codigo}           │
                      │  Los datos han sido almacenados correctamente      ૮_‘_ა     │
                      │                                                 ૮  • ﻌ • ა  │                                         
                      │                                                  (  ა  ૮ )   │
                      └────────────────────────────────────────────────────────────┘
                            \n""") #no sé por qué se descajetan las lineas de la derecha

# Función para acceder a los datos mediante el código
def acceder_datos():
    datos_guardados = cargar_datos()
    
    codigo = int(input("Por favor, ingrese el Número del ticket que desea buscar: "))
    
    if codigo in datos_guardados:
        datos = datos_guardados[codigo]
        print(f"Nombre: {datos['nombre']}")
        print(f"Sector: {datos['sector']}")
        print(f"Asunto: {datos['asunto']}")
        print(f"Mensaje: {datos['problema']}")
    else:
        print("No se encontraron datos para el número de ticket ingresado.")





def menu_principal():
    control = True   
    while control == True:
        print("""
            
        Bienvenido al sistema de TICKETS
        
        Menú
        
        1- Generar un nuevo ticket
        2- Leer un ticket
        3- Salir   
    \n""")

        n= input("Seleccione una opción: ")#Alta de Ticket

        if n.isdigit():
            if int(n) == 1:
                nuevo='SI'
                while nuevo == 'SI':
                    ingresar_datos()

                    nuevo= input("¿Desea generar un nuevo TICKET?  SI/NO  *solo se admiten mayúsculas*:  ")
                    if nuevo == 'SI': #si agrego or 'si' el elif/else debajo ya no funciona
                        nuevo == 'SI'
                    elif nuevo == 'NO':
                        control = True #Regresa al Menú, como indica la consigna
                    else:
                        print("ERROR: el usuario no ha seleccionado una opción valida")



            if int(n) == 2:
                leerotro= 'SI'
                while leerotro == 'SI':
                    acceder_datos()

                    leerotro = input("¿Deseea acceder a otro ticket? (SI/NO) *solo se admiten mayúsculas*:  ")#Dar la opción de leer otro ticket
                    if leerotro == 'SI': 
                        leerotro == 'SI'
                    elif leerotro == 'NO':
                        control = True #Regresa al Menú
                    else:
                        print("ERROR: el usuario no ha seleccionado una opción valida")


            if int(n) == 3:
                confirmar= input("¿Está seguro de que quiere salir del sistema?  SI/NO   *solo se admiten mayúsculas*:  ")#Que el usuario confirme el cierre, lo pide la consigna
                if confirmar == 'NO': #si agrego or 'no' el elif/else debajo ya no funciona :/
                        control = True
                        print("Volviendo al menú...")
                elif confirmar == 'SI':
                    control = False
                    print(f"""                        
        Cerrando...                  
        Gracias por usar nuestro sistema!⠀❤︎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                          \n""")   
                    sys.exit() #con este comando cierra la ejecucion del programa
                else:
                    print("ERROR: el usuario no ha ingresado una opción válida")     
        else:
            print ("Lo sentimos, solo se admite el ingreso de un número\nvolviendo al menú...")

 # Llamamos a la función principal del menú
if __name__ == "__main__":
    menu_principal()  