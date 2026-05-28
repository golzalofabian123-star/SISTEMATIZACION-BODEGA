# SISTEMA DE BODEGA "DONDE JAVI"

productos = {}
ventas = []
ingresos_totales = 0


def pausar():

    input("\nPresione ENTER para continuar...")


# ===== PRODUCTOS =====

def menu_productos():

    while True:

        print("\n===== PRODUCTOS =====")
        print("1. Registrar producto")
        print("2. Cambiar precio")
        print("3. Ver productos")
        print("4. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            nombre = input(
                "\nNombre producto: "
            )

            if nombre in productos:

                print(
                    "Producto ya existe."
                )

            else:

                precio = float(
                    input("Precio S/: ")
                )

                productos[nombre] = precio

                print(
                    "Producto registrado."
                )

            pausar()

        elif opcion == "2":

            nombre = input(
                "\nProducto: "
            )

            if nombre in productos:

                nuevo = float(
                    input(
                        "Nuevo precio: S/"
                    )
                )

                productos[nombre] = nuevo

                print(
                    "Precio actualizado."
                )

            else:

                print(
                    "Producto no encontrado."
                )

            pausar()

        elif opcion == "3":

            print(
                "\n=== PRODUCTOS ==="
            )

            if len(productos) == 0:

                print(
                    "No hay productos."
                )

            else:

                for nombre, precio in productos.items():

                    print(
                        nombre,
                        "- S/",
                        precio
                    )

            pausar()

        elif opcion == "4":

            break

        else:

            print(
                "Opción inválida."
            )

            pausar()


# ===== VENTAS =====

def menu_ventas():

    global ingresos_totales

    while True:

        print("\n===== VENTAS =====")
        print("1. Registrar venta")
        print("2. Historial")
        print("3. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            producto = input(
                "\nProducto: "
            )

            if producto not in productos:

                print(
                    "Producto inexistente."
                )

            else:

                cantidad = int(
                    input(
                        "Cantidad: "
                    )
                )

                precio = productos[
                    producto
                ]

                total = precio * cantidad

                ventas.append({

                    "producto": producto,

                    "cantidad": cantidad,

                    "precio": precio,

                    "total": total

                })

                ingresos_totales += total

                print(
                    f"Venta registrada. Total: S/{total}"
                )

            pausar()

        elif opcion == "2":

            print(
                "\n=== HISTORIAL ==="
            )

            if len(ventas) == 0:

                print(
                    "No existen ventas."
                )

            else:

                for venta in ventas:

                    print(

                        venta["producto"],

                        "| Cantidad:",

                        venta["cantidad"],

                        "| Total:",

                        venta["total"]

                    )

            pausar()

        elif opcion == "3":

            break

        else:

            print(
                "Opción inválida."
            )

            pausar()


# ===== REPORTES =====

def menu_reportes():

    while True:

        print(
            "\n===== REPORTES ====="
        )

        print(
            "1. Ver ingresos"
        )

        print(
            "2. Volver"
        )

        opcion = input(
            "Seleccione: "
        )

        if opcion == "1":

            print(
                "\nIngresos Totales: S/",
                ingresos_totales
            )

            pausar()

        elif opcion == "2":

            break

        else:

            print(
                "Opción inválida."
            )

            pausar()


# ===== MENU PRINCIPAL =====

while True:

    print(
        "\n====== BODEGA DONDE JAVI ======"
    )

    print("1. Productos")
    print("2. Ventas")
    print("3. Reportes")
    print("4. Salir")

    opcion = input(
        "Seleccione: "
    )

    if opcion == "1":

        menu_productos()

    elif opcion == "2":

        menu_ventas()

    elif opcion == "3":

        menu_reportes()

    elif opcion == "4":

        print(
            "Sistema finalizado."
        )

        break

    else:

        print(
            "Opción inválida."
        )

        pausar()