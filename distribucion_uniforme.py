#-- DISTRIBUCIÓN UNIFORME --



#x = a + rnd * (b-a) 


if a >= b:
   print("El límite inferior a debe ser menor que el límite superior b.")
else:
  for rnd in numeros_uniformes_0_1:
      x = a + rnd * (b-a)
      numeros_distribucion_uniforme.append(x)