pares = {
    "(": ")",
    "[": "]",
    "{": "}"
}

aperturas = ["(", "[", "{"]
cierres = [")", "]", "}"]

nombre_archivo = "expresiones.txt"

archivo = open(nombre_archivo, "r")
lineas = archivo.readlines()
archivo.close()

numero_de_linea = 0
resultados = []


print("archivo:", nombre_archivo)


for linea in lineas:
    linea = linea.strip()

    if linea == "":
        continue

    numero_de_linea = numero_de_linea + 1

    print("")
    print("--- Linea", numero_de_linea, ":", linea, "---")

    pila = []
    balanceada = True
    posicion = 0
    paso = 0

    for caracter in linea:
        posicion = posicion + 1

        if caracter in aperturas:
            paso = paso + 1
            pila.append(caracter)
            print("  Paso", paso, "| Pos", posicion, "-> caracter:", caracter, "(apertura) push | pila ahora:", pila)

        elif caracter in cierres:
            if len(pila) == 0:
                paso = paso + 1
                balanceada = False
                print("  Paso", paso, "| Pos", posicion, "-> caracter:", caracter, "(cierre) pop   | error: la pila esta vacia :/")
                break
            else:
                tope = pila[len(pila) - 1]
                if pares[tope] == caracter:
                    paso = paso + 1
                    pila.pop()
                    print("  Paso", paso, "| Pos", posicion, "-> caracter:", caracter, "(cierre) pop   | se quita:", tope, "| Pila ahora:", pila)
                else:
                    paso = paso + 1
                    balanceada = False
                    print("  Paso", paso, "| Pos", posicion, "-> caracter:", caracter, "(cierre) pop   | ERROR: no hace pareja con el tope (", tope, ")")
                    break

    if balanceada == True and len(pila) != 0:
        balanceada = False
        print("  Al terminar la linea quedaron simbolos sin cerrar en la pila:", pila)

    if balanceada == True:
        print("Resultado: BALANCEADA")
        resultados.append((numero_de_linea, linea, "BALANCEADA"))
    else:
        print("Resultado: NO BALANCEADA")
        resultados.append((numero_de_linea, linea, "NO BALANCEADA"))

print("")
print("Resultados:")
for r in resultados:
    print("Linea", r[0], "->", r[2], "->", r[1])