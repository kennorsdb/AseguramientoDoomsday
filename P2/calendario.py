# -*- coding: utf-8 -*-
#Código fuente.

#Autores:
#Alejandro Pacheco Quesada
#Kenneth Obando Rodríguez

'''
Tabla con los días que tiene cada mes
'''
diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def fecha_es_tupla(fecha):
    """Todas las fechas serán presentadas como tuplas de tres números enteros
    positivos (ternas), en este orden: (año, mes, día). El resultado debe ser un valor booleano,
    True o False."""

    """
    Entrada: fecha->tupla de enteros
    Salida: Boolean
    """
    if isinstance(fecha, tuple):    #Verifica que fecha realmente sea una tupla, y de tamaño 3.
        if len(fecha)==3:
            for i in fecha:
                if not (isinstance(i, int) and i>0):    #Verifica que todos los valores de la tupla sean enteros positivos.
                    return False
            return True
        return False
    return False

def bisiesto(y):
    """ Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
        resultado debe ser un valor booleano, True o False.

        Se valida la regla de que un año bisiesto es divisible por cuatro, excepto para los años
        múltiplos de 100 pero sí de 400. """

    """
    Entrada: y-> Entero para el año
    Salida: Boolean
    """

    return y >= 1583 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def fecha_es_valida(fecha):
    """ Dada una fecha, determinar si ésta es válida. El resultado debe ser un
        valor booleano, True o False."""

    # Determina si el formato es correcto
    if (fecha_es_tupla(fecha)):
        # Si el mes, el año y los días son válidos
        y, m, d = fecha
        if (m < 1 or m > 12 or y < 1583) or (1 > d or d > diasMes[m]) or (m==2 and d > 28 + bisiesto(y)):
            return False
        else:
            return True
    return False


def dia_siguiente(fecha):
    """Dada una fecha válida, determinar la fecha del día siguiente. El resultado
    # debe ser una fecha válida (tupla de tres números enteros positivos que corresponde a una fecha
    # en el Calendario gregoriano."""

    '''
    Entrada: fecha->tupla de enteros
    Salida: fecha->tupla de enteros
    
    ACLARACIÓN:  En caso de ingresar una fecha no válida, retorna una terna con -1.
    '''

    if fecha_es_valida(fecha):
        y, m, d = fecha
        if m==12 and d == 31:  #Verificación de final de año
            return (y+1,1,1)
        elif not bisiesto(y) and m == 2 and d == 28:  #Caso para años bisiestos
            return (y,3,1)
        elif diasMes[m] == d:  #Caso para final de mes
            return (y,m+1,1)
        else:                  #Caso general
            return (y,m,d+1)
    else:
        return (-1,-1,-1)

def dias_desde_primero_enero(fecha):
    """Dada una fecha válida, determinar el número de días
    # transcurridos desde el primero de enero de su año (el número de días transcurridos entre el
    # primero de enero y el primero de enero, dentro de un mismo año, es 0). El resultado debe ser un
    # número entero.
    """
    '''
    Entrada: fecha->tupla de enteros
    Salida: Entero
    
    ACLARACION: En caso de que la fecha no sea válida retorna -1
    '''
    if fecha_es_valida(fecha):
        y, m, d = fecha
        dias = 0
        for i in range(0,m):    #Conteo de días
            d += diasMes[i]
        dias += d-1
        dias -= not bisiesto(y) and m > 2  #Excepción en caso de que el año fuera bisiesto
        return dias
    else:
        return -1

def dia_primero_enero(y):
    """ Dado un año perteneciente al rango permitido, determinar el día de la
     semana que le corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
     miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número entero, conforme
     a la codificación indicada."""

    '''
    Entrada: y-> Entero
    Salida: Entero, corresponde al día de la semana
    
    ACLARACION: En caso de que la fecha sea incorrecta, se retorna -1
    '''

    return dia_semana((y,1,1)) #Se hace un llamado a una función auxiliar


