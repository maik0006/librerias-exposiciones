import calendar

año = 2025
mes = 10
dia= 15

def mes_actual(año, mes):
    print(calendar.month(año, mes)) 

def es_bisiesto(año):    
    if calendar.isleap(año):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")


def dia_de_la_semana(año, mes, dia):
    dia_semana = calendar.weekday(año, mes, dia)
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias[dia_semana]

def calendario_completo(año):
    print(calendar.calendar(año))

