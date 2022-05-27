ceroDiez = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]
diezVeinte = ["once", "doce","trece","catorce", "quince", "diezciseis", "diecisiete", "dieciocho", "diecinueve"]
veinteCien = ["veinte", "treinta","cuarenta","cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
cientos = "cientos"



moneda = input("Ingrese el nombre de la moneda ")

def convertir():
    respuesta = "si"
    while respuesta == "si":
        numero = input("Ingresa el numero a convertir: ") # Objetivo 999.999.999.999,99
        numeroArray = numero.split(".")
        convertido = "" #Se guarda la respuesta
        # Si es un un numero mayor de 3 cifras seria >= 1000
        if(len(numero) > 0 and len(numero)<=3):
            convertido = cero_Mil(int(numero))
        #--------
        else:
            convertido = mayor_MilC(numeroArray)

        print(convertido + " " + moneda)

        respuesta = input("Desea convertir otro numero? ")

#NUMEROS FINALES

#Metodo para cuando le pase el numero sepa cuantos ceros quitar
#y asi solo me devuelva el ultima numero con la funcion numero % 1(..0..)
def numeroFinal(numero):
    num = "1"
    for i in range(len(str(numero)) - 1):
        if i < 3:
            num = num + "0"
    numInt = int(num)
    return numero % numInt

#PRIMEROS NUMEROS
def primerNumero(numero):
    num = int(str(numero)[0])
    return num

def segundoNumero(numero):
    num = int(str(numero)[1])
    return num

#Funciones que convierten el numero a letras
#El nombre del metodo indica el rango de numeros a convertir

def cero_DiezC(numero):
    return ceroDiez[numero]

def veinte_CienC(numero):
    primero = primerNumero(numero)
    final = numeroFinal(numero)

    if (numero % 10 == 0): #Si el modulo es cero, quiere decir que es multiplo de 10
        return veinteCien[primero - 2]
    elif(primero == 2):
        return "veinti" + cero_DiezC(final)
    else:
        return veinteCien[primero - 2] + " y " + ceroDiez[final]

def cien_MilC(numero):
    primero = primerNumero(numero)
    segundo = segundoNumero(numero)
    final = numeroFinal(numero)

    ceroCero = str(segundo) + str(final) #Validamos si los dos ultimos numeros son ceros

    if (ceroCero == "00"):
        if(primero == 1):
            return "cien"
        elif(primero == 5):
            return "quinientos"
        elif(primero == 7):
            return "setecientos"
        elif(primero == 9):
            return "novecientos"
        else:
            return ceroDiez[primero] + cientos

    elif(segundo == 0):
        return "ciento " + str(ceroDiez[final])

    else:
        if(primero == 1 ):
            return "ciento" + str(veinte_CienC(numeroFinal(numero)))

        elif(primero == 5):
            return "quinientos " + str(veinte_CienC(numeroFinal(numero)))

        elif(primero == 7):
            return "setecientos " + str(veinte_CienC(numeroFinal(numero)))

        elif(primero == 9):
            return "novecientos " + str(veinte_CienC(numeroFinal(numero)))

        else:
            return ceroDiez[primero] + cientos + " " + str(veinte_CienC(numeroFinal(numero)))

#Me devuelve el resultado de cualquier numero entre cero y 1000-1
def cero_Mil(numero):
    numero = int(numero)
    respuesta = ""

    if(len(str(numero)) == 1):
        respuesta = cero_DiezC(numero)
    elif(len(str(numero)) == 2):
        if(numero < 20):
            respuesta = diezVeinte[numero - 11]
        else:
            respuesta = veinte_CienC(numero)
    else:
        respuesta = cien_MilC(numero)

    return respuesta

#Me devuelve cualquier resultado mayor a mil
def mayor_MilC(numeroArray):
    respuesta = ""
    valoresNumerios = ["millones", "", "billones", "", "trillones", "", "cuatrillones", "", "quintillones"]

    j = 0
    for i in reversed(range(len(numeroArray))): #Debe ir en reversa

        temp = ""

        if i == len(numeroArray) - 1: #El ultimo numero no me debe agregar nada
            temp = ""

        elif j % 2 != 0:
            temp = "mil"
        else:
            temp = valoresNumerios[j - 2]

        respuesta = cero_Mil(int(numeroArray[i])) + " " + temp + " " + respuesta
        j = j+1

    return respuesta

#Inicio de programa
convertir()






