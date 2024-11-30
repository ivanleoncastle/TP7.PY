# # 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
# # del rectángulo.


# class rectangulo():
#     def __init__(self, base, altura):
        
#         self.base = base
#         self.altura = altura
    
#     def area(self):
        
#         return self.base * self.altura


# rectangulo = rectangulo(8, 12)  
# print("El área del rectángulo es:", rectangulo.area())  


# # 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener 
# # como miembros: 
# # o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número). 
# # o Un atributo para el estado (lleno o vacío). 
# # o Un atributo n, que indica la cantidad máxima de cebadas. 
# # o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una 
# # excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste! 
# # o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se 
# # debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío! 
# # o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad 
# # de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: 
# # “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.


# class Mate:
#     def __init__(self, n):
       
#         self.n = n
#         self.cebadas_restantes = n  
#         self.estado = "vacío" 
#     def cebar(self):
#         if self.estado == "lleno":
          
#             print("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.estado = "lleno"
#             print("Mate cebado con agua.")
    
#     def beber(self):
#         if self.estado == "vacío":
            
#          print("¡El mate está vacío!")
        
#         if self.cebadas_restantes > 0:
#             self.cebadas_restantes -= 1
#             print(f"Se bebió el mate. Quedan {self.cebadas_restantes} cebadas.")
#         else:
           
#             print("Advertencia: el mate está lavado.")
        
#         self.estado = "vacío"

# mate = Mate(6) 

# mate.cebar()
# mate.beber()
# mate.cebar()
# mate.beber()
# mate.cebar() 



# mate.beber()  
# mate.beber()  
# mate.beber() 









# 3) Botella y Sacacorchos 
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega). 
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está 
# destapada. 
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde 
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el 
# sacacorchos ya contiene un corcho. 
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya 
# un corcho

# class Corcho:
#     def __init__(self, bodega):
       
#         self.bodega = bodega
    
#     def __str__(self):
#         return f"Corcho de la bodega {self.bodega}"

# class Botella:
#     def __init__(self, corcho=None):
       
#         self.corcho = corcho

#     def esta_destapada(self):
       
#         return self.corcho is None

#     def __str__(self):
#         if self.esta_destapada():
#             return "Botella destapada"
#         else:
#             return f"Botella con corcho de {self.corcho.bodega}"

# class Sacacorchos:
#     def __init__(self):
       
#         self.corcho = None

#     def destapar(self, botella):
      
#         if botella.esta_destapada():
#             return "La botella ya está destapada."
        
#         if self.corcho is not None:
#             return "El sacacorchos ya contiene un corcho."

#         self.corcho = botella.corcho
#         botella.corcho = None
#         return f"Botella destapada. El corcho es de la bodega {self.corcho.bodega}"

#     def limpiar(self):
       
#         if self.corcho is None:
#             return "El sacacorchos no tiene corcho para limpiar."
        
#         mensaje = f"Corcho de la bodega {self.corcho.bodega} retirado del sacacorchos."
#         self.corcho = None
#         return mensaje




# corcho1 = Corcho("LA LINDA")
# botella1 = Botella(corcho1)


# sacacorchos = Sacacorchos()


# print(sacacorchos.destapar(botella1))  
# print(sacacorchos.destapar(botella1))  

# print(sacacorchos.limpiar())  
# print(sacacorchos.limpiar())  
# print(botella1)

# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: 
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un 
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase 
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los 
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame 
# al método. 


# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
        
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
       
#         print(f"Restaurante: {self.restaurante_nombre}")
#         print(f"Tipo de comida: {self.tipo_comida}")

#     def abrir_restaurante(self):
       
#         print(f"¡El restaurante {self.restaurante_nombre} ahora está abierto!")


# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
       
#         super().__init__(restaurante_nombre, tipo_comida)
        
#         self.sabores = sabores

#     def mostrar_sabores(self):
      
#         print("Sabores disponibles:")
#         for sabor in self.sabores:
#             print(f"- {sabor}")


# heladeria = Heladeria("GRIDO", "Helados", ["Chocolate", "Vainilla", "Fresa", "Menta"])


# heladeria.describir_restaurante()  
# heladeria.abrir_restaurante()  
# heladeria.mostrar_sabores()  

# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que 
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover 
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad. 
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro 
# personaje, al que le debe hacer el daño indicado por el atributo ataque. 
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que 
# devuelva la cantidad cosechada

# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad

#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             print("El personaje ha muerto.")
#             self.vida = 0  
#     def mover(self, direccion):
#         if direccion == "izquierda":
#             self.posicion -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion += self.velocidad
#         elif direccion == "arriba":
#             self.posicion += self.velocidad
#         elif direccion == "abajo":
#             self.posicion -= self.velocidad
#         else:
#             print("Dirección no válida")

