 
# datosalumno = {

# 'nombre' : input ('ingrese un nombre: '),
# 'apellido' : input ('ingrese un apellido: '),
# 'edad' : input ('Ingrese una edad')
    
# }


# saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# nombre = input ('Ingrese un nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'w')

# archivo_abierto.write(nombre)

# archivo_abierto.close()




# archivo_abierto = open ('archivo_de_prueba.txt', 'r')

# valor_del_archivo = archivo_abierto.read()

# print(valor_del_archivo)
# # print([valor_del_archivo])

# valor_del_archivo_segunda_lectura = archivo_abierto.read()
# print (valor_del_archivo_segunda_lectura)

# archivo_abierto.close()



import json 

dicc = {
    'key1' : 'valor1',
    'key2' : True,
    'key3' : None,
    'key4' : ('valor', 123),    
    
}

with open('archivo_de_no_json.json', 'w') as archivo_abierto: 
    json.dump (dicc, archivo_abierto, indent=4)

with open ('archivo_de_no_json.json', 'r') as archivo_abierto:
    datos= json.load(archivo_abierto)
    print (datos)
    
print('#########################')
print(datos)
