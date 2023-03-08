import itertools

class Alfabeto:   
    def __init__(self, alfabeto1, alfabeto2):
        self.alfabeto1 = alfabeto1
        self.alfabeto2 = alfabeto2

    def Crear(self):
        self.alfabeto1 = ()
        self.alfabeto2 = () 
        while True:
            dato1 = input("Digite el primer alfabeto (cadena vacia es #, escriba 'salir' para terminar): ")
            if dato1 == "salir":
                break

            if dato1 == ',' or dato1 == ';' or dato1 == '.' or dato1 == ':' or dato1 == '-' or dato1 == '_' or dato1 == '{' or dato1 == '}' or dato1 == '(' or dato1 == ')' or dato1 == '/' or dato1 == '=' or dato1 == '"' or dato1 == '!' or dato1 == '|' or dato1 == '°':
                print("DATO INVALIDO, ingrese otro valor ")

            elif dato1 == '' or dato1 == '#':
                dato1 = " "
            self.alfabeto1 = self.alfabeto1 + (dato1,)

        while True:
            dato2 = input("Digite el segundo alfabeto (cadena vacia es #, escriba 'salir' para terminar): ")
            if dato2 == "salir":
                break

            if dato2 == ',' or dato2 ==';' or dato2 =='.' or dato2 == ':' or dato2 =='-' or dato2 == '_' or dato2 == '{' or dato2 == '}' or dato2 == '(' or dato2 == ')' or dato2 == '/' or dato2 == '=' or dato2 =='"' or dato2 == '!' or dato2 == '|' or dato2 == '°':
                print("DATO INVALIDO, ingrese otro valor ")

            elif dato2 == '' or dato2 == '#':
                dato2 = " "
            self.alfabeto2 = self.alfabeto2 + (dato2,)


class Union(Alfabeto):
    def __init__(self, alfabeto1, alfabeto2):
        super().__init__(alfabeto1, alfabeto2)

    def Unir(self):
        U = set(self.alfabeto1) | set(self.alfabeto2)
        return U

class Diferencia(Alfabeto):
    def __init__(self, alfabeto1, alfabeto2):
        super().__init__(alfabeto1, alfabeto2)

    def Diferente(self):
        D1 = set(self.alfabeto1) - set(self.alfabeto2)
        D2 = set(self.alfabeto2) - set(self.alfabeto1)
        if not D1 & D2:
            return"No hay numeros diferentes"
        else:
            return D1, D2
        

class Interseccion(Alfabeto):
    def __init__(self, alfabeto1, alfabeto2):
        super().__init__(alfabeto1, alfabeto2)

    def EncontrarInterseccion(self):
        interseccion = set(self.alfabeto1) & set(self.alfabeto2)
        if not interseccion :
            return f"No hay numeros iguales "
        else:
            return f"La intercepción de los dos alfabetos es: {interseccion}"

