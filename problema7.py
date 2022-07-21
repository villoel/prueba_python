# PROBLEMA 7
# INGRESO DE DATOS
dict1 = {"gato": "cat",
        "perro": "dog",
        "caballo": "horse",
        "leon": "lion"}
# OPERACIONES
dict2 = dict(dict1)

dict2["caballo"] = "pegaso"
dict2["leon"] = "david"
dict2["zebra"] = "zebra"
dict2["burro"] = "donkey"
dict2["mono"] = "bow"

# SALIDA DE DATOS
print(f"\nRESULTADO FINAL")
print(f"===========================================")
print(f"El primer diccionario es: {dict1}")
print(f"El diccionario modificado es: {dict2}")