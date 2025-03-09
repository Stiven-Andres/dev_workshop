class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida

    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):  
            if lista[i] == elemento:  
                return i  
        return -1  
    

    def eliminar_duplicados(self, lista):
        lista_sin_duplicados = []
        elementos_vistos = []

        for elemento in lista:
            if (elemento, type(elemento)) not in elementos_vistos:
                lista_sin_duplicados.append(elemento)
                elementos_vistos.append((elemento, type(elemento))) 

        return lista_sin_duplicados
        

    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0  
        resultado = []

        while i < len(lista1) and j < len(lista2):  
            if lista1[i] <= lista2[j]:  
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista:
            return lista  # Si la lista está vacía, se retorna igual

        k = k % len(lista)  # Para evitar rotaciones innecesarias si k > len(lista)
    
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1  # Como falta un número, el total debería ser len(lista) + 1
        suma_esperada = n * (n + 1) // 2  # Suma de los primeros n números naturales
        suma_actual = sum(lista)  # Suma de los números en la lista

        return suma_esperada - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        
        pila = []

        def push(elemento):
            """Agrega un elemento a la pila."""
            pila.append(elemento)

        def pop():
            """Elimina y devuelve el último elemento de la pila. Retorna None si está vacía."""
            return pila.pop() if pila else None

        def peek():
            """Devuelve el último elemento sin eliminarlo. Retorna None si está vacía."""
            return pila[-1] if pila else None

        def is_empty():
            """Verifica si la pila está vacía."""
            return len(pila) == 0

        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
    
    def implementar_cola(self):
        
        cola = []

        def enqueue(elemento):
            """Agrega un elemento al final de la cola."""
            cola.append(elemento)

        def dequeue():
            """Elimina y devuelve el primer elemento de la cola. Retorna None si está vacía."""
            return cola.pop(0) if cola else None

        def peek():
            """Devuelve el primer elemento sin eliminarlo. Retorna None si está vacía."""
            return cola[0] if cola else None

        def is_empty():
            """Verifica si la cola está vacía."""
            return len(cola) == 0

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
    
    def matriz_transpuesta(self, matriz):

        return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]