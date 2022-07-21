# problema 4
# INGRESO DE DATOS
def factorial_num(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial

facto=factorial_num(int(input("Ingrese número para sacar el factorial: ")))
# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"El factorial es: {facto}")