class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.value)


class CompresionHuffman:
    def __init__(self):
        self.arbol = None

    def comprimir(self, cadena):
        conteo_caracteres = self.contar_caracteres(cadena)
        tuplas_caracteres = self.crear_tuplas(conteo_caracteres)
        tuplas_ordenadas = self.ordenar_tuplas(tuplas_caracteres)
        nodos = self.crear_nodos(tuplas_ordenadas)
        self.arbol = self.construir_arbol_huffman(nodos)
        diccionario_comprimido = self.codificar(self.arbol)
        cadena_comprimida = self.codificar_cadena(diccionario_comprimido, cadena)
        print(cadena_comprimida)
        return diccionario_comprimido

    def contar_caracteres(self, cadena):
        conteo_caracteres = {}
        for caracter in cadena:
            if caracter.isalpha():
                conteo_caracteres[caracter] = conteo_caracteres.get(caracter, 0) + 1
        return conteo_caracteres

    def crear_tuplas(self, conteo_caracteres):
        return [(caracter, conteo) for caracter, conteo in conteo_caracteres.items()]

    def ordenar_tuplas(self, tuplas_caracteres):
        return sorted(tuplas_caracteres, key=lambda x: x[1])

    def crear_nodos(self, tuplas_caracteres):
        nodos = [Nodo(item) for item in tuplas_caracteres]
        return nodos

    def construir_arbol_huffman(self, nodos):
        while len(nodos) > 1:
            nodo1 = nodos.pop(0)
            nodo2 = nodos.pop(0)
            nodo_combinado = Nodo(("_", nodo1.value[1] + nodo2.value[1]))
            nodo_combinado.left = nodo1
            nodo_combinado.right = nodo2
            nodos.append(nodo_combinado)
            nodos.sort(key=lambda x: x.value[1])
        return nodos[0]

    def codificar(self, actual, diccionario_codificado={}, codificacion_actual=""):
        if actual:
            if actual.left:
                self.codificar(actual.left, diccionario_codificado, codificacion_actual + "0")
            if actual.right:
                self.codificar(actual.right, diccionario_codificado, codificacion_actual + "1")
            else:
                diccionario_codificado[actual.value[0]] = codificacion_actual
        return diccionario_codificado

    def codificar_cadena(self, diccionario_codificado, cadena):
        cadena_codificada = "".join(
            diccionario_codificado[caracter] for caracter in cadena if caracter in diccionario_codificado)
        return cadena_codificada

    def imprimir_arbol(self):
        self.imprimir(self.arbol)

    def imprimir(self, nodo, prefijo="", es_izquierdo=True):
        if not nodo:
            print("Árbol Vacío")
            return
        if nodo.right:
            self.imprimir(nodo.right, prefijo + ("│   " if es_izquierdo else "    "), False)
        print(prefijo + ("└── " if es_izquierdo else "┌── ") + str(nodo))
        if nodo.left:
            self.imprimir(nodo.left, prefijo + ("    " if es_izquierdo else "│   "), True)


ch = CompresionHuffman()
print(ch.comprimir("ADELY"))
ch.imprimir_arbol()
