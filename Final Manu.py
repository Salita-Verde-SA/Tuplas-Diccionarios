from colorama import Fore as fore


def mostrar_inventario(inventario: dict):
    for codigo in inventario.keys():
        descripcion, precio = inventario.get(codigo)
        print(
            f"Código: {fore.MAGENTA}{codigo}{fore.RESET}, Descripción: {fore.BLUE}{descripcion}, {fore.RESET}Precio: {fore.YELLOW}${precio}{fore.RESET}"
        )


def buscar_producto(inventario: dict, codigo: str):
    if inventario.get(codigo):
        descripcion, precio = inventario.get(codigo)
        print(
            f"Se encontró el producto {fore.BLUE}{descripcion} {fore.RESET}con el precio de {fore.YELLOW}${precio}{fore.RESET}"
        )
    else:
        print("No se encontró el producto buscado.")


def modificar_precio(inventario: dict, codigo: str, nuevoPrecio: float):
    if inventario.get(codigo):
        descripcion, precio = inventario.get(codigo)
        nuevoValor = (descripcion, nuevoPrecio)
        inventario.update({codigo: nuevoValor})
        print(
            f"Se actualizó el precio del producto con el código {fore.MAGENTA}{codigo} {fore.RESET}de {fore.YELLOW}${precio} {fore.RESET}a {fore.YELLOW}${nuevoPrecio}{fore.RESET}."
        )
    else:
        print("No se encontró el producto buscado.")


def eliminar_producto(inventario: dict, codigo: str):
    if inventario.get(codigo):
        eliminado, _ = inventario.pop(codigo)
        print(
            f"Se {fore.RED}eliminó {fore.RESET}el producto {fore.BLUE}{eliminado} {fore.RESET}con el código {fore.MAGENTA}{codigo} {fore.RESET}del inventario."
        )
    else:
        print("No se encontró el producto buscado.")


def productos_por_rango_de_precio(inventario: dict, min, max):
    c = {}
    for codigo, producto in inventario.items():
        if min < producto[1] < max:
            c.update({codigo: producto})
    if c.keys():
        print(
            f"Productos en el rango de precios entre {fore.YELLOW}${min} {fore.RESET}y {fore.YELLOW}${max}{fore.RESET}:"
        )
        mostrar_inventario(c)
    else:
        print(
            f"No se han encontrado productos dentro del rango de precios especificado."
        )


inventario = {
    "A001": ("Laptop", 1500),
    "A002": ("Mouse", 25),
    "A003": ("Teclado", 45),
    "A004": ("Monitor", 300),
    "A005": ("Impresora", 120),
}

mostrar_inventario(inventario)
buscar_producto(inventario, "A003")
modificar_precio(inventario, "A004", 350)
eliminar_producto(inventario, "A002")
productos_por_rango_de_precio(inventario, 100, 500)
