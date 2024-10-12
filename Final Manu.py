from colorama import Fore as fore


def mostrar_inventario(inventario: dict):
    for i in inventario.keys():
        print(
            f"Código: {fore.MAGENTA}{i}{fore.RESET}, Descripción: {fore.BLUE}{inventario.get(i)[0]}, {fore.RESET}Precio: {fore.YELLOW}${inventario.get(i)[1]}{fore.RESET}"
        )


def buscar_producto(inventario: dict, codigo: str):
    if inventario.get(codigo):
        print(
            f"Se encontró el producto {fore.BLUE}{inventario.get(codigo)[0]} {fore.RESET}con el precio de {fore.YELLOW}${inventario.get(codigo)[1]}{fore.RESET}"
        )
    else:
        print("No se encontró el producto buscado")


def modificar_precio(inventario: dict, codigo: str, nuevoPrecio):
    if inventario.get(codigo):
        nuevoValor = (inventario.get(codigo)[0], nuevoPrecio)
        inventario.update({codigo: nuevoValor})
        print(
            f"Se actualizó el precio del producto con el código {fore.MAGENTA}{codigo} {fore.RESET}a {fore.YELLOW}${nuevoPrecio}{fore.RESET}"
        )
    else:
        print("No se encontró el producto buscado")


def eliminar_producto(inventario: dict, codigo: str):
    if inventario.get(codigo):
        eliminado = inventario.pop(codigo)
        print(
            f"Se {fore.RED}eliminó {fore.RESET}el producto {fore.BLUE}{eliminado[0]} {fore.RESET}del inventario"
        )
    else:
        print("No se encontró el producto buscado")


def productos_por_rango_de_precio(inventario: dict, min, max):
    c = {}
    for i in inventario.keys():
        if min < inventario.get(i)[1] < max:
            c.update({i: inventario.get(i)})
    print(
        f"Productos en el rango de precios entre {fore.YELLOW}${min} {fore.RESET}y {fore.YELLOW}${max}{fore.RESET}:"
    )
    for i in c.keys():
        print(
            f"Código: {fore.MAGENTA}{i}{fore.RESET}, Descripción: {fore.BLUE}{c.get(i)[0]}, {fore.RESET}Precio: {fore.YELLOW}${c.get(i)[1]}{fore.RESET}"
        )


inventario = {
    "A001": ("Laptop", 1500),
    "A002": ("Mouse", 25),
    "A003": ("Teclado", 45),
    "A004": ("Monitor", 300),
    "A005": ("Impresora", 120),
}


mostrar_inventario(inventario)
codigo = input(f"{fore.WHITE}Ingrese el código del producto: ")
buscar_producto(inventario, codigo)

nuevoPrecio = int(input(f"{fore.WHITE}Ingrese el nuevo precio para el producto: "))
modificar_precio(inventario, codigo, nuevoPrecio)

codigo = input(f"{fore.WHITE}Ingrese el código del producto que desee eliminar: ")
eliminar_producto(inventario, codigo)

preciominimo = float(input(f"{fore.WHITE}Ingrese el precio mínimo: "))
preciomaximo = float(input(f"{fore.WHITE}Ingrese el precio máximo: "))
productos_por_rango_de_precio(inventario, preciominimo, preciomaximo)
