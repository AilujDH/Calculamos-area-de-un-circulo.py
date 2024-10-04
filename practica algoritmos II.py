
#Paso 1: Solicite al usuario que ingrese el radio del circulo que quiere calcular
#Mostrar mensaje " Por favor, ingrese el radio del circulo: "
#Leer el dato ingresado y asignarlo a variable radio de tipo flotante (castear)



import math


radio= float (input ("Por favor ingrese el radio del circulo que quiere calcular: "))
#Paso 2:Calcular el area del circulo usando la formula Pi x R¨2
#Definir y asignar a la variable area el resultado de pix r´2

area_circulo= math.pi*(radio**2)

#Paso 3: Mostrar al usuario el area calculada
#Mostrar mensaje "El area del circulo con radio", radio, "es: "
 
print ("El area calculada para el radio", radio, "es: ", area_circulo,)