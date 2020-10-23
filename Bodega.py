
import sys



class Articulo:
    def __init__(self,codigo,nombre,cantidad,precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__cantidad=cantidad
        self.__precio=precio
    def imprimirDatosArticulo(self):
        print(f"Codigo: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Cantidad: {self.__cantidad}")
        print(f"Precio: {self.__precio}")
    def getId(self):
        return self.__codigo
class Stock:
    def __init__(self):
        self.__stock=list()
    def añadirArticulo(self,articulo):
        self.__stock.append(articulo)
    def eliminarArticulo(self,codigo):
        self.indices=list()
        for i in self.__stock:
            self.indices.append(i.getId())
        for i in self.indices:
            if i==codigo:
                indice=self.indices.index(i)
        self.__stock.pop(indice)
    def mostrarArticulos(self):
        for i in self.__stock:
            print("------------------------------------------------")
            i.imprimirDatosArticulo()
    def checarIds(self):
        self.__ids=list()
        for i in self.__stock:
            self.__ids.append(i.getId())
        return self.__ids
    def articulos(self):
        return self.__stock
class Menu:
    def __init__(self):
        self.mostrarMenu()
    def mostrarMenu(self):
        print("1)Añadir Articulo\n2)Eliminar Articulo\n3)Imprimir Articulos\n4)Salir")
        while True:
            try:
                respuesta = int(input())
            except:
                print("Valor no admintido.(Solo enteros)")
            else:
                break
        if respuesta==1:
            avanzar=True
            while avanzar:
                print("Codigo del producto")

                try:
                    id=int(input())
                except:
                    print("Solo enteros.")
                else:
                    if len(stock.articulos())==0:
                        break
                    elif len(stock.articulos())>0:
                        for i in stock.checarIds():
                            if i==id:
                                print("Ya hay un producto con este codigo. Intente con otro")
                                continue
                            else:
                                avanzar=False
            name=input("Nombre del producto\n")
            while True:
                print("Cantidad de producto")
                try:
                    quantity=int(input())
                except:
                    print("Solo enteros.")
                else:
                    break
            while True:
                print("Precio del producto")
                try:
                    price = int(input())
                except:
                    print("Solo enteros.")
                else:
                    break

            while True:
                opcion=input("¿Desea guardar los datos? si/no")
                if opcion.lower()=="si":
                    articulo=Articulo(id,name,quantity,price)
                    stock.añadirArticulo(articulo)
                    print("Articulo guardado con exito.")
                    break
                else:
                    print("Intenta de nuevo")

        elif respuesta==2:
            stock.mostrarArticulos()
            while True:
                try:

                    eleccion = int(input("introduce el codido del articulo que desea borrar\n 0 para regresar \n"))
                except:
                    print("Valor no valido")
                else:
                    if eleccion==0:
                        break

                    else:
                        try:

                            stock.eliminarArticulo(eleccion)
                        except:
                            print("Codigo no existe, o valor no es admitido, intente de nuevo")
                            continue
                        else:
                            print("Articulo eliminado con exito.")
                            break




        elif respuesta==3:
            stock.mostrarArticulos()
        elif respuesta==4:
            sys.exit()
        else:
            print("Estimado usuario, la opcion no existe")





stock=Stock()

while True:
    menu=Menu()
