import datetime
import pprint
from pymongo import MongoClient
from pymongo import errors
from os import system
from time import sleep



def mostrarDocumentos (cliente,collection):
    system("cls")
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
    system("cls")
    if collection == 'presidencia':
        #Variables
        dbID = input(f'{bcolors.HEADER}Digite el ID: {bcolors.ENDC}')
        docName = input(f'{bcolors.HEADER}Digite el nombre: {bcolors.ENDC}')
        newDateN = input(f'{bcolors.HEADER}Digite el la fecha aaaa/mm/dd: {bcolors.ENDC}').split('/')
        birthPlace= input(f'{bcolors.HEADER}Digite el lugar de nacimiento: {bcolors.ENDC}')
        cantidadTitulos = int(input(f"{bcolors.HEADER}Digite la cantidad de titulos: {bcolors.ENDC}"))
        for i in range(0,cantidadTitulos):
            aaaa = input(f'{bcolors.HEADER}Digite año de inicio y finalizacion aaaa/aaaa: {bcolors.ENDC}' ).split('/')
            if i == 0:
                titulos = [{'programa': input(f'{bcolors.HEADER}Digite el programa: {bcolors.ENDC}'),'universidad': input(f'{bcolors.HEADER}Digite la universidad: {bcolors.ENDC}'),'nombrePrograma' : input(f'{bcolors.HEADER}Digite el nombre del programa: {bcolors.ENDC}'),'duracionPrograma' : [aaaa[0],aaaa[1]]}]
            else:
                titulos.append({'programa': input(f'{bcolors.HEADER}Digite el programa: {bcolors.ENDC}'),'universidad': input(f'{bcolors.HEADER}Digite la universidad: {bcolors.ENDC}'),'nombrePrograma' : input(f'{bcolors.HEADER}Digite el nombre del programa: {bcolors.ENDC}'),'duracionPrograma' : [aaaa[0],aaaa[1]]})
        cantidadCargosPublicos = int(input(f"{bcolors.HEADER}Digite la cantidad de cargos publicos: {bcolors.ENDC}"))
        for i in range(0,cantidadCargosPublicos):
            aaaa = input(f'{bcolors.HEADER}Digite año de inicio y finalizacion aaaa/aaaa:{bcolors.ENDC}' ).split('/')
            if i == 0:
                cargosPublicos = [{'nombreCargo' : input(f'{bcolors.HEADER}Digite el nombre del cargo publico: {bcolors.ENDC}'), 'duracionCargo': [aaaa[0],aaaa[1]]}]
            else:
                cargosPublicos.append({'nombreCargo' : input(f'{bcolors.HEADER}Digite el nombre del cargo publico: {bcolors.ENDC}'), 'duracionCargo': [aaaa[0],aaaa[1]]})
        lemaCampaña = input(f'{bcolors.HEADER}Digite el lema de campaña: {bcolors.ENDC}')
        partidoPolitico = input(f'{bcolors.HEADER}Digite el partido politico: {bcolors.ENDC}')
        edad = int(input(f'{bcolors.HEADER}Digite la edad: {bcolors.ENDC}'))
        identificacion = input(f'{bcolors.HEADER}Digite el numero de identificacion: {bcolors.ENDC}')
        tipoDocumento = input(f'{bcolors.HEADER}Digite el tipo de documento C | P: {bcolors.ENDC}')
        cantidadProfesiones = int(input(f'{bcolors.HEADER}Digite la cantidad de profesiones: {bcolors.ENDC}'))
        for i in range(0,cantidadProfesiones):
            if i == 0:
                profesiones = [input(f'{bcolors.HEADER}Digite la profesion {i+1}: {bcolors.ENDC}')]
            else:
                profesiones.append(input(f'{bcolors.HEADER}Digite la profesion {i+1}: {bcolors.ENDC}'))

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
            print(f"{bcolors.OKGREEN}Se ha agregado el documento Exitosamente{bcolors.ENDC}")
        except Exception as e :
            print(f'{bcolors.FAIL}No se logro insertar el documento {e}{bcolors.ENDC}')
    elif collection == 'vicepresidencia':
        #Variables
        dbID = input(f'{bcolors.HEADER}Digite el ID: {bcolors.ENDC}')
        docName = input(f'{bcolors.HEADER}Digite el nombre: {bcolors.ENDC}')
        newDateN = input(f'{bcolors.HEADER}Digite el la fecha aaaa/mm/dd: {bcolors.ENDC}').split('/')
        birthPlace= input(f'{bcolors.HEADER}Digite el lugar de nacimiento: {bcolors.ENDC}')
        cantidadTitulos = int(input(f'{bcolors.HEADER}Digite la cantidad de titulos: {bcolors.ENDC}'))
        for i in range(0,cantidadTitulos):
            aaaa = input(f'{bcolors.HEADER}Digite año de inicio y finalizacion aaaa/aaaa:{bcolors.ENDC} ').split('/')
            if i == 0:
                titulos = [{'programa': input(f'{bcolors.HEADER}Digite el programa: {bcolors.ENDC}'),'universidad': input(f'{bcolors.HEADER}Digite la universidad: {bcolors.ENDC}'),'nombrePrograma' : input(f'{bcolors.HEADER}Digite el nombre del programa: {bcolors.ENDC}'),'duracionPrograma' : [aaaa[0],aaaa[1]]}]
            else:
                titulos.append({'programa': input(f'{bcolors.HEADER}Digite el programa: {bcolors.ENDC}'),'universidad': input(f'{bcolors.HEADER}Digite la universidad: {bcolors.ENDC}'),'nombrePrograma' : input(f'{bcolors.HEADER}Digite el nombre del programa: {bcolors.ENDC}'),'duracionPrograma' : [aaaa[0],aaaa[1]]})
        cantidadCargosPublicos = int(input(f'{bcolors.HEADER}Digite la cantidad de cargos publicos: {bcolors.ENDC}'))
        for i in range(0,cantidadCargosPublicos):
            aaaa = input(f'{bcolors.HEADER}Digite año de inicio y finalizacion aaaa/aaaa: {bcolors.ENDC}').split('/')
            if i == 0:
                cargosPublicos = [{'nombreCargo' : input(f'{bcolors.HEADER}Digite el nombre del cargo publico: '), 'duracionCargo': [aaaa[0],aaaa[1]]}]
            else:
                cargosPublicos.append({'nombreCargo' : input(f'{bcolors.HEADER}Digite el nombre del cargo publico: {bcolors.ENDC}'), 'duracionCargo': [aaaa[0],aaaa[1]]})
        lemaCampaña = input(f'{bcolors.HEADER}Digite el lema de campaña: {bcolors.ENDC}')
        partidoPolitico = input(f'{bcolors.HEADER}Digite el partido politico: {bcolors.ENDC}')
        edad = int(input(f'{bcolors.HEADER}Digite la edad: '))
        identificacion = input(f'{bcolors.HEADER}Digite el numero de identificacion: {bcolors.ENDC}')
        tipoDocumento = input(f'{bcolors.HEADER}Digite el tipo de documento C | P: {bcolors.ENDC}')
        idCandidato = input(f'{bcolors.HEADER}Digite la ID del candidato presidencial: {bcolors.ENDC}')
        cantidadProfesiones = int(input(f'{bcolors.HEADER}Digite la cantidad de profesiones: {bcolors.ENDC}'))
        for i in range(0,cantidadProfesiones):
            if i == 0:
                profesiones = [input(f'{bcolors.HEADER}Digite la profesion {i+1}{bcolors.ENDC}: ')]
            else:
                profesiones.append(input(f'{bcolors.HEADER}Digite la profesion {i+1}{bcolors.ENDC}: '))
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
            print(f"{bcolors.OKGREEN}Se ha agregado el documento Exitosamente{bcolors.ENDC}")
            system("cls")
        except Exception as e :
            print(f'{bcolors.FAIL}No se logro insertar el documento {e}{bcolors.ENDC}')
    sleep(1.5)
    system("cls")

