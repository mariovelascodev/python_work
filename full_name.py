fist_name = "ada"
last_name = "lovelace"

"""
"Cadena f", la "f" es de "formato" porque Python formatea la cadena reemplazando 
el nombre de cualquier variable entre llaves con su valor.

"""
full_name = f"{fist_name} {last_name}"
print(full_name)
#Usando  un método con una variable de tipo string
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

#Añadir espacios en blanco o tabulaciones o nuevas lineas
print("Python")
#Usando \t añadimos tabulaciones
print("\tPython")
#Usando \n cambiamos de línea
print("Languages:\nPython\nC\nJavaScript")
#Se pueden combinar tabulaciones y nuevas líneas
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Eliminar prefijos
nostrach_url = 'https://nostrach.com'
nostrach_url.removeprefix('https://') #el método removeprefix no modifica la cadena original
simple_url = nostrach_url.removeprefix('https://')
print(nostrach_url)
print(simple_url)