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
        
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()
        
        # Ordenamos los caracteres de ambas cadenas y las comparamos
        return sorted(texto1) == sorted(texto2)

    
    def contar_palabras(self, texto):
        return len(texto.split())

    
    def palabras_mayus(self, texto):
        
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        
        inicio = " " if texto.startswith(" ") else ""  # Un solo espacio si hay espacios iniciales
        fin = " " if texto.endswith(" ") else ""  # Un solo espacio si hay espacios finales

        texto_limpio = " ".join(texto.split())  # Elimina espacios extra entre palabras

        return inicio + texto_limpio + fin

    
    def es_numero_entero(self, texto):
        
        if not texto:  # Verifica si la cadena está vacía
            return False

        if texto[0] in ("-", "+"):  # Permite números negativos y positivos
            texto = texto[1:]  # Elimina el signo para evaluar solo los dígitos
        
        return all("0" <= char <= "9" for char in texto)
    
    def cifrar_cesar(self, texto, desplazamiento):
        cifrado = ""

        for caracter in texto:
            if caracter.isalpha():  # Solo cifrar letras
                ascii_offset = ord('A') if caracter.isupper() else ord('a')
                nuevo_caracter = chr(((ord(caracter) - ascii_offset + desplazamiento) % 26) + ascii_offset)
                cifrado += nuevo_caracter
            else:
                cifrado += caracter  # Mantener espacios y caracteres especiales sin cifrar

        return cifrado

    
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