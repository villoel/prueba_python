# PROBLEMA 1
# INGRESO DE DATOS
print("INGRESE LAS SIGUIENTES NOTAS DEL ALUMNO")
print(f"===========================================")
nota1=float(input("Nota del primer laboratorio es: "))
nota2=float(input("Nota del segundo laboratorio es: "))
nota3=float(input("Nota del tercer laboratorio es: "))
nota_par=float(input("Nota del examen parcial es: "))
nota4=float(input("Nota del cuarto laboratorio es: "))
nota5=float(input("Nota del quinto laboratorio es: "))
nota_final=float(input("Nota del examen final es: "))
# OPERACIONES 41
promedio=(nota1*1+nota2*2+nota3*4+nota_par*7+nota4*6+nota5*9+nota_final*12)/41

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"El promedio final del alumno es: {promedio}")