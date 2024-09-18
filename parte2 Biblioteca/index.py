class Item:
    def __init__(self, nombre, cantidad, disponibilidad):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__disponibilidad = disponibilidad
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")
    def get_disponibilidad(self):
        return self.__disponibilidad

    def set_disponibilidad(self, disponibilidad):
        if disponibilidad in [True, False]:
            self.__disponibilidad = disponibilidad
        else:
            print("Disponibilidad debe ser True o False.")
    def mostrar_info(self):
        disponibilidad_str = "Disponible" if self.__disponibilidad else "No disponible"
        return f"Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Disponibilidad: {disponibilidad_str}"
    
    def prestar(self):
        if self.__disponibilidad and self.__cantidad > 0:
            self.__cantidad -= 1
            if self.__cantidad == 0:
                self.set_disponibilidad(False)  # Si ya no hay más, lo marcamos como no disponible
            print(f"Se ha prestado '{self.__nombre}'. Quedan {self.__cantidad} disponibles.")
        else:
            print(f"'{self.__nombre}' no está disponible para préstamo.")
            
    def devolver(self):
        self.__cantidad += 1
        if not self.__disponibilidad:
            self.set_disponibilidad(True)  # Al devolverlo, se marca como disponible
        print(f"Se ha devuelto '{self.__nombre}'. Ahora hay {self.__cantidad} disponibles.")

    
class Libro(Item):
    def __init__(self, nombre, cantidad, disponibilidad):
        Item.__init__(self, nombre, cantidad, disponibilidad )
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"[Libro] {info_base}"


class Revista(Item):
    def __init__(self, nombre,cantidad, disponibilidad):
        Item.__init__(self, nombre,cantidad, disponibilidad )
        
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"[Revista] {info_base}" 
        
        
        
class Biblioteca:
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item):
        self.items.append(item)
    
    def prestar_item(self, nombre):
        for item in self.items:
            if item.get_nombre() == nombre:
                item.prestar()
                return
        print(f"El ítem     '{nombre}' no se encuentra en la biblioteca.")
        
    def devolver_item(self, nombre):
        for item in self.items:
            if item.get_nombre() == nombre:
                item.devolver()
                return   
            
    def mostrar_informacion_items(self):
        for item in self.items:
            print(item.mostrar_info())




biblioteca = Biblioteca()


libro1 = Libro("El Quijote", 3, True)
revista1 = Revista("National Geographic", 5, True)

biblioteca.agregar_item(libro1)
biblioteca.agregar_item(revista1)

# Mostrar la información de todos los ítems
biblioteca.mostrar_informacion_items()