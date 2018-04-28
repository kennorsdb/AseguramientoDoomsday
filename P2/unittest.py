# -*- coding: utf-8 -*-
import datetime
import random
from calendar import monthrange, isleap


"""def fecha_es_tupla(d,m,y): 
    Todas las fechas serán presentadas como tuplas de tres números enteros
    positivos (ternas), en este orden: (año, mes, día). El resultado debe ser un valor booleano,
    True o False."""
diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def bisiesto(y): 
    """ Dado un año perteneciente al rango permitido, determinar si este es bisiesto. El
        resultado debe ser un valor booleano, True o False.
        Se valida la regla de que un año bisiesto es divisible por cuatro, excepto para los años
        múltiplos de 100 pero sí de 400. """
    return y >= 1583 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def fecha_es_valida((d,m,y)): 
    """ Dada una fecha, determinar si ésta es válida. El resultado debe ser un
        valor booleano, True o False."""
    # Si el mes, el año y los días son válidos
    if (m < 1 and m > 12 and y < 1853) or (0 > d and d > diasMes[m]) or (m==2 and d > 28 + bisiesto(y)):
        return False
    else:
        return True


def dia_siguiente((d,m,y)): 
    # Dada una fecha válida, determinar la fecha del día siguiente. El resultado
    # debe ser una fecha válida (tupla de tres números enteros positivos que corresponde a una fecha
    # en el Calendario gregoriano.
    if fecha_es_valida((d,m,y)):
        if m==12 and d == 31:
            return (1,1,y+1)
        elif not bisiesto(y) and m == 2 and d == 28: 
            return (1,3,y)
        elif diasMes[m] == d:
            return (1,m+1,y)
        else:
            return (d+1,m,y)

def dias_desde_primero_enero((d,m,y)):
    # Dada una fecha válida, determinar el número de días
    # transcurridos desde el primero de enero de su año (el número de días transcurridos entre el
    # primero de enero y el primero de enero, dentro de un mismo año, es 0). El resultado debe ser un
    # número entero.
    if fecha_es_valida((d,m,y)):
        dias = 0
        for i in range(0,m):
            d += diasMes[i]
        dias += d-1
        dias -= not bisiesto(y) and m > 2
        return dias
    else:
        return -1


def dia_primero_enero(y): 
    """ Dado un año perteneciente al rango permitido, determinar el día de la
     semana que le corresponde, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 =
     miércoles, 4 = jueves, 5 = viernes, 6 = sábado. El resultado debe ser un número entero, conforme
     a la codificación indicada."""
    return dia_semana((1,1,y))


def imprimir_3x4():
    

def dia_semana((d,m,y)):
    if fecha_es_valida((d,m,y)):
        y -= m<3
        mesIndex=[45,98,101,100,61,112,101,110,43,109,97,100,46]
        return (y+y//4-y//100+y//400+mesIndex[m]+d-1)%7
    else :
        return -1


    



 
# Unit test para comprobar el día de la semana de todos los días
# hasta 2999
for y in range(1582,2999):
    for m in range(1,12):
        for d in range(1,monthrange(y,m)[1]):
            kenneth = dia_semana((d,m,y))
            python = datetime.date(y, m, d).weekday()
            if kenneth != python:
                print 'error:', d,m,y  

# Unit test para compromar los días siguientes de todos los días
for y in range(1582,2999):
    for m in range(1,12):
        for d in range(1,monthrange(y,m)[1]):
            kenneth = dia_siguiente((d,m,y))
            python = datetime.date(y, m, d)+datetime.timedelta(days=1)
            if kenneth != (python.day,python.month,python.year):
                print 'error:', kenneth, (python.day,python.month,python.year)
                
# Unit test para compromar los días siguientes de todos los días
for y in range(1900,2999):
    if bisiesto(y) != isleap(y):
        print "error en bisiesto:", y

# Unit test para compromar los días siguientes de todos los días
for y in range(1900,2999):
    for m in range(1,12):
        for d in range(1,monthrange(y,m)[1]+1):
            kenneth = dias_desde_primero_enero((d,m,y))
            python = datetime.date(y, m, d) - datetime.date(y, 1, 1)
            if kenneth != python.days:
                print 'error:', kenneth, python.days
