#-- DISTRIBUCIÓN UNIFORME --

a = float(input("Ingrese el límite inferior de la distribución uniforme: "))
b = float(input("Ingrese el límite superior de la distribución uniforme: "))

x = a + rnd * (b-a) 

numeros_distribucion_uniforme = []

if a >= b:
   print("El límite inferior a debe ser menor que el límite superior b.")
else:
  for rnd in numeros:
      x = a + rnd * (b-a)
      numeros_distribucion_uniforme.append(x)