def imprimir_3x4(y):
    """Dado un año perteneciente al rango permitido, desplegar en consola el calendario de ese
    año en formato de 3 secuencias (‘filas’) de 4 meses cada una.
    El resultado debe lucir semejante al que se muestra al final de este enunciado."""

    '''
    Entrada: y->Año
    Salida: No hay
    '''

    print("\nCalendario del año "+y.__str__()+ " D.C.\n")
    #Encabezado para cada día de la semana
    Header = " D   L   K   M   J   V   S  |  "

    #Grupos de meses (3x4)
    meses = [["Enero","Febrero","Marzo","Abril"],["Mayo","Junio","Julio","Agosto"],["Septiembre","Octubre","Noviembre","Diciembre"]]
    calendario = "__________________________________________________________________________________________________________________________\n"

    weeks = dias_calendar(y) #Llamada a función auxiliar para el cálculo de días
    last = 0
    for batch in meses:
        #Print para cada grupo de meses (Nombre)
        for mes in batch:
            calendario+= mes.center(27,' ')
            calendario+=" |  "
        calendario+="\n"

        #Print de los días de la semana
        for mes in batch:
            calendario+=Header
        calendario+="\n"
        #-------------------------------------
        #Días de todos los meses:

        #Para cada se semana, de cada mes, se imprimen sus días.
        for i in range(0,6):
            concat = ""
            for m in range(last,last+4):
                try:
                    fila = weeks[m][i]
                    for numero in fila:
                        if numero==0:
                            concat+="  "
                        elif numero<10:
                            concat+= " "+str(numero)
                        else:
                            concat+=str(numero)
                        concat+="  "
                    concat+="|  "
                except:
                    concat+="                            |  "
            calendario+=concat+"\n"
        calendario+="____________________________|______________________________|______________________________|______________________________|\n"
        last+=4

    print(calendario)


def dias_calendar(y):
    isBis = bisiesto(y)
    semanas = []
    #Para cada mes:
    for i in range(1,13):
        diaInic = dia_semana((y,i,1))  #Se calcula el día en que inicia el mes y la cantidad que tiene
        dias = diasMes[i]
        if i==2 and not isBis:
            dias-=1     #Excepción en caso de años bisiestos
        mes = []; j=1

        #Cada día del mes se agrupa en las semanas del mes
        while(j<=dias):
            week=[]
            if(diaInic!=0):
                week+= [0 for i in range(0,diaInic)] #Los días vacíos se settean en 0

            #Agrupación en semanas
            while(diaInic<=6 and j<=dias):
                week.append(j);j+=1
                diaInic+=1
            diaInic = 0
            full = len(week)
            if(full!=7):
                week+=[0 for i in range(full,7)] #Los días vacíos se settean en 0
            mes.append(week)

        semanas.append(mes)
    return semanas


'''
--------------------------------------------------------------------
-      E X T E N S I O N   D E   F U N C I O N A L I D A D         -
-                                                                  -
-                  I T E R A C I O N   # 2                         -
-                                                                  -
--------------------------------------------------------------------
'''

'''
Lista de la forma (MES, DIA) con los feriados estáticos de Costa Rica
'''

feriadosEstaticos = [(1,1), (4,11), (5,1), (7,25), (8,2), (8,15), (9,15), (10,2), (12,25)]



def fecha_futura(tupla, dias):
    """
    Dada una fecha válida f y un número entero no-negativo n, determinar
    la fecha que está n días (naturales) en el futuro. El resultado debe ser una fecha válida.

    Entradas:
    :param tupla: fecha en forma de tupla de enteros
    :param dias: Entero

    Salida:
    :return: tupla de enteros
    """

    '''
    ACLARACIÓN:  En caso de ingresar una fecha no válida o un número negativo, retorna una terna con -1.
    '''
    if fecha_es_valida(tupla):
        if(dias>=0):
            actual = tupla
            for i in range(0,dias):
                actual = dia_siguiente(actual)
            return actual
        else:
            return (-1,-1,-1)
    else:
        return (-1,-1,-1)
        

def es_mayor(f1, f2):
    """
    Función auxiliar que retorna True si f1 es mayor que f2, y de locontrario False.

    Entradas:
    :param f1: Fecha número 1
    :param f2: Fecha número 2

    Salida:
    :return: Booleano
    """
    if fecha_es_valida(f1) and fecha_es_valida(f2):
        y1, m1, d1 = f1
        y2, m2, d2 = f2
        return (y1 > y2) or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2)


def dias_entre (f1, f2):
    """
    Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
    determina el número de días (naturales) entre las dos fechas. Si f1 = f2, entonces
    días_entre(f1, f2) = 0. 

    Entradas:
    :param f1: fecha en forma de tupla de enteros
    :param f2: fecha en forma de tupla de enteros

    Salida:
    :return: entero con la cantidad de días
    """
    '''
    ACLARACIÓN:  En caso de ingresar una fecha no válida o un número negativo, retorna una terna con -1.
    '''
    if fecha_es_valida(f1) and fecha_es_valida(f2):
        if es_mayor(f1,f2):
            fechaMenor = f2
            fechaMayor = f1
        else:
            fechaMenor = f1
            fechaMayor = f2
        dias = 0
        while(fechaMenor != fechaMayor):    #Conteo de días
            fechaMenor = dia_siguiente(fechaMenor)
            dias += 1
        return dias


