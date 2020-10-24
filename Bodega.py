#importamos la libreria sys para el metodo salir de la clase Menu
import sys

#definimos la clase Articulo con los 
#metodos imprimirDatosArticulo, getId, y su respectivo constructor

class Articulo:
    #metodo constructor
    #cada vez que se instancie un objeto de la clase Articulo se le tendran que pasar como parametros 4 variables, codigo, nombre, cantidad, precio, para despues vaciarlas en 
    #otras variable de tipo privado que seran los atributos de la clase u objeto
    def __init__(self,codigo,nombre,cantidad,precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__cantidad=cantidad
        self.__precio=precio
      #el metodo imprimirDatosArticulo sirve para 
      #imprimir cada atributo de la clase
      #se define el metodo
    def imprimirDatosArticulo(self):
        #las siguientes 4 lineas imprimen los atributos del objeto
        print(f"Codigo: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Cantidad: {self.__cantidad}")
        print(f"Precio: {self.__precio}")
     #el metodo getId se define con el proposito de
     #poder acceder al codigo o id del articulo 
     #se define el metodo
    def getId(self):
        #retorna el codigo id
        return self.__codigo
        
 # se define la clase Stock que servira como clase de almacenamiento/registro, impresora y eliminadora de los articulos gracias a sus respectivos metodos
class Stock:
    #definimos el metodo constructor con un espacio en memoria de tipo lista
    def __init__(self):
        self.__stock=list()
       #definimos otro metodo llamaso añadirArticulo que tendra la funcion de añadir un articulo al atributo stock de la clase Stock
    def añadirArticulo(self,articulo):
        #se toma el parametro que se pasa y se añade con la funcion de la lista 'append'
        self.__stock.append(articulo)
       #se define el metodo eliminarArticulo que sirve para eliminar los articulos del stock, se pasa como parametro el codigo del producto
    def eliminarArticulo(self,codigo):
        #se declara una lista para almacenar los codigos
        self.indices=list()
        #se recorre la lista stock y se toma con ayuda de la funcion getId de la clase Articulo el id
        for i in self.__stock:
            self.indices.append(i.getId())
            #recorremos la lista indices para despuea comparar si es igual al codigo que pasamos colo parametro
        for i in self.indices:
            #si es igual lo almacenamos en una variable llamada indixe
            if i==codigo:
                indice=self.indices.index(i)
         #luego esa variable la pasamos como parametro al metodo pop de la lista stock
        self.__stock.pop(indice)
        #listo se ha eliminado
        
        #se define la clase mostrar articulos, la cual
        #ayuda a imprimir los articulos almacenados hasta el momento
    def mostrarArticulos(self):
        #se reforre cada valor de la lista stock
        for i in self.__stock:
            print("------------------------------------------------")
            #llamamos al metodo imprimirDatosArticulo de cada elemento de la lista
            i.imprimirDatosArticulo()
            
            
            #se define el metodo checarIds para verificar que los ids no se repitan
    def checarIds(self):
        #definimos una variable donde iran los ids
        self.__ids=list()
        for i in self.__stock:
            #recorremos cada elemento y obtenemos su id con el metodo getId
            self.__ids.append(i.getId())
           #retornamos la lista
        return self.__ids
      #metodo que sirve para devolver la lista de articulos
    def articulos(self):
        #retornamos la lista
        return self.__stock
 # se define una clase llamada Menu para el menu
class Menu:
    #se define wl metodo constructor que actuara como lanzador del menu
    def __init__(self):
        #llamamos al metodo mostrarMenu para lanzar el menu
        self.mostrarMenu()
        #se define el metodo que contiene el menu
    def mostrarMenu(self):
        #imprimimos laa opciones
        print('Sistema De Alta y Baja de Articulos')
        print("1)Añadir Articulo\n2)Eliminar Articulo\n3)Imprimir Articulos\n4)Salir")
        #definimos varios ciclo while seguidos de un bloque try para controlar excepciones y solo se pueda introducir un valor valido
        while True:
            try:
                respuesta = int(input())
            except:
                print("Valor no admintido.(Solo enteros)")
            else:
                break
        if respuesta==1:
            avanzar=True
            #definimos varios ciclo while seguidos de un bloque try para controlar excepciones y solo se pueda introducir un valor valido
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
            #definimos varios ciclo while seguidos de un bloque try para controlar excepciones y solo se pueda introducir un valor valido
            while True:
                opcion=input("¿Desea guardar los datos? si/no")
                if opcion.lower()=="si":
                    articulo=Articulo(id,name,quantity,price)
                    stock.añadirArticulo(articulo)
                    print("Articulo guardado con exito.")
                    break
                else:
                    print("Intenta de nuevo")
        #opcion que muestra en pantalla los articulos almacenados hasta el momento para despues elegir el que queremos eliminar
        elif respuesta==2:
            #imprimimos los articulos
            stock.mostrarArticulos()
            #definimos varios ciclo while seguidos de un bloque try para controlar excepciones y solo se pueda introducir un valor valido
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
                        #si pasamos los filtros se elimina el articulo con el metodo eliminae articulo
                            stock.eliminarArticulo(eleccion)
                        except:
                            #si no existe el articulo o es un valor no valido nos arroja un error
                            print("Codigo no existe, o valor no es admitido, intente de nuevo")
                            continue
                        else:
                            #si si se cumple nos arroja el mensaje de exito
                            print("Articulo eliminado con exito.")
                            break


#opcion que nos imprime los articulos en dado caso que tengamos
#gracias al metdo mostrarArticulos del objeto stock
        elif respuesta==3:
            stock.mostrarArticulos()
            
        elif respuesta==4:
            #metodo que finaliza el programa con el metodo exit de la libreria sys
            sys.exit()
        else:
            print("Estimado usuario, la opcion no existe")




#instanciamos el stock
stock=Stock()

#definimos un bucle while para la continua ejecucion del programa y dentro de el instanciamos un objeto de la clase Menu
while True:
    menu=Menu()

