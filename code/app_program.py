ls_viajeros = []
import os
viajero = ''
def fnt_limpiar():
    os.system("cls")
    print('Autor: jose daniel nuñez😘 \ncopyrigth-© 2024 \nUCLAM\n')

def fnt_agente(op):
    fnt_limpiar()
    global sw
    viajero = ''
    if op == '1':
        
        print('<<< AGREGAR VIAJERO >>>\n')
        nombre = input('nombre: ' )
        apellido = input('apellido: ')
        edad = input('edad: ')
        if (int(edad)> 0 and int(edad) <=25):
            viajero = nombre + ' ' + apellido + ' ' + edad
            ls_viajeros.append(viajero)
            print('viajero agregado')
            input('presione <ENTER> para continuar')
        else:
            print('edad incorrecta')
            input('presione <ENTER> para continuar')
    if op == '2':
        fnt_limpiar()
        print('<<< MOSTRAR VIAJEROS >>>\n')
        if len(ls_viajeros) ==0:
            print('no hay viajeros registrados')
            input('presione <ENTER> para continuar')
        else:
            for i in ls_viajeros:
                print(i)
            input('presione <ENTER> para continuar')
    if op == '3':
        sw = False


sw = True
while sw == True:
    opcion = input('<<< 😈MENU PRINCIPAL😈 >>>\n\n1. agregar \n2. mostrar \n3. salir \n➡️   ')
    fnt_agente(opcion)