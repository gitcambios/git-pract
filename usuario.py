
class Usuario:
    contador_id = 1  #contador de id usuarios

    def __init__(self, nombre, apellido, email, contraseña):
        self.id_usuario = Usuario.contador_id
        Usuario.contador_id += 1     #vamos aumentando el numero del id para el siguiente usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

#usuario = Usuario(1, "Juan", "Perez", "JuanPereaz@gmail.com", "clave123")
#print(usuario.__dict__)


    
