rut_lista = []
nombre_lista = []
edad_lista = []
anacimiento_lista=[]
fechanaci_lista=[]
pnacimiento_lista = []
cnacimiento_lista = []
econyugal_lista = []



while True:

    opcion = int(input("\nBienvenido a la atencion rapida del RENAPER de la Republica de Argentina, para comenzar seleccione una de las opciones que se muestran a continuacion.\n\nMenu Principal \n\n1) Grabar\n2) Buscar\n3) Imprimir certificados\n4) Eliminar\n5) Salir\n"))
    
    if opcion == 1:
        grabar_rut = int(input("Ingrese DNI: "))
        rut_lista.append(grabar_rut)
    
        while True:
            grabar_nombre = input("Ingrese Nombre: ")
            if len(grabar_nombre)>=8:
                nombre_lista.append(grabar_nombre.upper())
                break
            else:
                print("Ingrese un nombre con 8 caracteres como minimo")
                True
    
        while True:        
            grabar_edad = int(input("Ingrese Edad: "))
            if grabar_edad>=0:
                edad_lista.append(grabar_edad)
                break
            else:
                print("Ingrese una edad valida")
                True
        grabar_anacimiento = input("Ingrese Fecha de Nacimiento (DDMMAA): ")
        if len(grabar_anacimiento):
           anacimiento_lista.append(grabar_anacimiento.upper())
           
        grabar_pnacimiento = input("Ingrese Pais de nacimiento: ")
        pnacimiento_lista.append(grabar_pnacimiento.upper())
    
        grabar_cnacimiento = input("Ingrese Ciudad de nacimiento: ")
        cnacimiento_lista.append(grabar_cnacimiento.upper())
        
        grabar_estadoconyugal = input("Ingrese Estado Conyugal: ")
        econyugal_lista.append(grabar_estadoconyugal.upper())      
        
        print('\nUsuario grabado correctamente.')

    elif opcion ==2:
        
        while True:

            buscar_rut = int(input("Ingrese DNI: "))

            if rut_lista.index(buscar_rut)>=0:

                print(f"\nLos datos de la persona son:\n\nNombre: {nombre_lista[rut_lista.index(buscar_rut)]}\nDNI: {rut_lista[rut_lista.index(buscar_rut)]}\nEdad: {edad_lista[rut_lista.index(buscar_rut)]}\nPais de nacimiento: {pnacimiento_lista[rut_lista.index(buscar_rut)]}\nCiudad de nacimiento: {cnacimiento_lista[rut_lista.index(buscar_rut)]}")
                break
            else:
                print("Ingrese un rut valido")
                True
    
    elif opcion == 3:
        
        while True:
            
            cert_rut = int(input("Ingrese DNI: "))
            

            if rut_lista.index(cert_rut)>=0: 
                
               print(f'Certificado de nacimiento\n\nRut: {cert_rut}\nNombre: {nombre_lista[rut_lista.index(cert_rut)]}\nEdad: {edad_lista[rut_lista.index(cert_rut)]}\nPais de nacimiento: {pnacimiento_lista[rut_lista.index(cert_rut)]}\nCiudad de nacimiento: {cnacimiento_lista[rut_lista.index(cert_rut)]}\nFecha nacimiento: {anacimiento_lista[rut_lista.index(cert_rut)]}\nEstado Conyugal: {econyugal_lista[rut_lista.index(cert_rut)]}')  
            
            continuar_imp = int(input('\nDesea continuar imprimiendo certificados?\n1) Si\n2) No\n'))

            if continuar_imp==1:
                True
            if continuar_imp==2:
                print('Volviendo al menu principal.')
                break
    elif opcion ==4:

        while True:

            eliminar_rut = int(input('Ingrese DNI: '))

            if rut_lista.index(eliminar_rut)>=0:
                
                nombre_lista.pop(rut_lista.index(eliminar_rut))
                edad_lista.pop(rut_lista.index(eliminar_rut))
                pnacimiento_lista.pop(rut_lista.index(eliminar_rut))
                cnacimiento_lista.pop(rut_lista.index(eliminar_rut))
                rut_lista.pop(rut_lista.index(eliminar_rut))
                print("Registro eliminado con exito!")
                break
                
            else:
                print("Ingrese un rut ingresado anteriormente")
                True

    elif opcion == 5:
        print(" Programa creado por: Claudio Cornejo. Version: 1.1 ")
        exit()


