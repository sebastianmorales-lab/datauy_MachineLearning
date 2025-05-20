from clase_termo import Termo
from clase_caldera import Caldera

Termo_Ana = Termo("azul", "acero inoxidable", 750)

# y podemos ver el estado del objeto viendo algunos de sus atributos:
print(Termo_Ana)

Termo_Avril = Termo("naranja", "plastico", 750)
print(Termo_Avril)
Termo_Avril.rellenar()
print(Termo_Avril)
Termo_Avril.cebar(60)
print(Termo_Avril)
Termo_Ana.rellenar()
print(Termo_Ana)
Termo_Ana.cebar(100)
print(Termo_Ana)

Caldera.vaciar(10)



