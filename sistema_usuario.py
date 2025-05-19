from cliente import Cliente

class SistemaUsuario:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar_usuario(self, nombre, apellido, email, contraseña, telefono, direccion_nueva):
        for u in self.usuarios_registrados:
            if (u.email == email):
                print("¡El email ingresado ya existe!")
                return None
            
        nuevo_usuario = Cliente(nombre, apellido, email, contraseña, telefono, direccion_nueva)
        self.usuarios_registrados.append(nuevo_usuario)
        print("Registro exitoso!")
        return nuevo_usuario
        
    def iniciar_sesion(self, email, contraseña):
        for u in self.usuarios_registrados:
            if(u.email == email): 
                if (u.contraseña == contraseña):
                    return u
                else: 
                    print("La contraseña que ingreso es incorrecta!")
                    return None
                
        print("Email no registrado")
        return None
            