# class Soldado:
#     def __init__(self, vida, posicion, velocidad, ataque):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
#         self.ataque = ataque

#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             print("El soldado ha muerto.")
#             self.vida = 0  

#     def mover(self, direccion):
#         if direccion == "izquierda":
#             self.posicion -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion += self.velocidad
#         elif direccion == "arriba":
#             self.posicion += self.velocidad
#         elif direccion == "abajo":
#             self.posicion -= self.velocidad
#         else:
#             print("Dirección no válida")
    
#     def atacar(self, personaje):
#         if hasattr(personaje, 'recibir_ataque'):  
#             print(f"El soldado ataca al personaje y le hace {self.ataque} de daño.")
#             personaje.recibir_ataque(self.ataque)
#         else:
#             print("El objetivo no es un personaje válido.")

# class Campesino:
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
#         self.cosecha = cosecha

#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             print("El campesino ha muerto.")
#             self.vida = 0  

#     def mover(self, direccion):
        
#         if direccion == "izquierda":
#             self.posicion -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion += self.velocidad
#         elif direccion == "arriba":
#             self.posicion += self.velocidad
#         elif direccion == "abajo":
#             self.posicion -= self.velocidad
#         else:
#             print("Dirección no válida")
    
#     def cosechar(self):
#         print(f"El campesino ha cosechado {self.cosecha} unidades de cultivo.")
#         return self.cosecha

# soldado = Soldado(100, 0, 10, 20)
# campesino = Campesino(80, 5, 5, 30)

# print(f"Vida del soldado: {soldado.vida}")
# print(f"Posición del campesino: {campesino.posicion}")

# soldado.mover("derecha")
# print(f"Posición del soldado después de moverse: {soldado.posicion}")

# soldado.atacar(campesino)
# print(f"Vida del campesino después de ser atacado: {campesino.vida}")

# campesino.cosechar()

# campesino.recibir_ataque(50)
# print(f"Vida del campesino después del ataque: {campesino.vida}")

# soldado.atacar(campesino)
# print(f"Vida del campesino después del segundo ataque: {campesino.vida}")


# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente 
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del 
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario. 
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno. 

# class Usuario:
#     def __init__(self, nombre, apellido, edad, email, telefono):
       
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.telefono = telefono

#     def describir_usuario(self):
       
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad} años")
#         print(f"Email: {self.email}")
#         print(f"Teléfono: {self.telefono}")

#     def saludar_usuario(self):
        
#         print(f"¡Hola, {self.nombre}! Bienvenido a tu perfil.")
        

# usuario1 = Usuario("Juan", "Pérez", 30, "juan.perez@example.com", "123-456-7890")
# usuario2 = Usuario("Ana", "Gómez", 25, "ana.gomez@example.com", "987-654-3210")
# usuario3 = Usuario("Carlos", "Martínez", 40, "carlos.martinez@example.com", "555-123-4567")

# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# print("\n") 

# usuario2.describir_usuario()
# usuario2.saludar_usuario()

# print("\n")  
# usuario3.describir_usuario()
# usuario3.saludar_usuario()


# # 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase 
# # Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede 
# # postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que 
# # muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.


# class Admin:
#     def __init__(self, nombre, apellido, edad, email, telefono, privilegios):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.email = email
#         self.telefono = telefono
#         self.privilegios = privilegios

#     def describir_usuario(self):
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad} años")
#         print(f"Email: {self.email}")
#         print(f"Teléfono: {self.telefono}")

#     def saludar_usuario(self):
#         print(f"¡Hola, {self.nombre}! Bienvenido a tu perfil de administrador.")

#     def mostrar_privilegios(self):
#         print(f"Privilegios de {self.nombre}:")
#         for privilegio in self.privilegios:
#             print(f"- {privilegio}")

# privilegios_admin = ["puede postear en el foro", "puede borrar un post", "puede banear usuarios", "puede editar el perfil de otros"]
# admin = Admin("Luis", "Fernández", 35, "luis.fernandez@example.com", "333-444-5555", privilegios_admin)

# admin.describir_usuario()
# admin.saludar_usuario()
# admin.mostrar_privilegios()    

# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings 
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta 
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use 
# el método para mostrar privilegios. 
        
# class Privilegios:
#     def __init__(self):
#         self.privilegios = ["Acceder a todas las áreas", "Modificar usuarios", "Eliminar registros", "Configurar sistema"]
    
#     def mostrar_privilegios(self):
#         print(f"Privilegios de Admin:")
#         for privilegio in self.privilegios:
#             print(f"- {privilegio}")

# class Admin:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.privilegios = Privilegios()

# admin1 = Admin("Carlos")

# admin1.privilegios.mostrar_privilegios()

# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela 
# al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación 
# funcionó. 

 
import retaurante

def Restaurante
print(retaurante.abrir_restaurante)