def dia_semana(fecha):
    '''
    Dada una fecha válida, determina el día de la semana que le
    corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
    miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado es un número entero,
    conforme a la codificación indicada

    Entrada: fecha->tupla de enteros
    Salida: Entero, corresponde al día de la semana

    En caso de que la fecha sea incorrecta, se retorna -1
    '''
    if fecha_es_valida(fecha):
        y, m, d = fecha
        y -= m<3
        mesIndex=[45,98,101,100,61,112,101,110,43,109,97,100,46]    #Algoritmo Doomsday, ver referencia en documentación externa
        return ((y+y//4-y//100+y//400+mesIndex[m]+d-1)+1) % 7
    else :
        return -1

def calc_easter(year):
    """ Retorna la fecha de Pascua para el año 'year'
        Tomado de: http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/
        
        Esta función utiliza el algoritmo de Butcher, que funciona para todos los años del calendario
        Gregoriano. Este algoritmo se puede encontrar en el Almanaque Eclesiástico de 1876. 

        Entrada: year-> año que se desea el cálculo
        Salida: tupla con la fecha
    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return (year, month, day)


def es_dia_habil((y,m,d)):
    '''
    Función auxiliar que devuelve True si la fecha es día laboral "hábil" en Costa Rica.

    Entrada: fecha->tupla de enteros
    Salida: Booleano, True si es un día hábil.

    En caso de que la fecha sea incorrecta, se retorna -1
    '''
    if fecha_es_valida((y,m,d)):
        diaSemana = dia_semana((y,m,d))
        pascua = calc_easter(y)
        if diaSemana == 6 or diaSemana == 0:
            return False
        elif  pascua == fecha_futura((y,m,d), 2) or pascua == fecha_futura((y,m,d), 3):
            return False
        elif (m,d) in feriadosEstaticos:
            return False
        else:
            return True
    else:
        return (-1,-1,-1)


#Está ya la habíamos hecho
# def dia_semana (tupla):


def fecha_futura_habil (tupla, dias):
    '''
    Dada una fecha válida f y un número entero no-negativo n,
    determina la fecha que está n días hábiles en el futuro. El resultado es una fecha
    válida que corresponda a un día hábil. 

    Entrada: tupla->tupla de enteros
             días - Entero con la cantidad de días hábiles que se desean.
    Salida: Tupla, fecha correspondiente a n días hábiles despues de tupla

    En caso de que la fecha sea incorrecta, se retorna -1
    '''
    if fecha_es_valida(tupla):
        if(dias>=0):
            actual = tupla
            count = 0
            while (count < dias):
                actual = dia_siguiente(actual)
                if es_dia_habil(actual):
                    count += 1
            return actual
        else:
            return (-1,-1,-1)
    else:
        return (-1,-1,-1)


def dias_habiles_entre (f1, f2):
    '''
    Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤
    f1, determina el número de días hábiles entre las dos fechas. Si f1 = f2, entonces
    días_habiles_entre(f1, f2) = 0

    :param f1: fecha en forma de tupla de enteros
    :param f2: fecha en forma de tupla de enteros

    Salida: Entero, n días hábiles despues de tupla

    En caso de que la fecha sea incorrecta, se retorna -1
    '''
    if fecha_es_valida(f1) and fecha_es_valida(f2):
        if es_mayor(f1,f2):
            fechaMenor = f2
            fechaMayor = f1
        else:
            fechaMenor = f1
            fechaMayor = f2
        dias = 0
        while(fechaMenor < fechaMayor):    #Conteo de días
            fechaMenor = dia_siguiente(fechaMenor)
            if es_dia_habil(fechaMenor):
                dias += 1
            
        return dias




#print dias_entre((2018,4,11), 10 )
#print fecha_futura_habil((2018,5,5), 35 )
#print fecha_futura_habil((1986,6,18), 3985 )

print dias_entre((2018,7,2) , (2018,10,26) )
print dias_entre((2018,5,1) , (2018,10,31) )
print dias_entre((2018,5,30), (2018,7,25)  )
print dias_entre((2018,4,1) , (2018,4,29)  )
print dias_entre((2018,4,29), (2018,4,1)   )