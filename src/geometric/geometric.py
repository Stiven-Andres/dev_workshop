import math
class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        resultado=base*altura
        return resultado
    
    def perimetro_rectangulo(self, base, altura):
        resultado=(base*2)+(altura*2)
        return resultado
    
    def area_circulo(self, radio):
        resultado=math.pi*radio*radio
        return resultado
    
    def perimetro_circulo(self, radio):
        resultado=math.pi*(radio*2)
        return resultado
    
    def area_triangulo(self, base, altura):
        resultado=(base*altura)/2
        return resultado
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        resultado=lado1+lado2+lado3
        return resultado
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if lado1+lado2>=lado3:
            return True
        else:
            return False
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        resultado=(base_mayor+base_menor)*altura/2
        return resultado
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        resultado=(diagonal_mayor*diagonal_menor)/2
        return resultado
    
    def area_pentagono_regular(self, lado, apotema):
        resultado=(lado*5)*apotema/2
        return resultado
    
    def perimetro_pentagono_regular(self, lado):
        resultado=lado*5
        return resultado
    
    def area_hexagono_regular(self, lado, apotema):
        resultado=((6*lado)*apotema)/2
        return resultado
        
    
    def perimetro_hexagono_regular(self, lado):
        resultado=lado*6
        return resultado
    
    def volumen_cubo(self, lado):
        resultado=lado*lado*lado
        return resultado
    
    def area_superficie_cubo(self, lado):
        resultado=(lado*lado)*6
        return resultado
    
    
    def volumen_esfera(self, radio):
        resultado= (4/3)*math.pi*(radio*radio*radio)
        return resultado
    


    def area_superficie_esfera(self, radio):
        resultado= 4*math.pi*(radio*radio)
        return round(resultado,2)
    

    def volumen_cilindro(self, radio, altura):
        resultado=math.pi*(radio*radio)*altura
        return resultado
    
    def area_superficie_cilindro(self, radio, altura):
        resultado=(2*math.pi*radio*altura)+(2*math.pi*(radio*radio))
        return resultado
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        resultado=math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
        return round(resultado,2)
    
    def punto_medio(self, x1, y1, x2, y2):
        resultado_x=(x1+x2)/2
        resultado_y=(y1+y2)/2

        resultado_gen=(resultado_x,resultado_y)
        return resultado_gen
    
    def pendiente_recta(self, x1, y1, x2, y2):
        resultado=(y2-y1)/(x2-x1)
        return resultado
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            raise ValueError("Los puntos no pueden ser iguales, no definen una recta.")
    
        else:
            A = y2 - y1
            B = x1 - x2
            C = - (A * x1 + B * y1)

            return A, B, C
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        if num_lados==4:
            resultado=lado **2
            return resultado
        else:
            resultado=((num_lados*lado)*apotema)/2
            return round(resultado,2)
    
    def perimetro_poligono_regular(self, num_lados, lado):
        resultado=num_lados*lado
        return resultado
     
