from colorama import init, Fore, Back, Style
inventario = {
"A001": ("Laptop", 1500),
"A002": ("Mouse", 25),
"A003": ("Teclado", 45),
"A004": ("Monitor", 300),
"A005": ("Impresora", 120)
}
def mostrar_inventario(inventario):
    for x in inventario.keys():
        print(f"Codigo: {x}, Descripcion: {inventario[x][0]}, precio: ${inventario[x][1]}")

def mostrar_producto(inventario):
    prod=input("Ingrese el codigo del producto que desea buscar: ")
    if prod in inventario:
        print(f"Producto encontrado!: {inventario[prod][0]}, Precio: ${inventario[prod][1]}")
    else:
        print("No se encontro el producto")

def modificar_precio(inventario, cod, prec):
    if cod in inventario:
        inventario[cod]=inventario[cod][0],prec
        print(f"El precio del producto con código {cod} ha sido actualizado a ${inventario[cod][1]}")
    else:
        print("No se encontro el producto")

def eliminar_producto(inventario, cod):
    inventario.pop(cod)
    print(f"Se ha eliminado el producto con el codigo {cod}")

def productos_por_rango_de_precio(inventario, p1, p2):
    for x in inventario:
        if inventario[x][1]>p1 and inventario[x][1]<p2:
            print(f"Descripcion : {inventario[x][0]}, Precio : $ {inventario[x][1]}")

def menu():
    rta=1
    while True:
        rta=input("""
                                   ===============================================================================
                                   =================================== MENU ======================================
                                   =                                                                             =
                                   =                       1 - Mostrar productos                                 =
                                   =                       2 - Buscar producto                                   =
                                   =                       3 - Modificar precio                                  =
                                   =                       4 - Eliminar producto                                 =
                                   =                       5 - Buscar por rango de precio                        =
                                   =                       0 - Salir                                             =
                                   =                                                                             =
                                   ===============================================================================
                                   """)
        match rta:
            case "1":
                mostrar_inventario(inventario)
            case "2":
                mostrar_producto(inventario)
            case "3":
                codigo=input("Ingrese el codigo del producto al cual desea modificar el precio: ")
                precio=input("Ingrese el precio que desea asignarle: $")
                modificar_precio(inventario,codigo,precio)
            case "4":
                cod2=input("Ingrese el codigo del producto que desea eliminar: ")
                eliminar_producto(inventario,cod2)
            case "5":
                pm=int(input("Ingrese el menor valor: "))
                pmas=int(input("Ingrese el mayor valor: "))
                productos_por_rango_de_precio(inventario,pm,pmas)
            case "0":
                break
            case _:
                print("Ingrese una opcion valida")
menu()