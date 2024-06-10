registros= {}



def registrar():
    usuario = input ("Ingrese su nombre de usuario: ")
    contraseña = input ('Ingrese su contraseña: ')
    
    if usuario not in registros:
        registros[usuario] = contraseña
        print ('Su usuario a sido creado')
    else: 
        print ('Su usuario ya existe')
        
        
        
def login():
    usuario= input ('Ingrese su nombre de usuario: ')
    contraseña= input ('Ingrese su contraseña: ')
    
    if usuario in registros and registros[usuario] == contraseña : 
        print ('Bienvenido, iniciaste sesion correctamente')
    else:
        print('Su usuario o contraseña son incorrectos')
        
        


def mostrar():
    
  print (registros)
         

menu = True

while menu: 
    
    print ('''  
        Hola, que desea hacer hoy?

    1) Registrarse
    2) Iniciar sesion
    3) Ver los usuarios y contraseñas       
    4) Salir
    ''')

      
    opcion = input ('Ingrese aqui su opcion: ')
    
    if opcion == '1':
        registrar()
    elif opcion == '2':
            login()
    elif opcion == '3':
            mostrar()
    elif opcion == '4':
            menu = False
            print ('Bueno, Nos Vemos')
    else :
            print ('No entiendo, pruebe con 1,2,3,4')


