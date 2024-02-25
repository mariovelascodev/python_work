"""
Use una variable para representar el nombre de una persona e incluya algunos caracteres
de espacio en blanco al principio y al final del nombre. Asegúrese de usar cada combinación
de caracteres, "\t" y "\n", al menos una vez. Imprima el nombre una vez, de modo  que se muestren
los espacios de alrededor.
A continuación, imprima el nombre usando cada una de las tres funciones: lstrip(), rstrip(), strip()
"""

name = "   Ma\trio\n   "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())