class Ventana:
    def __init__(self,titulo,x_sup=0,y_sup=0,x_inf=500,y_inf=500):
        self.__titulo=titulo
        self.__x_sup=x_sup
        self.__y_sup=y_sup
        self.__x_inf=x_inf
        self.__y_inf=y_inf
    def mostrar(self):
        print('\nTitulo:{}    Esq. Superior izquierda:({},{})  Esq. Inferior Derecha:({},{})\n'.format(self.__titulo,self.__x_sup,self.__y_sup,self.__x_inf,self.__y_inf))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__y_inf - self.__y_sup
    def ancho(self):
        return self.__x_inf - self.__x_sup
    def moverDerecha(self,n=1):
        if self.__x_inf<500:
            self.__x_sup+=n
            self.__x_inf+=n
        else:
            print('No se puede mover a la derecha\n')
    def moverIzquierda(self,n=1):
        if self.__x_sup>0:
            self.__x_sup-=n
            self.__x_inf-=n
        else: 
            print('No se puede mover a la izquierda\n')
    def bajar(self,n=1):
        if self.__y_inf<500:
            self.__y_sup+=n
            self.__y_inf+=n
        else:
            print('No se puede bajar la ventana\n')
    def subir(self,n=1):
        if self.__y_sup>0:
            self.__y_sup-=n
            self.__y_inf-=n
        else:
            print('No se puede subir la ventana\n')
    