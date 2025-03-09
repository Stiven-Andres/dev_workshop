import re
class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())  # Eliminamos espacios y signos, y convertimos a minúsculas
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""  # Inicializamos una cadena vacía
        for caracter in texto:  # Recorremos la cadena original
            resultado = caracter + resultado  # Insertamos cada caracter al inicio del resultado
        return resultado

    
    def contar_vocales(self, texto):

        vocales = "aeiouAEIOU"  # Definimos las vocales (incluyendo mayúsculas)
        contador = 0  # Inicializamos el contador en 0
    
        for caracter in texto:  # Recorremos la cadena
            if caracter in vocales:  # Verificamos si el carácter es una vocal
                contador += 1  # Incrementamos el contador

        return contador

    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"  # Definimos las vocales
        contador = 0  # Inicializamos el contador en 0
        
        for caracter in texto:  # Recorremos la cadena
            if caracter.isalpha() and caracter not in vocales:  # Verificamos si es una consonante
                contador += 1  # Incrementamos el contador

        return contador

    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        pass
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass