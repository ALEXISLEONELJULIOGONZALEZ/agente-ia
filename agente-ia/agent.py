from tools import sumar, restar, convertir_mayusculas

while True:
    pregunta = input("Escribe tu pregunta: ")

    if "suma" in pregunta:
        print("Respuesta:", sumar(5, 3))

    elif "resta" in pregunta:
        print("Respuesta:", restar(10, 4))

    elif "mayusculas" in pregunta:
        print("Respuesta:", convertir_mayusculas("hola profesor"))

    else:
        print("No entiendo la pregunta")