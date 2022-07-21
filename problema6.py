# PROBLEMA 6
# INGRESO DE DATOS
print("POR FAVOR INGRESE 10 NÚMEROS")
print(f"===========================================")
tupla = (float(input("N1:")),
         float(input("N2:")),
         float(input("N3:")),
         float(input("N4:")),
         float(input("N5:")),
         float(input("N6:")),
         float(input("N7:")),
         float(input("N8:")),
         float(input("N9:")),
         float(input("N10:")),)

# OPERACIONES
suma=0
producto=1
for i in tupla:
    suma+=i
    producto*=i

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"La tupla es: {tupla}")
print(f"La suma de la tupla es: {suma}")
print(f"La multiplicación de la tupla es: {producto}")