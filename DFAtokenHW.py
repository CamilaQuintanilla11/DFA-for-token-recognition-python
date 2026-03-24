def lexerAritmetico(archivo):
    try: 
        with open (archivo, "r") as f:
            for line in f: 
                line = line.strip()

                if line == "":
                    continue

                myDfa(line)

    except FileNotFoundError:
        print("no se leyó el archivo correctamente")

def myDfa(line):
    START = 0
    VARIABLE = 1
    ENTEROS = 2
    REALES = 3
    ERROR = 4

    estado = START 
    token = ""
    i = 0

    while i < len(line):
        current_char = line[i]

        match estado:
            case 0:
                if current_char.isspace():
                    i += 1

                elif current_char.isalpha():
                    token = current_char
                    estado = VARIABLE
                    i += 1

                elif current_char.isdigit():
                    token = current_char
                    estado = ENTEROS
                    i += 1

                elif current_char == ".":
                    token = current_char
                    estado = REALES
                    i += 1
                    
                elif current_char == "/" and i+1 < len(line) and line[i+1] == "/":
                    token = line[i:]
                    print (f"{token}\tComentario")
                    break

                elif current_char == "=":
                    token = current_char
                    print(f"{token}\tAsignación")
                    i += 1

                elif current_char == "+":
                    token = current_char
                    print (f"{token}\tSuma")
                    i += 1

                elif current_char == "-":
                    token = current_char
                    print(f"{token}\tResta")
                    i += 1

                elif current_char == "*":
                    token = current_char
                    print (f"{token}\tMultiplicación")
                    i += 1

                elif current_char == "/":
                    token = current_char
                    print(f"{token}\tDivisión")
                    i += 1

                elif current_char == "^":
                    token = current_char
                    print (f"{token}\tPotencia")
                    i += 1

                elif current_char == "(":
                    token = current_char
                    print (f"{token}\tParéntesis que abre")
                    i += 1
            
                elif current_char == ")":
                    token = current_char
                    print (f"{token}\tParéntesis que cierra")
                    i += 1

                else:
                    print(f"{current_char}\tError. Token no válido")
                    i += 1

            case 1:
                if current_char.isalnum() or current_char == "_":
                    token += current_char
                    i += 1

                else: 
                    print(f"{token}\tVariable")
                    token = ""
                    estado = START

            case 2:
                if current_char.isdigit():
                    token += current_char
                    i += 1
                
                elif current_char == ".":
                    token += current_char
                    estado = REALES
                    i += 1

                elif current_char in "eE":
                    token += current_char
                    estado = REALES
                    i += 1

                elif current_char.isalpha():
                    token += current_char
                    print(f"{token}\tError. Token no válido.")
                    token = ""
                    estado = START
                    i += 1

                else:
                    print(f"{token}\tEntero")
                    token = ""
                    estado = START

            case 3:
                if current_char.isdigit() or current_char in "eE+-":
                    token += current_char
                    i += 1

                elif current_char == ".":
                    token = current_char
                    print(f"{token}\Error. Token no válido")
                    token = ""
                    estado = START
                    i += 1

                else:
                    print(f"{token}\tReal")
                    token = ""
                    estado = START
    if estado == VARIABLE:
        print(f"{token}\tVariable")

    elif estado == ENTEROS:
        print(f"{token}\tEntero")

    elif estado == REALES:
        print(f"{token}\tReal")

lexerAritmetico("pruebadificil.txt")