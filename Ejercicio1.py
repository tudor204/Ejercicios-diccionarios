"""
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""

divisas = {"Euro":"@","Dollar":"$","Yen":"¥"}
moneda = input("Introduce una moneda")
print(divisas.get(moneda.title(),"La divisa no está"))