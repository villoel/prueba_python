# PROBLEMA 3
# INGRESO DE DATOS
numero = int(input("Ingresa el número: "))

# PROCESO DE OPERACIONES
divisor = 0
lista_divisores=[]
for i in range(1, numero+1):
    if numero%i==0:
        lista_divisores.append(i)

cant_pares=0
cant_impares=0

for j in lista_divisores:
    
    if j%2==0:
        cant_pares+=1
    else:
        cant_impares+=1

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"La cantidad de números pares es:{cant_pares}")
print(f"La cantidad de números impares es:{cant_impares}")