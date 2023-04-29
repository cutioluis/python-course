""" 
   si condicion se cumple: false
      #codigo a ejecutar en caso de que se cumpla
   de lo contrario:
      #codigo a ejecutar 
"""

ingreso_mensual = 61000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual <= 0:
       print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000: 
       print("Estas bien economicamente")
   
   
elif ingreso_mensual > 1000:
   print("Estas bien en latinoamerica")
elif ingreso_mensual > 500:
   print("Estas bien en Argentina")
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
else:
    print("Eres pobre")
