# PROBLEMA 5
# INGRESO DE DATOS
print("POR FAVOR INGRESE 10 NÚMEROS")
print(f"===========================================")
lista=[]
for i in range(10):
    num=float(input("Ingrese numero:"))
    lista.append(num)

# OBTENGO PROMEDIO Y CREO OTRA LISTA
promedio=sum(lista)/len(lista)

lista2=[]
for i in lista:
    num2=(i-promedio)**2
    lista2.append(num2)

desv_estandar=(sum(lista2)/len(lista2))**0.5

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"La lista ingresada es:{lista}")
print(f"El promedio es:{promedio}")
print(f"La desviación estandar es: {desv_estandar}")