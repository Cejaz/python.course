materias = ["Matemáticas", "Física", "Química", "Sociales", "Lenguaje"]
lista = []
for objeto in materias:
    nota = float(input("¿Qué nota has sacado en " + objeto + "?"))
    if nota >= 5:
        lista.append(objeto)
for objeto in lista:
    materias.remove(objeto)
print("Tienes que repetir " + str(materias))