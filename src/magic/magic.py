class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo.")
    
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1  # Inicializamos los dos primeros números de Fibonacci
        for _ in range(2, n + 1):
            a, b = b, a + b  # Se actualizan los valores
        
        return b
    
    def secuencia_fibonacci(self, n):
        
        if n <= 0:
            return []  # Si n es 0 o negativo, devuelve una lista vacía
        elif n == 1:
            return [0]  # Si n es 1, devuelve solo el primer número de Fibonacci
        
        fib = [0, 1]  # Inicializa la lista con los dos primeros números
        for _ in range(2, n):  # Genera los siguientes números hasta n
            fib.append(fib[-1] + fib[-2])  # Suma los dos últimos números y los agrega a la lista
        
        return fib
    
    def es_primo(self, n):
        x = 1
        contador = 0
        while x<=n:
            if n % x ==0:
                contador = contador + 1
            x=x+1

        if contador ==2:
            return True
        else:
            return False
        
    
    def generar_primos(self, n):
        primos = []
        for num in range(2, n + 1):  # Empezamos desde 2 porque 1 no es primo
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def es_numero_perfecto(self, n):
        
        if n < 2:
            return False  # Los números menores que 2 no pueden ser perfectos

        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []  # Si filas es 0 o negativo, devolvemos una lista vacía

        triangulo = [[1]]  # Primera fila siempre es [1]

        for i in range(1, filas):
            fila_anterior = triangulo[-1]  # Última fila generada
            nueva_fila = [1]  # Comenzamos cada fila con 1

            for j in range(1, len(fila_anterior)):
                nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])  # Suma de elementos adyacentes

            nueva_fila.append(1)  # Terminamos la fila con 1
            triangulo.append(nueva_fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        
        pass