class CerraduraEstrella(Alfabeto):
    def __init__(self, alfabeto1, alfabeto2):
        super().__init__(alfabeto1, alfabeto2)
        self.C = () 
        
    def CrearCerraduraEstrella(self):
        n = input("Ingrese cuántas palabras desea obtener de la cerradura estrella (digite 0 para obtener la cadena vacía): ")
        if n == None:
            print("Digite un valor")
        elif n.isnumeric():
            
            n = int(n)
            concatenacion =  [a + b for a in self.alfabeto1 for b in self.alfabeto2]
            cerradura = []
            for i in range(1, n + 1):
                for palabra in itertools.product(concatenacion, repeat=i):
                    cerradura.append(''.join(palabra))
            

            if n <= len(cerradura):
                self.C = cerradura[:n]
                print(f"Cerradura estrella: {self.C}")
            else:
                print("Error: El número ingresado es mayor que la cantidad de palabras en la cerradura estrella.")
        else:
            print("Error: El valor ingresado no es un número.")

            
        
    def GuardarTuplas(self):
        mitad = len(self.C) // 2
        self.tupla1 = tuple(self.C[:mitad])
        self.tupla2 = tuple(self.C[mitad:])

        return self.tupla1,self.tupla2
        
    def UnirTuplas(self):
        self.uniontupla = set(self.tupla1) | set(self.tupla2)
        return self.uniontupla
    
    def DiferenciaTuplas(self):
        DT1 = set(self.tupla1) - set(self.tupla2)
        DT2 = set(self.tupla2) - set(self.tupla1)
        if not DT1 & DT2:
            return "No hay diferencia de lenguaje "
        else:
            return DT1,DT2
    
    def EncontrarInterseccionTupla(self):
        interseccionT = set(self.alfabeto1) & set(self.alfabeto2)
        if not interseccionT:
            return "No hay palabras iguales"
        else:
            return f"La intercepción de los dos alfabetos es: {interseccionT}"
        

    def InversaTupla(self):
        inversa = list(self.uniontupla)[::-1]
        print(f"La inversa del lenguaje es: {inversa}")

    def Concatenacion(self):
        lenguaje1 = ()
        lenguaje2 = ()
        while True:
            leng1 = input("Digite el primer lenguaje (cadena vacia es #, escriba 'salir' para terminar): ")
            if leng1 == "salir":
                break

            if leng1 == ',' or leng1 ==';' or leng1 =='.' or leng1 == ':' or leng1 =='-' or leng1 == '_' or leng1 == '{' or leng1 == '}' or leng1 == '(' or leng1 == ')' or leng1 == '/' or leng1 == '=' or leng1 =='"' or leng1 == '!' or leng1 == '|' or leng1 == '°':
                print("DATO INVALIDO, ingrese otro valor ")

            elif leng1 == '' or leng1 == '#':
                leng1 = " "
            lenguaje1 = lenguaje1 + (leng1,)

        while True:
            leng2 = input("Digite el primer lenguaje (cadena vacia es #, escriba 'salir' para terminar): ")
            if leng2 == "salir":
                break

            if leng2 == ',' or leng2 ==';' or leng2 =='.' or leng2 == ':' or leng2 =='-' or leng2 == '_' or leng2 == '{' or leng2 == '}' or leng2 == '(' or leng2 == ')' or leng2 == '/' or leng2 == '=' or leng2 =='"' or leng2 == '!' or leng2 == '|' or leng2 == '°':
                print("DATO INVALIDO, ingrese otro valor ")

            elif leng2 == '' or leng2 == '#':
                leng2 = " "
            lenguaje2 = lenguaje2 + (leng2,)

        lenguaje_concatenado = set()
        for palabra1 in lenguaje1:
            for palabra2 in lenguaje2:
                lenguaje_concatenado.add(palabra1 + palabra2)
        self.lenguaje_concatenado = lenguaje_concatenado
        concatenacion = f"La concatenacion de los dos lenguajes es: {lenguaje_concatenado}"
        print(concatenacion)
        return concatenacion
    
    def Cardinalidad(self):
        car = len(self.lenguaje_concatenado)
        print(f"La cardinalidad del lenguaje es: {car}")
        return car
    

if __name__ == '__main__':
    prueba1 = Union([], [])
    prueba1.Crear()
    prueba2 = Diferencia(prueba1.alfabeto1, prueba1.alfabeto2)
    prueba3 = Interseccion(prueba1.alfabeto1, prueba1.alfabeto2)
    prueba4 = CerraduraEstrella(prueba1.alfabeto1, prueba1.alfabeto2)
    print(f"La unión de los alfabetos es: {prueba1.Unir()}")
    prueba2.Diferente()
    print(f"La intersección de los alfabetos es: {prueba3.EncontrarInterseccion()}")
    prueba4.CrearCerraduraEstrella()
    print(f"Los dos lenguajes son: {prueba4.GuardarTuplas()}")
    print(f"La union de los lenguajes es: {prueba4.UnirTuplas()}")
    prueba4.DiferenciaTuplas()
    prueba4.EncontrarInterseccionTupla()
    prueba4.InversaTupla()
    prueba4.Concatenacion()
    prueba4.Cardinalidad()