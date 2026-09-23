#principal.py -> usa o modulo
import calculadora as c 
print(c.somar(2, 3))
print (c.PI)

#importando so o que precisa
from calculadora import somar
print (somar(2, 3))   # 5