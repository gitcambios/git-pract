from direccion import Direccion
from sistema_usuario import SistemaUsuario

sistema = SistemaUsuario()

llave = True
while (llave == True):
    print("---MENU---")
    print("1. Iniciar sesion: ")
    print("2. Registrarse: ")
    print("0. Salir del sistema")
    opcion = int(input("Seleccione una opcion: "))

    if(opcion == 1):
        
        email= input("Email: ")
        contraseña = input("Contraseña: ")
        usuario = sistema.iniciar_sesion(email, contraseña)

        if usuario:
            print("Inicio sesion exitosamente!!!")

    elif(opcion == 2):
                    
        nombre = input("Nombre: ")
        apellido = input("Apellido:")
        telefono = int(input("Numero telefonico: "))
                
        calle = input("Calle: ")
        numero = int(input("Numero de calle: "))
        ciudad = input("Ciudad: ")                    #Pido los atributos de la clase Direccion
        codigo_postal = int(input("Codigo postal: "))
        provincia = input("Provincia: ")

        #Creo un objeto de la clase Direccion
        direccion_nueva = Direccion(calle, numero, ciudad, codigo_postal, provincia)
        email = input("Email: ")

        #Confirmar contraseña 
                
        contraseña = input("Contraseña: ") 
        validar_contraseña = input("Confirme contraseña: ") 
        while contraseña != validar_contraseña:
            print("¡Las contraseñas no coinciden!")
            contraseña = input("Contraseña: ") 
            validar_contraseña = input("Confirme contraseña: ")

        sistema.registrar_usuario(nombre, apellido, email, contraseña, telefono, direccion_nueva)
        
    elif(opcion == 0):
        llave = False
                
    