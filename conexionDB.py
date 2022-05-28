import datetime
import pprint
from pymongo import MongoClient
from pymongo import errors
from os import system
from time import sleep



def mostrarDocumentos (cliente,collection):
    if collection == 'presidencia':
        for document in cliente.Proyecto3.presidencia.find():
            print(f'''
{bcolors.HEADER}Nombre: {bcolors.ENDC}{document["nombreCompleto"]}
{bcolors.HEADER}Tipo ID: {bcolors.ENDC}{document["tipoDocumento"]}
{bcolors.HEADER}Identidicacion: {bcolors.ENDC}{document["identificacion"]}
{bcolors.HEADER}Fecha Nacimiento: {bcolors.ENDC}{str(document["fechaNacimiento"])}
{bcolors.HEADER}Edad: {bcolors.ENDC}{document["edad"]}
{bcolors.HEADER}Lugar Nacimiento: {bcolors.ENDC}{document["lugarNacimiento"]}
{bcolors.HEADER}Titulos: {bcolors.ENDC}{document["titulos"]}
{bcolors.HEADER}Cargos Publicos: {bcolors.ENDC}{document["cargosPublicos"]}
{bcolors.HEADER}Lema de campaña: {bcolors.ENDC}{document["lemaCampaña"]}
{bcolors.HEADER}Partido politico: {bcolors.ENDC}{document["partidoPolitico"]}
{bcolors.HEADER}Profesiones: {bcolors.ENDC}{document["profesion"]}
''')

            print("========================================================================================================================================")
        if input("Presiona una tecla para continuar") != "":
            pass
    elif collection == 'vicepresidencia':
        for document in cliente.Proyecto3.vicepresidencia.find():
            print(f'''
{bcolors.HEADER}Nombre: {bcolors.ENDC}{document["nombreCompleto"]}
{bcolors.HEADER}Tipo ID: {bcolors.ENDC}{document["tipoDocumento"]}
{bcolors.HEADER}Identidicacion: {bcolors.ENDC}{document["identificacion"]}
{bcolors.HEADER}Fecha Nacimiento: {bcolors.ENDC}{str(document["fechaNacimiento"])}
{bcolors.HEADER}Edad: {bcolors.ENDC}{document["edad"]}
{bcolors.HEADER}Lugar Nacimiento: {bcolors.ENDC}{document["lugarNacimiento"]}
{bcolors.HEADER}Titulos: {bcolors.ENDC}{document["titulos"]}
{bcolors.HEADER}Cargos Publicos: {bcolors.ENDC}{document["cargosPublicos"]}
{bcolors.HEADER}Lema de campaña: {bcolors.ENDC}{document["lemaCampaña"]}
{bcolors.HEADER}Partido politico: {bcolors.ENDC}{document["partidoPolitico"]}
{bcolors.HEADER}Profesiones: {bcolors.ENDC}{document["profesion"]}
''')
            print("========================================================================================================================================")
        if input("Presiona una tecla para continuar") != "":
            pass
    system("cls")

