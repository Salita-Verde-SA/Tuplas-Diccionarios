from colorama import init, Fore, Back, Style
def mostrar_inventario(inventario):
     #.items : Recorrer claves y valores
     for codigo, (descripcion, precio) in inventario.items():
        print(f"{Fore.RED}Código:{Fore.WHITE} {codigo}, Descripción: {descripcion}, Precio:{Fore.BLUE} ${precio}")

def buscar_producto(inventario, codigo):
    if codigo in inventario:
        descripcion, precio = inventario[codigo]
        print(f"{Fore.WHITE}Producto {Fore.RED}Encontrado: {Fore.WHITE}Descripción: {descripcion}, Precio:{Fore.BLUE} ${precio}")
    else:
        print(F"{Fore.RED}Producto no encontrado.")
        
def modificar_precio(inventario, codigo):
    if codigo in inventario:
        nuevo_precio = float(input(f"{Fore.WHITE}Ingrese el nuevo precio: "))
        descripcion = inventario[codigo][0]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"{Fore.WHITE}El precio del producto {descripcion} ha sido actualizado a{Fore.BLUE} ${nuevo_precio}.")
    else:
        print(F"{Fore.RED}Producto no encontrado.")
def eliminar_producto(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo] 
        print(f"{Fore.RED}El producto con codigo {codigo} ha sido eliminado del inventario.")
    else:
        print(f"{Fore.RED}El producto con código {codigo} no existe en el inventario.")

def productos_por_rango_de_precio(inventario, preciominimo, preciomaximo):
    print(f"{Fore.WHITE}Productos en el rango de precio entre ${preciominimo} y ${preciomaximo}:")
    productos_en_rango = False
    for codigo, (descripcion, precio) in inventario.items():
        if preciominimo <= precio <= preciomaximo:
            print(f"{Fore.WHITE}Código: {codigo}, Descripción:{Fore.RED} {descripcion}, Precio: {Fore.BLUE}${precio}")
            productos_en_rango = True

inventario = {
    "A001": ("Teclado", 15000),
    "A002": ("Monitor", 250000),
    "A003": ("Mouse", 14000),
    "A004": ("Ram", 18000),
    "A005": ("Auriculares", 6000)
}
mostrar_inventario(inventario)
codigo = input(f"{Fore.WHITE}Ingresa el codigo: ")
buscar_producto(inventario, codigo)
modificar_precio(inventario, codigo)
codigo = input(f"{Fore.WHITE}Ingrese el codigo del elemento que quiera eliminar: ")
eliminar_producto(inventario, codigo)
print(inventario)
preciominimo= float(input(f"{Fore.WHITE}Ingrese el precio Minimo: "))
preciomaximo= float(input(f"{Fore.WHITE}Ingrese el precio Maximo: "))
productos_por_rango_de_precio(inventario, preciominimo, preciomaximo)
