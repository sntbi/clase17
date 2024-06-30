#v1 
# class Social:
#     def __init__(self, cant_amigos = 3) :
#         self.cant_amigos = cant_amigos
        




# class Alumno:
    
#     def __init__(self, apellido, division, sexo='Hombre'): 
#         self.division = division
#         self.apellido = apellido
#         self.sexo = sexo 
#         self.Social= Social()
        
#         print(f'Se inscribio el alumno {self}')
    
#     def desaprobado(self):
#         print('El alumno a desaprobado', self)
        
#     def aprobado(self):
#         print('El alumno a aprobado', self)
        

# Santiago = Alumno( 'Bisceglia','S6A')
# Pedro = Alumno( 'Gomez','S2C')
# Agustina = Alumno ('Lorenzo', 'S4B', 'Mujer')


# print (Agustina.Social.cant_amigos)


#v2

# class Social:
#     def __init__(self, numero_id,  cant_amigos = 3) :
#         self.numero_id = numero_id
#         self.cant_amigos = cant_amigos
        

# class Alumno:
    
#     cant_brazos= 2
    
#     def __init__(self, apellido, division, sexo='Hombre',**kwargs): 
#         self.division = division
#         self.apellido = apellido
#         self.sexo = sexo 
#         self.social= Social(**kwargs)
        
#         print(f'Se inscribio el alumno {self}')
    
#     def desaprobado(self):
#         print('El alumno a desaprobado', self)
        
#     def aprobado(self):
#         print('El alumno a aprobado', self)
        

# # Santiago = Alumno( 'Bisceglia','S6A')
# # Pedro = Alumno( 'Gomez','S2C')
# Agustina = Alumno ('Lorenzo', 'S4B', 'Mujer', cant_amigos=12, numero_id = 13324)


# print (Agustina.social.cant_amigos, Agustina.social.numero_id)


#V3

class Social:
    def __init__(self, numero_id,  cant_amigos = 3) :
        self.numero_id = numero_id
        self.cant_amigos = cant_amigos
        

class Alumno:
    
    cant_brazos= 2
    
    def __init__(self, nombre, apellido, division, sexo='Hombre',**kwargs): 
        self.nombre = nombre
        self.division = division
        self.apellido = apellido
        self.sexo = sexo 
        self.social= Social(**kwargs)
        
        print(f'Se inscribio el alumno {self}')
    
    def __str__(self):
        return f'Alumno, {self.nombre} {self.apellido} de la division {self.division} de sexo {self.sexo}'

    
    def desaprobado(self):
        print('El alumno a desaprobado', self)
        
    def aprobado(self):
        print('El alumno a aprobado', self)
        

# Santiago = Alumno( 'Bisceglia','S6A')
# Pedro = Alumno( 'Gomez','S2C')
alumno3 = Alumno ('Agustina','Lorenzo', 'S4B', 'Mujer', cant_amigos=12, numero_id = 13324)


#print (alumno3) 

#/////////////////////////////////////////////////////#

class Aula:
    
    def __init__(self, aula):
        self.aula = aula
        self.alumnos = []
    
    def __str__(self): 
        return f'Listado de alumnos en el aula: "{self.aula}"'
    
    def __len__ (self):
        return len(self.aula)
        




aula = Aula('Sexto A')

print (aula)
print (len(aula))