def crearDocumento(cliente,collection):
    if collection == 'presidencia':
        #Variables
        dbID = input('Digite el ID: ')
        docName = input('Digite el nombre: ')
        newDateN = input('Digite el la fecha aaaa/mm/dd: ').split('/')
        birthPlace= input('Digite el lugar de nacimiento: ')
        cantidadTitulos = int(input("Digite la cantidad de titulos: "))
        for i in range(0,cantidadTitulos):
            aaaa = input('Digite año de inicio y finalizacion aaaa/aaaa:' ).split('/')
            if i == 0:
                titulos = [{'programa': input('Digite el programa: '),'universidad': input('Digite la universidad: '),'nombrePrograma' : input('Digite el nombre del programa: '),'duracionPrograma' : [aaaa[0],aaaa[1]]}]
            else:
                titulos.append({'programa': input('Digite el programa: '),'universidad': input('Digite la universidad: '),'nombrePrograma' : input('Digite el nombre del programa: '),'duracionPrograma' : [aaaa[0],aaaa[1]]})
        cantidadCargosPublicos = int(input("Digite la cantidad de cargos publicos: "))
        for i in range(0,cantidadCargosPublicos):
            aaaa = input('Digite año de inicio y finalizacion aaaa/aaaa:' ).split('/')
            if i == 0:
                cargosPublicos = [{'nombreCargo' : input('Digite el nombre del cargo publico: '), 'duracionCargo': [aaaa[0],aaaa[1]]}]
            else:
                cargosPublicos.append({'nombreCargo' : input('Digite el nombre del cargo publico: '), 'duracionCargo': [aaaa[0],aaaa[1]]})
        lemaCampaña = input('Digite el lema de campaña: ')
        partidoPolitico = input('Digite el partido politico: ')
        edad = int(input('Digite la edad: '))
        identificacion = input('Digite el numero de identificacion: ')
        tipoDocumento = input('Digite el tipo de documento C | P: ')
        cantidadProfesiones = int(input("Digite la cantidad de profesiones: "))
        for i in range(0,cantidadProfesiones):
            if i == 0:
                profesiones = [input(f'Digite la profesion {i+1}: ')]
            else:
                profesiones.append(input(f'Digite la profesion {i+1}: '))


        newDocumentPresidente = {
        '_id': dbID,
        'nombreCompleto': docName,
        'fechaNacimiento': datetime.datetime(int(newDateN[0]),int(newDateN[1]),int(newDateN[2])),
        'lugarNacimiento': birthPlace,
        'titulos': titulos,
        'cargosPublicos': cargosPublicos,
        'lemaCampaña': lemaCampaña,
        'partidoPolitico': partidoPolitico,
        'edad': edad,
        'identificacion': identificacion,
        'tipoDocumento': tipoDocumento,
        'profesion': profesiones
        }
        
        try:
            cliente.Proyecto3.presidencia.insert_one(newDocumentPresidente)
            print("Se ha agregado el documento Exitosamente")
            system("cls")
        except Exception as e :
            print(f'No se logro insertar el documento {e}')


    elif collection == 'vicepresidencia':
        #Variables
        dbID = input('Digite el ID: ')
        docName = input('Digite el nombre: ')
        newDateN = input('Digite el la fecha aaaa/mm/dd: ').split('/')
        birthPlace= input('Digite el lugar de nacimiento: ')
        cantidadTitulos = int(input("Digite la cantidad de titulos: "))
        for i in range(0,cantidadTitulos):
            aaaa = input('Digite año de inicio y finalizacion aaaa/aaaa:' ).split('/')
            if i == 0:
                titulos = [{'programa': input('Digite el programa: '),'universidad': input('Digite la universidad: '),'nombrePrograma' : input('Digite el nombre del programa: '),'duracionPrograma' : [aaaa[0],aaaa[1]]}]
            else:
                titulos.append({'programa': input('Digite el programa: '),'universidad': input('Digite la universidad: '),'nombrePrograma' : input('Digite el nombre del programa: '),'duracionPrograma' : [aaaa[0],aaaa[1]]})
        cantidadCargosPublicos = int(input("Digite la cantidad de cargos publicos: "))
        for i in range(0,cantidadCargosPublicos):
            aaaa = input('Digite año de inicio y finalizacion aaaa/aaaa:' ).split('/')
            if i == 0:
                cargosPublicos = [{'nombreCargo' : input('Digite el nombre del cargo publico: '), 'duracionCargo': [aaaa[0],aaaa[1]]}]
            else:
                cargosPublicos.append({'nombreCargo' : input('Digite el nombre del cargo publico: '), 'duracionCargo': [aaaa[0],aaaa[1]]})
        lemaCampaña = input('Digite el lema de campaña: ')
        partidoPolitico = input('Digite el partido politico: ')
        edad = int(input('Digite la edad: '))
        identificacion = input('Digite el numero de identificacion: ')
        tipoDocumento = input('Digite el tipo de documento C | P: ')
        idCandidato = input('Digite la ID del candidato presidencial: ')
        cantidadProfesiones = int(input("Digite la cantidad de profesiones: "))
        for i in range(0,cantidadProfesiones):
            if i == 0:
                profesiones = [input(f'Digite la profesion {i+1}: ')]
            else:
                profesiones.append(input(f'Digite la profesion {i+1}: '))
        newDocumentVicepresidente = {
        '_id': dbID,
        'nombreCompleto': docName,
        'fechaNacimiento': newDateN,
        'lugarNacimiento': birthPlace,
        'titulos': titulos,
        'cargosPublicos': cargosPublicos,
        'lemaCampaña': lemaCampaña,
        'partidoPolitico': partidoPolitico,
        'edad': edad,
        'identificacion': identificacion,
        'tipoDocumento': tipoDocumento,
        'idCandidato': idCandidato,
        'profesion': profesiones
    }
        try:
            cliente.Proyecto3.presidencia.insert_one(newDocumentVicepresidente)
            print("Se ha agregado el documento Exitosamente")
            system("cls")
        except Exception as e :
            print(f'No se logro insertar el documento {e}')

