from tienda.cliente import Cliente

class SistemaUsuario:
    def __init__(self):
        self.usuarios_registrados = []

    def registrar_usuario(self, nombre, apellido, email, contraseña, telefono, direccion_nueva):
        
        for u in self.usuarios_registrados:
            if u.email == email:
                return "email_existente"
        
        nuevo_usuario = Cliente(nombre, apellido, email, contraseña, telefono, direccion_nueva)
        self.usuarios_registrados.append(nuevo_usuario)
        return nuevo_usuario

    def iniciar_sesion(self, email, contraseña):
        for u in self.usuarios_registrados:
            if u.email == email:
                if u.contraseña == contraseña:
                    return u
                else:
                    return "contraseña_incorrecta"
        return "email_no_registrado"



            
