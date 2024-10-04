from colorama import Fore


def mostrar_inventario(inventario):
    # .items : Recorrer claves y valores
    descripciones, precios = obtener_productos(inventario)
    for codigo, _ in descripciones.items():
        print(
            f"{Fore.RED}Código:{Fore.WHITE} {codigo}, Descripcion: {Fore.BLUE}{descripciones[codigo]},{Fore.WHITE} Precio:{Fore.BLUE} ${precios[codigo]}"
        )


def obtener_productos(inventario):
    precios = {}
    descripciones = {}
    for codigo, (descripcion, precio) in inventario.items():
        descripciones[codigo] = descripcion
        precios[codigo] = precio
    return descripciones, precios


def buscar_producto(inventario, codigo, retorno: bool):
    if codigo in inventario:
        descripciones, precios = obtener_productos(inventario)
        precio = precios[codigo]
        descripcion = descripciones[codigo]
        if retorno:
            return descripcion, precio
        else:
            print(
                f"{Fore.WHITE}Producto {Fore.RED}Encontrado: {Fore.WHITE}Descripcion:{Fore.BLUE} {descripcion}{Fore.WHITE}, Precio:{Fore.BLUE} ${precio}"
            )
    else:
        print(f"{Fore.RED}Producto no encontrado.")


def modificar_precio(inventario, codigo):
    if codigo in inventario:
        descripcion, precio = buscar_producto(inventario, codigo, True)
        nuevo_precio = float(input(f"{Fore.WHITE}Ingrese el nuevo precio: "))
        inventario[codigo] = (descripcion, nuevo_precio)
        print(
            f"{Fore.WHITE}El precio del producto {descripcion} ha sido actualizado de {Fore.BLUE}${precio} {Fore.WHITE}a {Fore.BLUE}${nuevo_precio}."
        )
    else:
        print(f"{Fore.RED}Producto no encontrado.")


def eliminar_producto(inventario, codigo):
    if codigo in inventario:
        inventario.pop(codigo)
        print(
            f"{Fore.RED}El producto con codigo {codigo} ha sido eliminado del inventario."
        )
    else:
        print(f"{Fore.RED}El producto con código {codigo} no existe en el inventario.")


def productos_por_rango_de_precio(inventario, preciominimo, preciomaximo):
    print(
        f"{Fore.WHITE}Productos en el rango de precio entre ${preciominimo} y ${preciomaximo}:"
    )

    descripciones, precios = obtener_productos(inventario)
    contador = 0

    for codigo, _ in inventario.items():
        if preciominimo <= precios[codigo] <= preciomaximo:
            contador += 1
            print(
                f"{Fore.WHITE}Código: {codigo}, Descripción:{Fore.RED} {descripciones[codigo]}{Fore.WHITE}, Precio: {Fore.BLUE}${precios[codigo]}"
            )
    if contador == 0:
        print("Ninguno.")


inventario = {
    "A001": ("Teclado", 15000),
    "A002": ("Monitor", 250000),
    "A003": ("Mouse", 14000),
    "A004": ("Ram", 18000),
    "A005": ("Auriculares", 6000),
}
mostrar_inventario(inventario)
codigo = input(f"{Fore.WHITE}Ingresa el codigo: ")
buscar_producto(inventario, codigo, False)
modificar_precio(inventario, codigo)
codigo = input(f"{Fore.WHITE}Ingrese el codigo del elemento que quiera eliminar: ")
eliminar_producto(inventario, codigo)

preciominimo = float(input(f"{Fore.WHITE}Ingrese el precio Minimo: "))
preciomaximo = float(input(f"{Fore.WHITE}Ingrese el precio Maximo: "))
productos_por_rango_de_precio(inventario, preciominimo, preciomaximo)