def actualizarDocumento(cliente,collection):
    targetID = input('Digite la ID del documento a modificar: ')
    if collection == 'presidencia':
        pprint.pprint(cliente.Proyecto3.presidencia.find_one({'_id': targetID}))
        print('atributo valorActual')
        actualValues = input().split()
        print('atributo nuevoValor')
        newValues = input().split()
        try:
            cliente.Proyecto3.presidencia.update_one({actualValues[0] : actualValues[1]},{'$set' : {newValues[0] : newValues[1]}})
            print('Documento modificado exitosamente')
        except Exception as e:
            print(f'No se logro modificar el documento {e}')
    elif collection == 'vicepresidencia':
        pprint.pprint(cliente.Proyecto3.vicepresidencia.find_one({'_id': targetID}))
        print('atributo valorActual')
        actualValues = input().split()
        print('atributo nuevoValor')
        newValues = input().split()
        try:
            cliente.Proyecto3.vicepresidencia.update_one({actualValues[0] : actualValues[1]},{'$set' : {newValues[0] : newValues[1]}})
            print('Documento modificado exitosamente')
        except Exception as e:
            print(f'No se logro modificar el documento {e}')

def eliminarDocumento(cliente,collection):
    #variavbles
    targetID = input('Digite la ID del documento a eliminar: ')
    if collection == 'presidencia':
        try:
            cliente.Proyecto3.presidencia.delete_one({'_id' : targetID })
            print(f'Se ha eliminado el documento satisfactoriamente')
        except Exception as e:
            print(f'No se logro eliminar el documento indicado {e}')
    elif collection == 'vicepresidencia':
        try:
            cliente.Proyecto3.vicepresidencia.delete_one({'_id' : targetID })
            print(f'Se ha eliminado el documento satisfactoriamente')
        except Exception as e:
            print(f'No se logro eliminar el documento indicado {e}')

def consultas(cliente,collection):
    pass

def menu(cliente,MONGO_URI):
    #Constantes
    MONGO_COLLECTION1 = "presidencia" #Nombre de las colecciones que estan en la base de datos
    MONGO_COLLECTION2 = "vicepresidencia"
    opcion = -1
    while opcion != 0:
        print(f"""
{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.WARNING}Conexion a la DB exitosa: {MONGO_URI}{bcolors.ENDC}

    1. Mostrar todos los documentos de una coleccion
    2. Crear un nuevo documento
    3. Actualizar un documento
    4. Eliminar un documento
    5. Consultas
    0. Salir
        """)
        try:
            opcion = int(input())
        except ValueError:
            print("Digite una opcion valida")
            sleep(2)
            main()
        if(opcion == 1):
            system("cls")
            print("1. " + MONGO_COLLECTION1 + "\n" + "2. " + MONGO_COLLECTION2)
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                mostrarDocumentos(cliente,MONGO_COLLECTION1)
            else:
                mostrarDocumentos(cliente,MONGO_COLLECTION2)
        elif(opcion == 2):
            system("cls")
            print("1. " + MONGO_COLLECTION1 + "\n" + "2. " + MONGO_COLLECTION2)
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                crearDocumento(cliente,MONGO_COLLECTION1)
            else:
                crearDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 3):
            system("cls")
            print("1. " + MONGO_COLLECTION1 + "\n" + "2. " + MONGO_COLLECTION2)
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                actualizarDocumento(cliente,MONGO_COLLECTION1)
            else:
                actualizarDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 4):
            system("cls")
            print("1. " + MONGO_COLLECTION1 + "\n" + "2. " + MONGO_COLLECTION2)
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                eliminarDocumento(cliente,MONGO_COLLECTION1)
            else:
                eliminarDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 5):
            system("cls")
            print("1. " + MONGO_COLLECTION1 + "\n" + "2. " + MONGO_COLLECTION2)
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                consultas(cliente,MONGO_COLLECTION1)
            else:
                consultas(cliente,MONGO_COLLECTION2)
        elif(opcion == 0):
            print("Conexion Finalizada")
            sleep(1)
            break
        

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    #Constantes
    MONGO_TTL = 1000 #Tiempo de espera para la conexion de la DB

    MONGO_HOST = "localhost" #HostName de la BDmongo (normalmente localhost)
    MONGO_PORT = "27017"  #Puerto de la DBmongo (normalmente 27017)
    MONGO_DB = "Proyecto3"  #Nombre de la DB

    MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/" + MONGO_DB

    system("cls")
    try:
        cliente = MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONGO_TTL)
        cliente.server_info()
    except errors.ServerSelectionTimeoutError as exceedTTL:
        print(f'tiempo excedido {exceedTTL}')
    except errors.ConnectionFailure as connectionFailure:
        print(f'Error en la conexion {connectionFailure}')
    menu(cliente,MONGO_URI)


if __name__ == "__main__":
    main()
