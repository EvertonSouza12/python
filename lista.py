lista = ["mamão", "banana", "morango"]
lista1 = ["Guitarra", "Bateria", "Baixo"]

print(len(lista))

lista.insert(3, "Melao")

print(lista)

print(len(lista))

lista.append("mamão")

print(lista)

lista.insert(2, "Violão")

print(lista)

lista.append("Violão")

print(lista, lista1)

lista.remove("Violão")

print(lista)

lista.pop(5)

print(lista)

lista.clear()

print(lista, lista1)