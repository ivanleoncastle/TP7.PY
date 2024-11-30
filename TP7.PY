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