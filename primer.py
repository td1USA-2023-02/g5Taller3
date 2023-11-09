class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock

    def agregar_producto(self):
        print(f"{self.nombre} ha sido agregado al almacén.")

    def actualizar_stock(self, cantidad):
        self.cantidad_en_stock += cantidad
        print(f"La cantidad en stock de {self.nombre} ha sido actualizada a {self.cantidad_en_stock}.")

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad en stock: {self.cantidad_en_stock}"

def main():
    productos = []
    while True:
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Ver productos")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Introduce el nombre del producto: ")
            precio = float(input("Introduce el precio del producto: "))
            cantidad_en_stock = int(input("Introduce la cantidad en stock del producto: "))
            producto = Producto(nombre, precio, cantidad_en_stock)
            productos.append(producto)
            producto.agregar_producto()
        elif opcion == "2":
            print("Productos disponibles:")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto.nombre}")
            indice_producto = int(input("Elige el número del producto a actualizar: ")) - 1
            cantidad = int(input("Introduce la cantidad a agregar al stock: "))
            productos[indice_producto].actualizar_stock(cantidad)
        elif opcion == "3":
            for producto in productos:
                print(producto.mostrar_info())
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