def actualizarDocumento(cliente,collection):
    system("cls")
    targetID = input(f'{bcolors.HEADER}Digite la ID del documento a modificar: {bcolors.ENDC}')
    if collection == 'presidencia':
        pprint.pprint(cliente.Proyecto3.presidencia.find_one({'_id': targetID}))
        print(f'{bcolors.HEADER} atributo valorActual {bcolors.ENDC}')
        actualValues = input().split()
        print(f'{bcolors.HEADER}atributo nuevoValor{bcolors.ENDC}')
        newValues = input().split()
        try:
            cliente.Proyecto3.presidencia.update_one({actualValues[0] : actualValues[1]},{'$set' : {newValues[0] : newValues[1]}})
            print(f'{bcolors.OKGREEN}Documento modificado exitosamente{bcolors.ENDC}')
        except Exception as e:
            print(f'{bcolors.FAIL}No se logro modificar el documento {e}{bcolors.ENDC}')
    elif collection == 'vicepresidencia':
        pprint.pprint(cliente.Proyecto3.vicepresidencia.find_one({'_id': targetID}))
        print(f'{bcolors.HEADER} atributo valorActual {bcolors.ENDC}')
        actualValues = input().split()
        print(f'{bcolors.HEADER}atributo nuevoValor{bcolors.ENDC}')
        newValues = input().split()
        try:
            cliente.Proyecto3.vicepresidencia.update_one({actualValues[0] : actualValues[1]},{'$set' : {newValues[0] : newValues[1]}})
            print(f'{bcolors.OKGREEN}Documento modificado exitosamente{bcolors.ENDC}')
        except Exception as e:
            print(f'{bcolors.FAIL}No se logro modificar el documento {e}{bcolors.ENDC}')
    sleep(1.5)
    system("cls")

