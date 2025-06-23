
class Usuario:
    contador_id = 1  #contador de id usuarios

    def __init__(self, nombre, apellido, email, contraseña):
        self.id_usuario = Usuario.contador_id
        Usuario.contador_id += 1     
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña



    
