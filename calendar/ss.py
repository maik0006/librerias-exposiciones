from milibreria import mes_actual, es_bisiesto, dia_de_la_semana, calendario_completo, año, mes, dia 

mes_actual(año, mes)
es_bisiesto(año)
print(f"El {dia}/{mes}/{año} cae en {dia_de_la_semana(año, mes, dia)}.")
calendario_completo(año)