def eliminarDocumento(cliente,collection):
    system("cls")
    #variavbles
    targetID = input(f'{bcolors.HEADER}Digite la ID del documento a eliminar: {bcolors.ENDC}')
    if collection == 'presidencia':
        try:
            cliente.Proyecto3.presidencia.delete_one({'_id' : targetID })
            print(f'{bcolors.FAIL}Se ha eliminado el documento satisfactoriamente{bcolors.ENDC}')
        except Exception as e:
            print(f'{bcolors.FAIL} No se logro eliminar el documento indicado {e}{bcolors.ENDC}')
    elif collection == 'vicepresidencia':
        try:
            cliente.Proyecto3.vicepresidencia.delete_one({'_id' : targetID })
            print(f'{bcolors.FAIL}Se ha eliminado el documento satisfactoriamente{bcolors.ENDC}')
        except Exception as e:
            print(f'{bcolors.FAIL}No se logro eliminar el documento indicado {e}{bcolors.ENDC}')
    sleep(1.5)
    system("cls")

def consulta(cliente):    
    for document in cliente.Proyecto3.presidencia.find():
            print(f'''
==================================================================================
{bcolors.HEADER}Nombre Presidente: {bcolors.ENDC}{document["nombreCompleto"]}
{bcolors.HEADER}Edad: {bcolors.ENDC}{document["edad"]}
{bcolors.HEADER}Lema de campaña: {bcolors.ENDC}{document["lemaCampaña"]}
    ''')
            for jdocument in cliente.Proyecto3.vicepresidencia.find():
                if (jdocument["idCandidato"] == document["_id"]):
                                print(f'''
{bcolors.HEADER}Nombre VicePresidente: {bcolors.ENDC}{jdocument["nombreCompleto"]}
{bcolors.HEADER}Edad: {bcolors.ENDC}{jdocument["edad"]}
{bcolors.HEADER}Lema de campaña: {bcolors.ENDC}{jdocument["lemaCampaña"]}
===================================================================================
    ''')
                                continue
    if input("Presiona una tecla para continuar") != "":
            pass
    system("cls")

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
    5. consulta
    0. Salir
        """)
        try:
            opcion = int(input())
        except ValueError:
            print("Digite una opcion valida")
            sleep(1.5)
            main()
        if(opcion == 1):
            system("cls")
            print(f"{bcolors.HEADER}1.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION1}{bcolors.ENDC}\n{bcolors.HEADER}2.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION2}{bcolors.ENDC}")
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                mostrarDocumentos(cliente,MONGO_COLLECTION1)
            else:
                mostrarDocumentos(cliente,MONGO_COLLECTION2)
        elif(opcion == 2):
            system("cls")
            print(f"{bcolors.HEADER}1.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION1}{bcolors.ENDC}\n{bcolors.HEADER}2.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION2}{bcolors.ENDC}")
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                crearDocumento(cliente,MONGO_COLLECTION1)
            else:
                crearDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 3):
            system("cls")
            print(f"{bcolors.HEADER}1.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION1}{bcolors.ENDC}\n{bcolors.HEADER}2.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION2}{bcolors.ENDC}")
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                actualizarDocumento(cliente,MONGO_COLLECTION1)
            else:
                actualizarDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 4):
            system("cls")
            print(f"{bcolors.HEADER}1.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION1}{bcolors.ENDC}\n{bcolors.HEADER}2.{bcolors.ENDC} {bcolors.UNDERLINE}{MONGO_COLLECTION2}{bcolors.ENDC}")
            if(int(input("Seleccione que coleccion quiere usar: ")) == 1):
                eliminarDocumento(cliente,MONGO_COLLECTION1)
            else:
                eliminarDocumento(cliente,MONGO_COLLECTION2)
        elif(opcion == 5):
            system("cls")
            consulta(cliente)
        elif(opcion == 0):
            print(f"{bcolors.WARNING}Conexion Finalizada{bcolors.ENDC}")
            sleep(1.5)
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
