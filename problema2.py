# PROBLEMA2
# INGRESO DE DATOS
numero1 = float(input("Ingresa el número 1: "))
numero2 = float(input("Ingresa el número 2: "))
numero3 = float(input("Ingresa el número 3: "))

# OPERANDO
promedio=(numero1+numero2+numero3)/3

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"El promedio es: {promedio}")
if abs(promedio-numero1)<=abs(promedio-numero2)<=abs(promedio-numero3):
    print(f"El valor más cercano al promedio es: {numero1}")
elif abs(promedio-numero1)<=abs(promedio-numero3)<=abs(promedio-numero2):
    print(f"El valor más cercano al promedio es: {numero1}")
elif abs(promedio-numero2)<=abs(promedio-numero1)<=abs(promedio-numero3):
    print(f"El valor más cercano al promedio es: {numero2}")
elif abs(promedio-numero2)<=abs(promedio-numero3)<=abs(promedio-numero1):
    print(f"El valor más cercano al promedio es: {numero2}")
elif abs(promedio-numero3)<=abs(promedio-numero1)<=abs(promedio-numero2):
    print(f"El valor más cercano al promedio es: {numero3}")
elif abs(promedio-numero3)<=abs(promedio-numero2)<=abs(promedio-numero1):
    print(f"El valor más cercano al promedio es: {numero3}")