import os
import numpy
import time

hotel = numpy.zeros((2,10), int)

lista_ruts = []
lista_nombres = []
lista_mascotas = []
lista_totales = []
lista_filas =[]
lista_columnas = []
lista_letras  = ['A','B','C','D','E']
lista_habitaciones = [1,2,3,4,5,6,7,8,9,10]

#Mostrar menu y validar opcion:

def mostrar_menu():
    os.system('cls')
    print("""MENÚ
    1. Guardar datos mascota
    2. Buscar
    3. Retirarse
    4. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("Opcion invalida")
        except:
            print("ERROR! debe ingresar un numero")

#Opcion 1:

def validar_rut_dueño():
    while True:
        try:
            rut = int(input("Ingrese su rut (Sin puntos ni digito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR rut entre 10000000 y 99999999")
        except:
            print("ERROR! debe ingresar un numero entero")

def validar_nombre_dueño():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR debe tener al menos 3 letras")
    
def validar_id_dueño():
    while True:
        try:
            edad = int(input("Ingrese edad(entre 0 y 100): "))
            if edad >= 0 and edad <= 100:
                return edad
            else:
                print("ERROR edad fuera de rango de 0 y 100")
        except:
            print("ERROR! debe ingresar un numero entero")

def validar_nombre_mascota():
    while True:
        nombre_mascota = input("Ingrese su nombre: ")
        if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
            return nombre_mascota
        else:
            print("ERROR debe tener al menos 3 letras")

def cantidad_dias_mascota():
    while True:
        try:
            cant_dias_mascota = int(input("Ingrese cantidad de dias que permanecera su mascota:"))
            if cant_dias_mascota >=1:
                return cant_dias_mascota
            else:
                print("Cantidad de dias ingresado invalidas:")
        except:
            print("ERROR! Debe ingresar un numero entero!")

#Ver mascota segura:


def ver_habitacion():
    for x in range(2):
        print("PISO: ",lista_habitaciones[x], end=" ")
        for y in range (10):
            print(hotel[x][y], end=" ")
        print()
    time.sleep(3)

def validar_habitacion():
    while True:
        try:
            habitacion = int(input("Ingrese numero de habitacion: "))
            if habitacion in lista_habitaciones:
                return habitacion
            else:
                print("Habitacion invalida")
        except:
            print("Debe ingresar un numero entero ")
    
def comprar():
    rut = validar_rut_dueño
    nombre = validar_nombre_dueño
    dinero = int("INGRSE DINERO:")
    if dinero < cant_total:
        print("Dinero suficiente")

def buscar():
    rut = int(input("Ingrese rut:"))
    if rut not in lista_ruts:
        print("ERROR!")




